import requests
import json
import time

url = 'https://grsai.dakka.com.cn/v1/draw/completions'
headers = {
    'Authorization': 'Bearer sk-bd5389b636e74686a2a16f875ae3de15',
    'Content-Type': 'application/json'
}
data = {
    'model': 'gpt-image-1.5',
    'prompt': '酒店数字化转型概念图，现代简约风格，深蓝色调，适合微信公众号封面，包含数字化、转型、升级等元素',
    'size': '16:9'
}

resp = requests.post(url, headers=headers, json=data)
print(resp.text)

# 如果返回是task_id，需要查询结果
result = resp.json()
if 'id' in result:
    task_id = result['id']
    # 查询结果
    time.sleep(5)
    result_url = 'https://grsai.dakka.com.cn/v1/draw/result'
    result_data = {'task_id': task_id}
    result_resp = requests.post(result_url, headers=headers, json=result_data)
    print('Result:', result_resp.text)