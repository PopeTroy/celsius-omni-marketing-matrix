"""
⚡ Celsius Omni-Stack Engine - Staggered Micro-Batch 10M Transmission Matrix
Handles high-volume queues smoothly using legal delays and server protection blocks.
"""

import os
import json
import time
import math
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class OmniActionBroadcaster:
    def __init__(self):
        self.db_file = 'contacts.json'
        
        # Hyper-Scale Flow Configurations
        self.batch_chunk_size = 5000       # Target block size per active transmission burst
        self.individual_delay = 1.5        # Seconds to rest between single email dispatches
        self.batch_cooldown_delay = 300    # Seconds (5 mins) to rest between 5k blocks

    def process_saved_database(self, tag_filter: str):
        if not os.path.exists(self.db_file):
            print("📁 No active subscriber database file found.")
            return []

        with open(self.db_file, 'r') as f:
            try:
                all_contacts = json.load(f)
            except:
                all_contacts = []

        return [c for c in all_contacts if c.get('tag', '').lower() == tag_filter.lower()]

    def construct_compliant_html(self, subject: str, preview: str, img_url: str, body_text: str, fb: str, li: str, recipient_email: str) -> str:
        banner_img = img_url if img_url else "https://celsiusmediagroup.co.za/assets/banner.webp"
        
        social_elements = ""
        if fb:
            social_elements += f'<td><a href="{fb}" style="color:#a855f7; text-decoration:none; font-weight:bold; margin:0 10px; font-size:13px;">Facebook</a></td>'
        if li:
            social_elements += f'<td><a href="{li}" style="color:#a855f7; text-decoration:none; font-weight:bold; margin:0 10px; font-size:13px;">LinkedIn</a></td>'

        unsubscribe_url = f"https://celsiusmediagroup.co.za/unsubscribe?email={recipient_email}"

        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{subject}</title>
        </head>
        <body style="margin:0; padding:0; background-color:#f8fafc; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
            <div style="display:none; max-height:0px; overflow:hidden; mso-hide:all;">{preview}</div>
            <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px; background-color:#ffffff; margin:30px auto; border:1px solid #e2e8f0; border-radius:12px; overflow:hidden; box-shadow:0 4px 12px rgba(0,0,0,0.03);">
                <tr>
                    <td style="padding:0; background-color:#07050a; text-align:center;">
                        <img src="{banner_img}" alt="Celsius Media Group" style="width:100%; max-width:600px; height:auto; display:block; border:0; margin:0 auto;">
                    </td>
                </tr>
                <tr>
                    <td style="padding:45px 40px; color:#334155; font-size:16px; line-height:1.7;">
                        <h2 style="font-size:24px; color:#0f172a; margin-top:0; margin-bottom:18px; font-weight:700;">{subject}</h2>
                        <p style="margin-top:0; margin-bottom:25px; color:#475569;">{body_text}</p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:35px 40px; background-color:#f8fafc; border-top:1px solid #e2e8f0; text-align:center;">
                        <table align="center" border="0" cellpadding="0" cellspacing="0" style="margin:0 auto 15px auto;">
                            <tr>{social_elements}</tr>
                        </table>
                        <p style="margin:0 0 12px 0; font-size:12px; color:#64748b; line-height:1.6;">
                            <strong>Celsius Technology & Media Group</strong><br>
                            Kempton Park, Gauteng, South Africa<br>
                        </p>
                        <p style="margin:0; font-size:11px; color:#94a3b8;">
                            Refused connection preferences? <a href="{unsubscribe_url}" style="color:#6a0dad; text-decoration:underline; font-weight:bold;">Unsubscribe instantly from this list</a>.
                        </p>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        """

    def broadcast_in_staggered_waves(self, recipients: list, subject: str, preview: str, img_url: str, body_text: str, fb: str, li: str):
        host = os.getenv("SMTP_HOST")
        port = os.getenv("SMTP_PORT", "465")
        user = os.getenv("SMTP_USER")
        password = os.getenv("SMTP_PASS")
        sender = os.getenv("SENDER_EMAIL", user)

        if not all([host, user, password]):
            print("🚨 Missing Mail Server Credentials: SMTP transmission terminated.")
            return False

        total_recipients = len(recipients)
        total_batches = math.ceil(total_recipients / self.batch_chunk_size)
        
        print(f"📊 Hyper-Scale Configured: Segments split into [{total_batches}] logical block arrays.")

        global_counter = 0

        for batch_index in range(total_batches):
            start_offset = batch_index * self.batch_chunk_size
            end_offset = start_offset + self.batch_chunk_size
            current_batch = recipients[start_offset:end_offset]

            print(f"\n📦 Wave [{batch_index + 1}/{total_batches}] Spinning Up — Processing contacts index range {start_offset} to {end_offset}...")
            
            try:
                if port == "465":
                    server = smtplib.SMTP_SSL(host, int(port))
                else:
                    server = smtplib.SMTP(host, int(port))
                    server.starttls()
                    
                server.login(user, password)

                for contact in current_batch:
                    email = contact.get('email')
                    name = contact.get('name', 'Subscriber')

                    if not email or '@' not in email:
                        continue

                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = subject
                    msg['From'] = f"Celsius AI <{sender}>"
                    msg['To'] = f"{name} <{email}>"
                    
                    unsubscribe_url = f"https://celsiusmediagroup.co.za/unsubscribe?email={email}"
                    msg['List-Unsubscribe'] = f"<{unsubscribe_url}>"

                    html_message = self.construct_compliant_html(subject, preview, img_url, body_text, fb, li, email)
                    msg.attach(MIMEText(preview, 'plain'))
                    msg.attach(MIMEText(html_message, 'html'))

                    server.sendmail(sender, [email], msg.as_string())
                    global_counter += 1
                    print(f"   🚀 [{global_counter}] Sent -> {email}")

                    time.sleep(self.individual_delay)

                server.quit()
                print(f"✅ Wave {batch_index + 1} processing concluded successfully.")

                if batch_index < total_batches - 1:
                    print(f"⏳ Cooling down for {self.batch_cooldown_delay} seconds to safeguard IP health parameters...")
                    time.sleep(self.batch_cooldown_delay)

            except Exception as e:
                print(f"🚨 Connection lost or reset mid-transit on wave {batch_index + 1}: {str(e)}")
                print("⏳ Resting system for 30 seconds before trying next wave chunk...")
                time.sleep(30)
                continue

        print(f"\n⚡ Master Engine Complete: Broadcast processed. Total safe deliveries: [{global_counter}] records reached.")
        return True

if __name__ == "__main__":
    subject = os.getenv("CAMPAIGN_SUBJECT", "")
    preview = os.getenv("CAMPAIGN_PREVIEW", "")
    image_url = os.getenv("CAMPAIGN_IMAGE", "")
    body_text = os.getenv("CAMPAIGN_BODY", "")
    target_tag = os.getenv("TARGET_TAG", "General")
    fb_url = os.getenv("LINK_FB", "")
    li_url = os.getenv("LINK_LI", "")

    broadcaster = OmniActionBroadcaster()
    matched_contacts = broadcaster.process_saved_database(target_tag)

    if len(matched_contacts) > 0:
        broadcaster.broadcast_in_staggered_waves(matched_contacts, subject, preview, image_url, body_text, fb_url, li_url)
    else:
        print(f"⚠️ Safe-Stop: Zero contacts match filter: [{target_tag}].")
        global_counter = 0

        # Loop through data arrays using chunks
        for batch_index in range(total_batches):
            start_offset = batch_index * self.batch_chunk_size
            end_offset = start_offset + self.batch_chunk_size
            current_batch = recipients[start_offset:end_offset]

            print(f"\n📦 Wave [{batch_index + 1}/{total_batches}] Spinning Up — Processing contacts index range {start_offset} to {end_offset}...")
            
            try:
                # Open an explicit mail session channel for this batch wave
                if port == "465":
                    server = smtplib.SMTP_SSL(host, int(port))
                else:
                    server = smtplib.SMTP(host, int(port))
                    server.starttls()
                    
                server.login(user, password)

                for contact in current_batch:
                    email = contact.get('email')
                    name = contact.get('name', 'Subscriber')

                    if not email or '@' not in email:
                        continue

                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = subject
                    msg['From'] = f"Celsius AI <{sender}>"
                    msg['To'] = f"{name} <{email}>"
                    
                    unsubscribe_url = f"https://celsiusmediagroup.co.za/unsubscribe?email={email}"
                    msg['List-Unsubscribe'] = f"<{unsubscribe_url}>"

                    html_message = self.construct_compliant_html(subject, preview, img_url, body_text, fb, li, email)
                    msg.attach(MIMEText(preview, 'plain'))
                    msg.attach(MIMEText(html_message, 'html'))

                    # Push individual email out
                    server.sendmail(sender, [email], msg.as_string())
                    global_counter += 1
                    print(f"   🚀 [{global_counter}] Sent -> {email}")

                    # ⏱️ Micro-pause to maintain healthy transit intervals
                    time.sleep(self.individual_delay)

                # Gracefully close session at the end of the current batch block
                server.quit()
                print(f"✅ Wave {batch_index + 1} processing concluded successfully.")

                # 🛑 Macro-cooldown rest loop (Skip if it's the absolute final batch)
                if batch_index < total_batches - 1:
                    print(f"⏳ Cooling down for {self.batch_cooldown_delay} seconds to safeguard IP health parameters...")
                    time.sleep(self.batch_cooldown_delay)

            except Exception as e:
                print(f"🚨 Connection lost or reset mid-transit on wave {batch_index + 1}: {str(e)}")
                print("⏳ Resting system for 30 seconds before trying next wave chunk...")
                time.sleep(30)
                continue

        print(f"\n⚡ Master Engine Complete: Broadcast processed. Total safe deliveries: [{global_counter}] records reached.")
        return True

if __name__ == "__main__":
    subject = os.getenv("CAMPAIGN_SUBJECT", "")
    preview = os.getenv("CAMPAIGN_PREVIEW", "")
    image_url = os.getenv("CAMPAIGN_IMAGE", "")
    body_text = os.getenv("CAMPAIGN_BODY", "")
    target_tag = os.getenv("TARGET_TAG", "General")
    fb_url = os.getenv("LINK_FB", "")
    li_url = os.getenv("LINK_LI", "")

    broadcaster = OmniActionBroadcaster()
    matched_contacts = broadcaster.process_saved_database(target_tag)

    if len(matched_contacts) > 0:
        broadcaster.broadcast_in_staggered_waves(matched_contacts, subject, preview, image_url, body_text, fb_url, li_url)
    else:
        print(f"⚠️ Safe-Stop: Zero contacts match filter: [{target_tag}].")
        user = os.getenv("SMTP_USER")
        password = os.getenv("SMTP_PASS")
        sender = os.getenv("SENDER_EMAIL", user)

        if not all([host, user, password]):
            print("🚨 Missing Mail Server Credentials: SMTP transmission terminated.")
            return False

        print(f"📡 Activating connection pipelines to {host}:{port}...")
        
        try:
            if port == "465":
                server = smtplib.SMTP_SSL(host, int(port))
            else:
                server = smtplib.SMTP(host, int(port))
                server.starttls()
                
            server.login(user, password)

            # Generate beautiful unified layout frame
            html_message = self.construct_rich_html_template(subject, preview, img_url, body_text, fb, li)
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

                part_text = MIMEText(preview, 'plain')
                part_html = MIMEText(html_message, 'html')
                msg.attach(part_text)
                msg.attach(part_html)

                server.sendmail(sender, [email], msg.as_string())
                print(f"🚀 Rich Campaign Stream Delivered to Node: {email}")
                sent_count += 1

            server.quit()
            print(f"\n⚡ Master System Complete: Transmissions clean. Total deliveries: [{sent_count}].")
            return True

        except Exception as e:
            print(f"🚨 Transport Level Exception Triggered: {str(e)}")
            return False

if __name__ == "__main__":
    print("👁️ Tenseigan Core Activation Sequence Initiating...")
    
    subject = os.getenv("CAMPAIGN_SUBJECT", "")
    preview = os.getenv("CAMPAIGN_PREVIEW", "")
    image_url = os.getenv("CAMPAIGN_IMAGE", "")
    body_text = os.getenv("CAMPAIGN_BODY", "")
    target_tag = os.getenv("TARGET_TAG", "General")
    fb_url = os.getenv("LINK_FB", "")
    li_url = os.getenv("LINK_LI", "")

    broadcaster = OmniActionBroadcaster()
    matched_contacts = broadcaster.process_saved_database(target_tag)
    total_count = len(matched_contacts)

    if total_count > 0:
        broadcaster.send_broadcast_emails(matched_contacts, subject, preview, image_url, body_text, fb_url, li_url)
    else:
        print(f"⚠️ Simulation Mode Safe-Stop: Zero contacts found matching filter: [{target_tag}].")
