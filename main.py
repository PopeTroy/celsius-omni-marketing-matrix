"""
⚡ Celsius Omni-Stack Engine - Rich Layout SMTP Generation Matrix
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

        filtered_targets = [c for c in all_contacts if c.get('tag', '').lower() == tag_filter.lower()]
        return filtered_targets

    def construct_rich_html_template(self, subject: str, preview: str, img_url: str, body_text: str, fb: str, li: str) -> str:
        """
        Generates a premium, clean, cross-compatible HTML newsletter template structure.
        """
        banner_img = img_url if img_url else "https://celsiusmediagroup.co.za/assets/banner.webp"
        
        # Format social icons layout conditionally based on input links
        social_elements = ""
        if fb:
            social_elements += f'<td><a href="{fb}" style="color:#a855f7; text-decoration:none; font-weight:bold; margin:0 10px; font-size:13px;">Facebook</a></td>'
        if li:
            social_elements += f'<td><a href="{li}" style="color:#a855f7; text-decoration:none; font-weight:bold; margin:0 10px; font-size:13px;">LinkedIn</a></td>'

        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{subject}</title>
        </head>
        <body style="margin:0; padding:0; background-color:#f8fafc; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;">
            
            <div style="display:none; max-height:0px; overflow:hidden; mso-hide:all;">{preview}</div>
            
            <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px; background-color:#ffffff; margin:30px auto; border:1px solid #e2e8f0; border-radius:12px; overflow:hidden; box-shadow:0 4px 12px rgba(0,0,0,0.03);">
                
                <tr>
                    <td style="padding:0; background-color:#07050a; text-align:center;">
                        <img src="{banner_img}" alt="Header Showcase" style="width:100%; max-width:600px; height:auto; display:block; border:0; margin:0 auto;">
                    </td>
                </tr>
                
                <tr>
                    <td style="padding:45px 40px; color:#334155; font-size:16px; line-height:1.7;">
                        <h2 style="font-size:24px; color:#0f172a; margin-top:0; margin-bottom:18px; font-weight:700; letter-spacing:-0.5px;">
                            {subject}
                        </h2>
                        <p style="margin-top:0; margin-bottom:25px; color:#475569;">
                            {body_text}
                        </p>
                    </td>
                </tr>
                
                <tr>
                    <td style="padding:30px 40px; background-color:#f1f5f9; border-top:1px solid #e2e8f0; text-align:center;">
                        
                        <table align="center" border="0" cellpadding="0" cellspacing="0" style="margin:0 auto 15px auto;">
                            <tr>
                                {social_elements if social_elements else '<td><span style="color:#94a3b8;">Stay Connected</span></td>'}
                            </tr>
                        </table>
                        
                        <p style="margin:0; font-size:12px; color:#94a3b8; line-height:1.5;">
                            Sent via the Celsius Omni-Marketing Matrix System.<br>
                            <span style="font-size:11px; color:#cbd5e1; margin-top:5px; display:block;">© 2026 Celsius Technology & Media Group. All Rights Reserved.</span>
                        </p>
                    </td>
                </tr>
            </table>
            
        </body>
        </html>
        """

    def send_broadcast_emails(self, recipients: list, subject: str, preview: str, img_url: str, body_text: str, fb: str, li: str):
        host = os.getenv("SMTP_HOST")
        port = os.getenv("SMTP_PORT", "465")
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
