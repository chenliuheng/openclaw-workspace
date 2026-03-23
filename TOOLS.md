# Grsai API 配置

## API 配置
- 地址：https://grsai.dakka.com.cn
- Key：sk-bd5389b636e74686a2a16f875ae3de15

## 生图接口
- Endpoint: POST /v1/draw/completions
- 模型：gpt-image-1.5, sora-image

## 使用示例
```python
import requests

url = 'https://grsai.dakka.com.cn/v1/draw/completions'
headers = {
    'Authorization': 'Bearer sk-bd5389b636e74686a2a16f875ae3de15',
    'Content-Type': 'application/json'
}
data = {
    'model': 'gpt-image-1.5',
    'prompt': '你的提示词',
    'size': '1:1'
}

resp = requests.post(url, headers=headers, json=data, stream=True)
# 处理流式响应...
```

## 查询结果
- Endpoint: POST /v1/draw/result
- 需要任务ID
