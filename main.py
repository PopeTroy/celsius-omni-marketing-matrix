"""
⚡ Celsius Omni-Stack Engine - Outbound SMTP Matrix Delivery Core
"""

import os
import json
import math
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class OmniActionBroadcaster:
    def __init__(self):
        self.ai_nodes = 100
        self.rag_clones = 1000
        self.sectors = 4
        
        self.sector_ai = self.ai_nodes // self.sectors
        self.sector_clones = self.rag_clones // self.sectors

    def process_saved_database(self, tag_filter: str):
        db_file = 'contacts.json'
        if not os.path.exists(db_file):
            print("📁 No active subscriber database file found.")
            return []

        with open(db_file, 'r') as f:
            try:
                all_contacts = json.load(f)
            except:
                all_contacts = []

        # Filter database down to match your exact selection tag
        filtered_targets = [c for c in all_contacts if c.get('tag', '').lower() == tag_filter.lower()]
        return filtered_targets

    def construct_html_template(self, subject: str, preview: str, img_url: str) -> str:
        """
        Builds a high-fidelity, responsive transactional layout frame.
        """
        # Fallback default image placeholder if input field remains empty
        banner_img = img_url if img_url else "https://celsiusmediagroup.co.za/assets/banner.webp"
        
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{subject}</title>
        </head>
        <body style="margin:0; padding:0; background-color:#fafafa; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" max-width="600px" style="background-color:#ffffff; margin:20px auto; border:1px solid #e2e8f0; border-radius:8px; overflow:hidden; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05);">
                <!-- Hidden Preview Text Hook for Inbox Previews -->
                <div style="display:none; max-height:0px; overflow:hidden;">{preview}</div>
                
                <!-- Main Header Image Section -->
                <tr>
                    <td style="padding:0; text-align:center;">
                        <img src="{banner_img}" alt="Celsius Campaign Banner" style="width:100%; max-width:600px; height:auto; display:block; border:0;">
                    </td>
                </tr>
                
                <!-- Core Campaign Body Copy -->
                <tr>
                    <td style="padding:40px 30px; color:#1e293b; font-size:16px; line-height:1.6;">
                        <h1 style="font-size:22px; color:#0f172a; margin-top:0; margin-bottom:20px;">{subject}</h1>
                        <p style="margin-bottom:24px; color:#334155;">
                            {preview}
                        </p>
                        <div style="border-top:1px dashed #e2e8f0; padding-top:20px; font-size:12px; color:#94a3b8; text-align:center;">
                            Sent via Celsius Omni-Marketing Matrix Ecosystem.<br>
                            © 2026 Celsius Technology & Media Group. All Rights Reserved.
                        </div>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        """

    def send_broadcast_emails(self, recipients: list, subject: str, preview: str, img_url: str):
        # Gather SMTP parameters securely from system environment properties
        host = os.getenv("SMTP_HOST")
        port = os.getenv("SMTP_PORT", "465")
        user = os.getenv("SMTP_USER")
        password = os.getenv("SMTP_PASS")
        sender = os.getenv("SENDER_EMAIL", user)

        if not all([host, user, password]):
            print("🚨 Missing Mail Server Credentials: SMTP transmission terminated.")
            print("💡 Action required: Configure SMTP_HOST, SMTP_USER, and SMTP_PASS in GitHub Secrets.")
            return False

        print(f"📡 Establishing contact paths to {host}:{port} via server context...")
        
        try:
            # 1. Connect securely based on common port configurations
            if port == "465":
                server = smtplib.SMTP_SSL(host, int(port))
            else:
                server = smtplib.SMTP(host, int(port))
                server.starttls() # Establish security layers over port 587
                
            server.login(user, password)

            # 2. Iterate through matched contacts loop and dispatch
            html_message = self.construct_html_template(subject, preview, img_url)
            sent_count = 0

            for contact in recipients:
                email = contact.get('email')
                name = contact.get('name', 'Subscriber')

                if not email:
                    continue

                msg = MIMEMultipart('alternative')
                msg['Subject'] = subject
                msg['From'] = f"Celsius AI <{sender}>"
                msg['To'] = f"{name} <{email}>"

                # Standard injection of plain backup and responsive rich-text assets
                part_text = MIMEText(preview, 'plain')
                part_html = MIMEText(html_message, 'html')
                msg.attach(part_text)
                msg.attach(part_html)

                server.sendmail(sender, [email], msg.as_string())
                print(f"🚀 Outbound Stream Delivered Successfully to Node: {email}")
                sent_count += 1

            server.quit()
            print(f"\n⚡ Operational Complete: Outbound lines closed. Delivered {sent_count} tracking nodes.")
            return True

        except Exception as e:
            print(f"🚨 Physical Transport Level Error Encountered: {str(e)}")
            return False

if __name__ == "__main__":
    print("👁️ Tenseigan Core System Initialization: Mapping Repository Arrays...")
    
    subject = os.getenv("CAMPAIGN_SUBJECT", "Default Update Notification")
    preview = os.getenv("CAMPAIGN_PREVIEW", "Opening transmission stream...")
    image_url = os.getenv("CAMPAIGN_IMAGE", "")
    target_tag = os.getenv("TARGET_TAG", "General")

    broadcaster = OmniActionBroadcaster()
    matched_contacts = broadcaster.process_saved_database(target_tag)
    total_count = len(matched_contacts)

    print("\n======================================================================")
    print("⚡ CELSIUS OMNI-MATRIX - BACKEND CAMPAIGN LOG FILE MATRIX")
    print("======================================================================")
    print(f"📧 Campaign Subject Line   : {subject}")
    print(f"📸 Creative Banner Image   : {image_url if image_url else 'None'}")
    print(f"🎯 Filter Target Group Tag : {target_tag}")
    print(f"👥 Total Matched Contacts   : {total_count:,} profiles verified inside repo")
    print("======================================================================\n")
    
    if total_count > 0:
        broadcaster.send_broadcast_emails(matched_contacts, subject, preview, image_url)
    else:
        print(f"⚠️ Transmission Stopped: Zero manual contacts found matching the tag: [{target_tag}].")
        print("💡 Action required: Double check your contact tags match your campaign input filters exactly.")
