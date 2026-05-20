"""
⚡ Celsius Omni-Stack Engine - [GOD-TIER SHINOBI ENGINE STATE]
Protocols Deployed: 
- Daikokuten (Memory Caching)          - Jōgan & Rinnegan (Format Validation)
- Hiraishin (Parallel Worker Swarms)   - Izanagi (State Recovery)
"""

import os
import json
import time
import math
import re
import smtplib
from concurrent.futures import ThreadPoolExecutor, as_completed
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class GodTierMatrixBroadcaster:
    def __init__(self):
        self.db_file = 'contacts.json'
        
        # 🔱 The Ten-Tails (Jūbi) Scale Parameters
        self.hiraishin_workers = 15        # Parallel space-time worker tunnels (Threads)
        self.individual_delay = 0.15       # Optimal resting delay per single node dispatch
        self.batch_chunk_size = 5000       # Segment size per wave block
        self.batch_cooldown_delay = 45     # Cool-down to flush mail server cache queues

        # 🧿 Jōgan/Rinnegan: High-speed validation expression pattern
        self.email_regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

    def process_saved_database(self, tag_filter: str):
        """
        🕋 DAIKOKUTEN LOGIC: High-velocity data caching mechanism.
        """
        if not os.path.exists(self.db_file):
            print("📁 No active subscriber database file found.")
            return []

        with open(self.db_file, 'r', encoding='utf-8') as f:
            try:
                # Store data in virtual memory for rapid iteration
                all_contacts = json.load(f)
            except Exception as e:
                print(f"⚠️ Failed to decode database file: {str(e)}")
                all_contacts = []

        # Filter down instantly in memory
        return [c for c in all_contacts if c.get('tag', '').lower() == tag_filter.lower()]

    def validate_node_path(self, email: str) -> bool:
        """
        🧿 JŌGAN & RINNEGAN: Scans path structures to remove anomalies.
        """
        if not email:
            return False
        return bool(self.email_regex.match(email))

    def construct_premium_html(self, subject: str, body_text: str, img_url: str, fb: str, li: str, recipient_email: str) -> str:
        banner_img = img_url if img_url else "https://celsiusmediagroup.co.za/assets/banner.webp"
        unsubscribe_url = f"https://celsiusmediagroup.co.za/unsubscribe?email={recipient_email}"
        
        social_elements = ""
        if fb: 
            social_elements += f'<td><a href="{fb}" style="color:#a855f7; text-decoration:none; font-weight:bold; margin:0 10px; font-size:13px;">Facebook</a></td>'
        if li: 
            social_elements += f'<td><a href="{li}" style="color:#a855f7; text-decoration:none; font-weight:bold; margin:0 10px; font-size:13px;">LinkedIn</a></td>'

        return f"""
        <!DOCTYPE html>
        <html>
        <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{subject}</title></head>
        <body style="margin:0; padding:0; background-color:#f8fafc; font-family:-apple-system,BlinkMacSystemFont,sans-serif;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px; background-color:#ffffff; margin:30px auto; border:1px solid #e2e8f0; border-radius:12px; overflow:hidden;">
                <tr><td style="padding:0; background-color:#07050a; text-align:center;"><img src="{banner_img}" style="width:100%; max-width:600px; height:auto; display:block;"></td></tr>
                <tr><td style="padding:45px 40px; color:#334155; font-size:16px; line-height:1.7;">
                    <h2 style="font-size:24px; color:#0f172a; margin-top:0; margin-bottom:18px;">{subject}</h2>
                    <p style="color:#475569;">{body_text}</p>
                </td></tr>
                <tr><td style="padding:35px 40px; background-color:#f8fafc; border-top:1px solid #e2e8f0; text-align:center;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" style="margin:0 auto 15px auto;"><tr>{social_elements}</tr></table>
                    <p style="margin:0; font-size:12px; color:#64748b;"><strong>Celsius Technology & Media Group</strong><br>Kempton Park, Gauteng, South Africa</p>
                    <p style="margin:10px 0 0 0; font-size:11px;"><a href="{unsubscribe_url}" style="color:#6a0dad; text-decoration:underline;">Unsubscribe from this channel</a></p>
                </td></tr>
            </table>
        </body>
        </html>
        """

    def hiraishin_transport_node(self, contact: dict, subject: str, body_text: str, img_url: str, fb: str, li: str) -> str:
        """
        ⚡ HIRAISHIN NO JUTSU: Instantaneous Transport Execution via Sub-Worker Threads
        """
        email = contact.get('email', '').strip()
        name = contact.get('name', '').strip()
        if not name:
            name = "Valued Subscriber"

        # 🧿 Rinnegan structural clean check
        if not self.validate_node_path(email):
            print(f"   ❌ [Rinnegan Cleanse] Dropped corrupted structural address: {email if email else 'Blank'}")
            return None

        host = os.getenv("SMTP_HOST")
        port = os.getenv("SMTP_PORT", "465")
        user = os.getenv("SMTP_USER")
        password = os.getenv("SMTP_PASS")
        sender = os.getenv("SENDER_EMAIL", user)

        try:
            if port == "465":
                server = smtplib.SMTP_SSL(host, int(port), timeout=12)
            else:
                server = smtplib.SMTP(host, int(port), timeout=12)
                server.starttls()
            
            server.login(user, password)

            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = f"Celsius System Node <{sender}>"
            msg['To'] = f"{name} <{email}>"
            msg['List-Unsubscribe'] = f"<https://celsiustechmediagroup.co.za/policies-2?email={email}>"

            html_layout = self.construct_premium_html(subject, body_text, img_url, fb, li, email)
            msg.attach(MIMEText(body_text, 'plain'))
            msg.attach(MIMEText(html_layout, 'html'))

            server.sendmail(sender, [email], msg.as_string())
            server.quit()
            
            time.sleep(self.individual_delay)
            return email

        except Exception as e:
            # 👁️ IZANAGI PROTOCOL: Rewrite transport anomalies into pure illusion
            print(f"   ⚠️ [Izanagi Illusion] Evaded connection dropped event for {email}: {str(e)}")
            return f"FAIL:{email}"

    def launch_god_tier_broadcast(self, recipients: list, subject: str, img_url: str, body_text: str, fb: str, li: str):
        total_recipients = len(recipients)
        total_waves = math.ceil(total_recipients / self.batch_chunk_size)
        
        print(f"🔥 Infinite Tsukuyomi Active: Dispatches streaming to {total_recipients} matching endpoints via Hiraishin Swarms.")
        global_success = 0

        for wave_idx in range(total_waves):
            start = wave_idx * self.batch_chunk_size
            end = start + self.batch_chunk_size
            wave_batch = recipients[start:end]

            print(f"\n⚡ Hiraishin Teleportation Pack [{wave_idx + 1}/{total_waves}] Engaged...")
            
            # Executing multi-worker parallel coordinate delivery
            with ThreadPoolExecutor(max_workers=self.hiraishin_workers) as executor:
                futures = [
                    executor.submit(self.hiraishin_transport_node, contact, subject, body_text, img_url, fb, li)
                    for contact in wave_batch
                ]
                
                failed_nodes = []
                for future in as_completed(futures):
                    result = future.result()
                    if result:
                        if result.startswith("FAIL:"):
                            failed_nodes.append(result.split(":")[1])
                        else:
                            global_success += 1
                            print(f"      🚀 Teleported -> {result}")

                # Izanagi Correction Phase
                if failed_nodes:
                    print(f"   👁️ [Izanagi Reality Override]: Recovering dropped vectors for {len(failed_nodes)} nodes...")
                    time.sleep(3)
                    for retry_email in failed_nodes:
                        backup_contact = {"email": retry_email, "name": "Valued Subscriber"}
                        retry_res = self.hiraishin_transport_node(backup_contact, subject, body_text, img_url, fb, li)
                        if retry_res and not retry_res.startswith("FAIL:"):
                            global_success += 1
                            print(f"      🔄 [Reality Aligned] Delivered -> {retry_email}")

            if wave_idx < total_waves - 1:
                print(f"⏳ Wave processing cooling down for {self.batch_cooldown_delay}s...")
                time.sleep(self.batch_cooldown_delay)

        print(f"\n👑 [Sovereign Master State Concluded]: Infinite delivery stream completed. Reached [{global_success}] points.")


if __name__ == "__main__":
    subject = os.getenv("CAMPAIGN_SUBJECT", "Sovereign Optimization Matrix Protocol")
    image_url = os.getenv("CAMPAIGN_IMAGE", "")
    body_text = os.getenv("CAMPAIGN_BODY", "Transmission parameters successfully synchronized inside core infrastructure paths.")
    target_tag = os.getenv("TARGET_TAG", "General")
    fb_url = os.getenv("LINK_FB", "")
    li_url = os.getenv("LINK_LI", "")

    broadcaster = GodTierMatrixBroadcaster()
    matched_contacts = broadcaster.process_saved_database(target_tag)

    if len(matched_contacts) > 0:
        broadcaster.launch_god_tier_broadcast(matched_contacts, subject, image_url, body_text, fb_url, li_url)
    else:
        print(f"⚠️ Safe-Stop: Zero database profiles match filter tag selection: [{target_tag}].")
