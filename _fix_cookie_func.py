#!/usr/bin/env python3
"""Fix cookie function name in paypal_auto.py."""

PAYPAL_AUTO_PATH = "E:/java-demo/GPT-Register-Tool/sms_tool/paypal_auto.py"

with open(PAYPAL_AUTO_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the double-safe function name
content = content.replace("_safe_safe_import_cookie_header", "_safe_import_cookie_header")

with open(PAYPAL_AUTO_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("[+] Fixed cookie function name")
