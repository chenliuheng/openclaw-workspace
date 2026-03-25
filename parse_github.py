# -*- coding: utf-8 -*-
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('github_api.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

items = d.get('items', [])
for i, item in enumerate(items[:10]):
    print(f"{i+1}. {item['full_name']}")
    desc = item.get('description', '') or ''
    print(f"   {desc[:100]}")
    print(f"   Stars: {item['stargazers_count']} | Language: {item.get('language', 'N/A')}")
    print(f"   URL: {item['html_url']}")
    print()
