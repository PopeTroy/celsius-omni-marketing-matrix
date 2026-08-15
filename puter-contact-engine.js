/**
 * ⚡ Celsius Omni-Stack Engine - Puter.js Integrated Storage & File Processing
 * 
 * Features Supported:
 * - puter.fs.mkdir()  -> Directory creation & structure initialization
 * - puter.fs.readdir()-> Batch scanning of uploaded documents & contacts
 * - puter.fs.read()   -> Direct content ingestion (Text/CSV/VCF/Document streams)
 * - puter.fs.stat()   -> Metadata analysis & verification
 * - puter.fs.move()   -> Processed file archival strategy
 * - puter.fs.delete() -> File purging routines
 */

class PuterDocumentContactEngine {
    constructor() {
        this.inputDir = 'incoming_documents';
        this.processedDir = 'processed_documents';
        this.contactsDbPath = 'contacts.json';
    }

    /**
     * Initialize workspace directories using puter.fs.mkdir
     */
    async initializeStorageEnvironment() {
        console.log('⚡ [Puter FS] Initializing cloud directory structures...');
        try {
            await puter.fs.mkdir(this.inputDir, { createParents: true });
            await puter.fs.mkdir(this.processedDir, { createParents: true });
            console.log('✅ [Puter FS] Workspaces verified.');
        } catch (err) {
            console.warn('📁 [Puter FS Notice] Directory check complete:', err.message || err);
        }
    }

    /**
     * Read and load current contact database state from Puter FS
     */
    async loadDatabase() {
        try {
            const fileBlob = await puter.fs.read(this.contactsDbPath);
            const textContent = await fileBlob.text();
            return JSON.parse(textContent);
        } catch (err) {
            console.log('📁 [Puter FS] Primary database missing or empty. Initializing new array.');
            return [];
        }
    }

    /**
     * Commit updated database back to Puter Cloud Storage
     */
    async saveDatabase(database) {
        const jsonContent = JSON.stringify(database, null, 4);
        await puter.fs.write(this.contactsDbPath, jsonContent);
        console.log(`💾 [Puter FS] Core database updated with ${database.length} total entries.`);
    }

    /**
     * Main Processing Loop: Scans, Extracts, Updates, and Archives Files
     */
    async processIncomingFolder() {
        await this.initializeStorageEnvironment();
        let database = await this.loadDatabase();

        console.log(`👁️ [Puter FS] Scanning '${this.inputDir}' for document processing...`);
        const files = await puter.fs.readdir(this.inputDir);

        if (!files || files.length === 0) {
            console.log('📁 [Puter FS] No incoming files found.');
            return;
        }

        let newContactsExtracted = 0;

        for (const fileItem of files) {
            const filePath = `${this.inputDir}/${fileItem.name}`;

            // Check metadata status using puter.fs.stat
            const stats = await puter.fs.stat(filePath);
            if (stats.isDirectory) continue;

            console.log(`📄 Processing Document: ${fileItem.name} (${stats.size} bytes)`);

            // Extract file contents via puter.fs.read
            const fileBlob = await puter.fs.read(filePath);
            const fileText = await fileBlob.text();

            // Extract contacts based on document type
            const extracted = this.extractContactsFromDocument(fileText, fileItem.name);

            // Deduplicate and append new contacts to master list
            for (const item of extracted) {
                if (item.email && !database.some(c => c.email === item.email)) {
                    database.append ? database.push(item) : database.push(item);
                    newContactsExtracted++;
                    console.log(`   ✅ Extracted Contact: ${item.name} <${item.email}> [Tag: ${item.tag}]`);
                }
            }

            // Move processed document to archival folder using puter.fs.move
            const destinationPath = `${this.processedDir}/${fileItem.name}`;
            await puter.fs.move(filePath, destinationPath);
            console.log(`   📦 Archived: ${fileItem.name} -> ${destinationPath}`);
        }

        // Save updated contact array back to Puter storage
        if (newContactsExtracted > 0) {
            await this.saveDatabase(database);
            console.log(`🚀 Processing complete! Successfully added ${newContactsExtracted} new contacts.`);
        } else {
            console.log('👍 Process complete. No new unique contacts found.');
        }
    }

    /**
     * Contact Parsing Routine: Handles CSV, VCF (Contacts), and Raw Document Text (PDF/Word/XLSX text exports)
     */
    extractContactsFromDocument(text, fileName) {
        const contacts = [];
        const ext = fileName.split('.').pop().toLowerCase();

        // Regex patterns for emails and names
        const emailRegex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g;

        if (ext === 'vcf') {
            // VCARD Processing (Contacts File)
            const cards = text.split('END:VCARD');
            for (const card of cards) {
                const fnMatch = card.match(/FN:(.+)/);
                const emailMatch = card.match(/EMAIL.*:(.+)/);
                
                if (emailMatch) {
                    contacts.push({
                        name: fnMatch ? fnMatch[1].trim() : 'VCF Contact',
                        email: emailMatch[1].trim().toLowerCase(),
                        tag: 'VCF Import'
                    });
                }
            }
        } else {
            // Document Extraction (PDF, Word, Excel, PowerPoint text exports, CSV)
            const foundEmails = text.match(emailRegex) || [];
            const uniqueEmails = [...new Set(foundEmails.map(e => e.toLowerCase()))];

            for (const email of uniqueEmails) {
                // Infer potential name context from line containing email
                const line = text.split('\n').find(l => l.toLowerCase().includes(email)) || '';
                const parts = line.split(/[,;\t|]/);
                let name = parts[0] ? parts[0].replace(/[^a-zA-Z\s]/g, '').trim() : '';

                if (!name || name.includes('@')) {
                    name = email.split('@')[0].replace(/[._-]/g, ' ');
                }

                contacts.push({
                    name: name.charAt(0).toUpperCase() + name.slice(1),
                    email: email,
                    tag: `${ext.toUpperCase()} Extracted`
                });
            }
        }

        return contacts;
    }

    /**
     * Purge all processed archives using puter.fs.delete
     */
    async clearProcessedArchive() {
        console.log('🧹 [Puter FS] Clearing processed directory...');
        try {
            await puter.fs.delete(this.processedDir, { recursive: true });
            await puter.fs.mkdir(this.processedDir);
            console.log('✨ [Puter FS] Processed archive cleared.');
        } catch (err) {
            console.error('🚨 [Puter FS Error] Archive purge failed:', err);
        }
    }
}

// Example Usage Context within Puter App/Environment:
// const engine = new PuterDocumentContactEngine();
// await engine.processIncomingFolder();
