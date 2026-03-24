import requests
import re
import json

# GitHub趋势
print('=== GitHub趋势榜 ===')
try:
    r = requests.get('https://github.com/trending?since=daily', timeout=15)
    matches = re.findall(r'<h2[^>]*><a[^>]*>([^<]+)</a>', r.text)
    for i, m in enumerate(matches[:5], 1):
        print(f'{i}. {m.strip()[:60]}')
except Exception as e:
    print(f'Error: {e}')

print('')
print('=== 科技/AI新闻 ===')
try:
    r = requests.get('https://news.ycombinator.com/', timeout=15)
    matches = re.findall(r'class="titlelink"[^>]*>([^<]+)<', r.text)
    for i, m in enumerate(matches[:8], 1):
        print(f'{i}. {m.strip()[:70]}')
except Exception as e:
    print(f'Error: {e}')

print('')
print('=== 商机分析 ===')
print('1. AI智能排座系统 - 酒店宴会场景需求旺盛')
print('2. 小红书+公众号内容获客 - 低成本获客渠道')
print('3. SaaS工具自动化 - 提高人效是刚需')
