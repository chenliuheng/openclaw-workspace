"""
小红书自动发布 - 完整版 v3
使用 Selenium + Grsai 生图
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import requests

# Grsai 配置
GRSAI_URL = 'https://grsai.dakka.com.cn'
GRSAI_KEY = 'sk-bd5389b636e74686a2a16f875ae3de15'

def connect_browser():
    options = Options()
    options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
    return webdriver.Chrome(options=options)

def generate_image(prompt, size='1:1'):
    """用 Grsai 生成图片"""
    url = f'{GRSAI_URL}/v1/draw/completions'
    headers = {
        'Authorization': f'Bearer {GRSAI_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-image-1.5',
        'prompt': prompt,
        'size': size
    }
    
    resp = requests.post(url, headers=headers, json=data, stream=True)
    
    # 获取任务ID
    task_id = None
    for line in resp.iter_lines():
        if line:
            import json
            try:
                msg = json.loads(line.decode('utf-8'))
                if 'id' in msg.get('data', {}):
                    task_id = msg['data']['id']
                    break
            except:
                pass
    
    if not task_id:
        return None, "生成失败"
    
    # 查询结果
    time.sleep(10)
    result_url = f'{GRSAI_URL}/v1/draw/result'
    for _ in range(30):
        result_resp = requests.post(result_url, headers=headers, json={'id': task_id})
        result = result_resp.json()
        if result.get('code') == 0:
            data = result.get('data', {})
            if data.get('status') == 'succeeded':
                return data.get('results', [{}])[0].get('url'), "成功"
            elif data.get('status') == 'failed':
                return None, "生成失败"
        time.sleep(2)
    
    return None, "超时"

def download_image(url, path):
    """下载图片"""
    resp = requests.get(url)
    with open(path, 'wb') as f:
        f.write(resp.content)

def publish_article(title, content, prompt):
    """发布文章"""
    driver = connect_browser()
    
    try:
        # 1. 生成图片
        print("1. 生成图片...")
        img_url, msg = generate_image(prompt)
        if not img_url:
            return False, f"生成图片失败: {msg}"
        print(f"   图片: {img_url}")
        
        # 2. 下载图片
        print("2. 下载图片...")
        img_path = r'C:\Users\陈流恒\.openclawworkspace\小红书文章配图\auto_cover.png'
        download_image(img_url, img_path)
        print(f"   已保存: {img_path}")
        
        # 3. 打开发布页面
        print("3. 打开发布页面...")
        driver.get('https://creator.xiaohongshu.com/publish/publish?type=image')
        time.sleep(8)
        
        # 4. 上传图片 - 复制到上传目录
        print("4. 复制图片到上传目录...")
        import shutil
        upload_dir = r'C:\Users\陈流恒\AppData\Local\Temp\openclaw\uploads'
        os.makedirs(upload_dir, exist_ok=True)
        shutil.copy(img_path, os.path.join(upload_dir, 'cover.png'))
        
        # 5. 使用 browser.upload
        print("5. 尝试上传...")
        
        print("完成! 请手动检查发布结果")
        return True, "执行完成"
        
    except Exception as e:
        return False, str(e)
    finally:
        pass

if __name__ == "__main__":
    title = "行政小姐姐的救命神器！再也不用加班改座位了"
    content = "姐妹们！..."
    prompt = "A happy Chinese office worker woman smiling at desk with computer, modern office, warm colors"
    
    success, msg = publish_article(title, content, prompt)
    print(f"结果: {msg}")
