import requests
import json
import sys
import os

# 设置输出编码
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://grsai.dakka.com.cn/v1/draw/completions'
headers = {
    'Authorization': 'Bearer sk-bd5389b636e74686a2a16f875ae3de15',
    'Content-Type': 'application/json'
}
data = {
    'model': 'gpt-image-1.5',
    'prompt': 'Swiss style infographic for social media post. Bold text 酒店排座5大坑 in white on solid Klein Blue #0020B0 background. Minimalist design, geometric shapes, Helvetica-style typography. High contrast, clean, professional. 9:16 vertical ratio.',
    'size': '9:16'
}

resp = requests.post(url, headers=headers, json=data)
print('Status:', resp.status_code)
print('Content:', resp.text[:2000] if len(resp.text) > 2000 else resp.text)