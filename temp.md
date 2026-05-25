powershell -ExecutionPolicy Bypass -File .\SmsWorkbench\build_dotnet.ps1


uv run python chatgpt_phone_reg.py --chatai-mailbox-file outlook.txt --count 1 --workers 1

uv run python chatgpt_phone_reg.py --email cretebletsch4566@outlook.com --one-click-pay --proxy socks5h://TxnpfSqJ:6tqjyRPrk4vpTN1g@us.proxy302.com:3333