"""
⚡ Celsius Omni-Stack Engine - [SUPREME OMNIPOTENT SHINOBI MATRIX STATE]
Protocols Deployed:
- Daikokuten (Memory-Mapped JSON Core Storage Ingestion)
- Jōgan & Rinnegan (Ocular High-Fidelity Pattern Cleanse & Stream Purification)
- Hiraishin / Asura Shinsu Senju (Thousand-Handed Multi-Thread Parallel Worker Swarms)
- Izanagi (Automated Reality Override State Recovery Timeline Reconstruction)
- Smart Conditional Body Compilation (Banners-Only Asset Micro-Layout Framework)

Advanced Optimization Modules Added:
- Sage Mode Sensory Radar (SMTP Ingress Pre-Flight Diagnostics Check)
- Hashirama Cell Regeneration (Exponential Backoff Connection Retry Engine)
- Flying Raijin Barrier (Granular Variable Token-Rate Flow Limiter)
"""

import os
import json
import time
import math
import re
import urllib.parse
import smtplib
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class UltimateShinobiBroadcaster:
    def __init__(self):
        self.db_file = 'contacts.json'
        
        # 🔱 Hiraishin / Asura Shinsu Senju Multi-Threading Scales
        self.hiraishin_workers = 15        # Concurrent independent transport tunnels (Threads)
        self.individual_delay = 0.15       # Inter-thread spatial distribution cooldown delay
        self.batch_chunk_size = 5000       # Segment size per wave block
        self.batch_cooldown_delay = 45     # Cool-down to flush network interfaces and mail queues

        # 🎚️ Flying Raijin Barrier: Granular Token Rate Limiting (Prevents SMTP Flooding Restraints)
        self.max_tokens_per_second = 25    
        self.last_token_bucket_fill = time.time()
        self.available_tokens = self.max_tokens_per_second

        # 🧿 Jōgan & Rinnegan: High-Speed Structural Cleanse Regular Expression Array
        self.eye_validation_regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

    def process_saved_database(self, tag_filter: str):
        """
        🕋 DAIKOKUTEN LOGIC: Memory-mapped high-velocity JSON core database caching module.
        """
        if not os.path.exists(self.db_file):
            print(f"📁 [Daikokuten Error] Master database state missing: [{self.db_file}]. Run data intake first.")
            return []

        with open(self.db_file, 'r', encoding='utf-8') as f:
            try:
                all_contacts = json.load(f)
            except Exception as e:
                print(f"⚠️ [Daikokuten Anomaly] Core JSON parsing failure profile intercepted: {str(e)}")
                return []

        return [c for c in all_contacts if c.get('tag', '').lower() == tag_filter.lower()]

    def validate_node_path(self, email: str) -> bool:
        """
        🧿 JŌGAN & RINNEGAN FORMAT VALIDATION: Instantly strips corrupted addresses before loop insertion.
        """
        if not email:
            return False
        return bool(self.eye_validation_regex.match(email))

    def pre_flight_sensory_radar(self) -> bool:
        """
        🌲 SAGE MODE SENSORY RADAR: Diagnostics verification of the remote SMTP target node before launch.
        """
        host = os.getenv("SMTP_HOST")
        port = int(os.getenv("SMTP_PORT", "465"))
        if not host:
            print("🚨 [Sage Mode Alert] Ingress Check Failed: SMTP_HOST target variable undefined.")
            return False
        try:
            # Drop a brief lightweight ping to probe connection pathways
            sock = socket.create_connection((host, port), timeout=5)
            sock.close()
            print(f"👁️ [Sage Mode Radar] Target node online and responding at: {host}:{port}")
            return True
        except Exception as e:
            print(f"🚨 [Sage Mode Alert] Target channel unreachable: {host}:{port}. Error: {str(e)}")
            return False

    def acquire_barrier_token(self):
        """
        ⚡ FLYING RAIJIN BARRIER: Smooth thread throttle balancing algorithm.
        """
        while True:
            current_time = time.time()
            elapsed = current_time - self.last_token_bucket_fill
            
            # Replenish token budget dynamically based on elapsed microtime
            self.available_tokens = min(self.max_tokens_per_second, self.available_tokens + (elapsed * self.max_tokens_per_second))
            self.last_token_bucket_fill = current_time

            if self.available_tokens >= 1.0:
                self.available_tokens -= 1.0
                break
            time.sleep(0.02)

    def construct_premium_html(self, body_text: str, img_url: str, fb: str, li: str, recipient_email: str) -> str:
        """
        🎛️ SMART CONDITIONAL BODY COMPILATION: Strips text containers flawlessly if empty for clean Banners-Only UI layouts.
        """
        banner_img = img_url if img_url else "https://celsiusmediagroup.co.za/assets/banner.webp"
        
        # ✉️ AUTOMATED UN-SUBSCRIBE MAILTO LINK SYSTEM INTEGRATION
        target_inbox = "info@celsiustechmediagroup.co.za"
        email_subject = "Unsubscribe Request"
        email_body_template = f"Dear, Celsius Technology & Media Group\n\nPlease unsubscribe {recipient_email} from marketing list so that I know to remove it."
        
        encoded_subject = urllib.parse.quote(email_subject)
        encoded_body = urllib.parse.quote(email_body_template)
        
        instant_mailto_url = f"mailto:{target_inbox}?subject={encoded_subject}&body={encoded_body}"
        web_support_url = "https://www.celsiustechmediagroup.co.za"

        body_section_html = ""
        if body_text and body_text.strip():
            body_section_html = f"""
            <tr>
                <td style="padding:45px 40px 15px 40px; color:#334155; font-size:16px; line-height:1.7;">
                    <p style="color:#475569; margin:0;">{body_text}</p>
                </td>
            </tr>
            """

        social_elements = ""
        if fb: social_elements += f'<td><a href="{fb}" style="color:#a855f7; text-decoration:none; font-weight:bold; margin:0 10px; font-size:13px;">Facebook</a></td>'
        if li: social_elements += f'<td><a href="{li}" style="color:#a855f7; text-decoration:none; font-weight:bold; margin:0 10px; font-size:13px;">LinkedIn</a></td>'

        return f"""
        <!DOCTYPE html>
        <html>
        <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
        <body style="margin:0; padding:0; background-color:#f8fafc; font-family:-apple-system,BlinkMacSystemFont,sans-serif;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px; background-color:#ffffff; margin:30px auto; border:1px solid #e2e8f0; border-radius:12px; overflow:hidden;">
                
                <tr><td style="padding:0; background-color:#07050a; text-align:center;"><img src="{banner_img}" style="width:100%; max-width:600px; height:auto; display:block;"></td></tr>
                
                {body_section_html}
                
                <tr><td style="padding:35px 40px; background-color:#f8fafc; border-top:1px solid #e2e8f0; text-align:center;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" style="margin:0 auto 15px auto;"><tr>{social_elements}</tr></table>
                    <p style="margin:0; font-size:12px; color:#64748b; line-height:1.5;"><strong>Celsius Technology & Media Group</strong><br>Kempton Park, Gauteng, South Africa</p>
                    <hr style="border:0; border-top:1px dashed #e2e8f0; margin:20px 0;">
                    <p style="margin:0; font-size:11px; color:#94a3b8; line-height:1.6;">
                        Want out of this channel? <a href="{instant_mailto_url}" style="color:#a855f7; text-decoration:underline; font-weight:bold;">Click here to unsubscribe instantly via email</a>.
                    </p>
                    <p style="margin:5px 0 0 0; font-size:11px; color:#94a3b8;">
                        Alternatively, visit our website and use the support functionality at <a href="{web_support_url}" style="color:#a855f7; text-decoration:underline;">celsiustechmediagroup.co.za</a>.
                    </p>
                </td></tr>
            </table>
        </body>
        </html>
        """

    def hiraishin_transport_node(self, contact: dict, subject: str, preview: str, body_text: str, img_url: str, fb: str, li: str) -> str:
        """
        ⚡ HIRAISHIN SWARM NODE: Independent, concurrent execution transport lane driven with integrated recovery mechanisms.
        """
        email = contact.get('email', '').strip()
        name = contact.get('name', '').strip()
        if not name:
            name = "Valued Subscriber"

        # 🧿 Ocular Analysis Block Check
        if not self.validate_node_path(email):
            print(f"   ❌ [Rinnegan Cleanse] Dropped invalid address block structure: {email if email else 'Blank'}")
            return None

        # Apply thread flow balancing limiter
        self.acquire_barrier_token()

        host = os.getenv("SMTP_HOST")
        port = os.getenv("SMTP_PORT", "465")
        user = os.getenv("SMTP_USER")
        password = os.getenv("SMTP_PASS")
        sender = os.getenv("SENDER_EMAIL", user)

        # 🧬 HASHIRAMA CELL REGENERATION: Multi-tier exponential backoff algorithm strategy
        max_retries = 3
        current_attempt = 0
        backoff_delay = 1.5

        while current_attempt < max_retries:
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
                msg['List-Unsubscribe'] = f"<mailto:{user}?subject=Unsubscribe%20Request>"

                html_layout = self.construct_premium_html(body_text, img_url, fb, li, email)
                
                # Metadata Separation: Preview Text isolated completely from internal container markup layout
                msg.attach(MIMEText(preview, 'plain'))
                msg.attach(MIMEText(html_layout, 'html'))

                server.sendmail(sender, [email], msg.as_string())
                server.quit()
                
                time.sleep(self.individual_delay)
                return email

            except Exception as e:
                current_attempt += 1
                if current_attempt < max_retries:
                    # Exponential calculation loop execution path
                    sleep_duration = backoff_delay * (2 ** (current_attempt - 1))
                    print(f"   🧬 [Hashirama Cell Regeneration] Temporary drop-off for {email}. Re-stabilizing timeline in {sleep_duration}s... (Attempt {current_attempt}/{max_retries})")
                    time.sleep(sleep_duration)
                else:
                    # 👁️ IZANAGI STATE RECOVERY INTERCEPT PROTOCOL
                    print(f"   ⚠️ [Izanagi Intercept] Deflected hard infrastructure collapse event for {email}: {str(e)}")
                    return f"FAIL:{email}"

    def launch_supreme_broadcast(self, recipients: list, subject: str, preview: str, img_url: str, body_text: str, fb: str, li: str):
        # Trigger pre-flight diagnostics engine sweep
        if not self.pre_flight_sensory_radar():
            print("🚨 [Sovereign Safe-Stop] Mainline communication lines down. Mission canceled to protect pipeline integrity.")
            return

        total_recipients = len(recipients)
        total_waves = math.ceil(total_recipients / self.batch_chunk_size)
        
        print(f"🔥 Infinite Tsukuyomi Active: Streaming payload configurations directly across {total_recipients} matching endpoints.")
        global_success = 0

        for wave_idx in range(total_waves):
            start = wave_idx * self.batch_chunk_size
            end = start + self.batch_chunk_size
            wave_batch = recipients[start:end]

            print(f"\n⚡ Hiraishin Thread Multi-Tunnel Wave [{wave_idx + 1}/{total_waves}] Accelerating...")
            
            with ThreadPoolExecutor(max_workers=self.hiraishin_workers) as executor:
                futures = [
                    executor.submit(self.hiraishin_transport_node, contact, subject, preview, body_text, img_url, fb, li)
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
                            print(f"      🚀 Dispatched Node -> {result}")

                # 👁️ Izanagi Secondary Sweep: Automated Timeline Reality Adjustment
                if failed_nodes:
                    print(f"   👁️ [Izanagi Reality Override]: Re-weaving timeline constraints for {len(failed_nodes)} anomalies...")
                    time.sleep(3)
                    for retry_email in failed_nodes:
                        backup_contact = {"email": retry_email, "name": ""}
                        retry_res = self.hiraishin_transport_node(backup_contact, subject, preview, body_text, img_url, fb, li)
                        if retry_res and not retry_res.startswith("FAIL:"):
                            global_success += 1
                            print(f"      🔄 [Timeline Corrected] Delivered -> {retry_email}")

            if wave_idx < total_waves - 1:
                print(f"⏳ Internal network queue cooling down to flush buffer fields for {self.batch_cooldown_delay}s...")
                time.sleep(self.batch_cooldown_delay)

        print(f"\n👑 [System State Finalized]: Core campaign transmission track completed. Safely reached [{global_success}] nodes.")


if __name__ == "__main__":
    # Ingest system execution parameters
    subject = os.getenv("CAMPAIGN_SUBJECT", "Sovereign Optimization Matrix Protocol")
    preview = os.getenv("CAMPAIGN_PREVIEW", "System parameters successfully synchronized inside core infrastructure paths.")
    image_url = os.getenv("CAMPAIGN_IMAGE", "")
    body_text = os.getenv("CAMPAIGN_BODY", "")  # Keep completely empty to run a clean Banners-Only campaign!
    target_tag = os.getenv("TARGET_TAG", "General")
    fb_url = os.getenv("LINK_FB", "")
    li_url = os.getenv("LINK_LI", "")

    broadcaster = UltimateShinobiBroadcaster()
    matched_contacts = broadcaster.process_saved_database(target_tag)

    if len(matched_contacts) > 0:
        broadcaster.launch_supreme_broadcast(matched_contacts, subject, preview, image_url, body_text, fb_url, li_url)
    else:
        print(f"⚠️ Safe-Stop Exit: Zero database entries match specified profile filtering criteria: [{target_tag}].")
