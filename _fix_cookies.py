#!/usr/bin/env python3
"""Fix cookie handling in paypal_auto.py."""

PAYPAL_AUTO_PATH = "E:/java-demo/GPT-Register-Tool/sms_tool/paypal_auto.py"

with open(PAYPAL_AUTO_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Find the line that imports _import_cookie_header and add a local wrapper
old_import = "from .session_refresh import _import_cookie_header, _poll_auth_session, _session_token"
new_import = "from .session_refresh import _poll_auth_session, _session_token"

if old_import in content:
    content = content.replace(old_import, new_import)
    print("[+] Updated import")

# Add a safe cookie import function after the imports
import_section_end = '''# ──────────────────────────── constants ────────────────────────────'''

safe_cookie_func = '''

def _safe_import_cookie_header(ctx, cookie_header):
    """Safely import cookies into Playwright context."""
    if not cookie_header:
        return

    cookies = []
    for item in str(cookie_header).split(";"):
        if "=" not in item:
            continue
        name, value = item.split("=", 1)
        name = name.strip()
        value = value.strip()
        if not name or not value:
            continue
        # Skip cookies that might cause issues
        if name.startswith("__Host-"):
            continue
        cookie = {
            "name": name,
            "value": value,
            "domain": ".chatgpt.com",
            "path": "/",
        }
        # Only add optional fields if they won't cause issues
        if name.startswith("__Secure-"):
            cookie["secure"] = True
            cookie["httpOnly"] = True
            cookie["sameSite"] = "Lax"
        cookies.append(cookie)

    if cookies:
        try:
            ctx.add_cookies(cookies)
        except Exception as e:
            print(f"[!] Cookie import warning: {e}")

'''

if "_safe_import_cookie_header" not in content:
    content = content.replace(import_section_end, import_section_end + safe_cookie_func)
    print("[+] Added safe cookie import function")

# Replace the call to _import_cookie_header with _safe_import_cookie_header
content = content.replace("_import_cookie_header(ctx,", "_safe_import_cookie_header(ctx,")
print("[+] Updated cookie import call")

with open(PAYPAL_AUTO_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("[*] Cookie handling fixed")
