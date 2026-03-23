from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import base64

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
driver = webdriver.Chrome(options=options)

try:
    # 打开发布页面
    print("1. 打开发布页面...")
    driver.get('https://creator.xiaohongshu.com/publish/publish?type=image')
    time.sleep(5)
    
    # 读取图片并转为 base64
    print("2. 读取图片...")
    image_path = r'C:\Users\陈流恒\.openclawworkspace\小红书文章配图\article7_cover.png'
    with open(image_path, 'rb') as f:
        img_data = base64.b64encode(f.read()).decode('utf-8')
    print(f"   图片大小: {len(img_data)} bytes")
    
    # 使用 base64 上传
    print("3. 上传图片...")
    js = """
    const fileInput = document.querySelector('input[type="file"]');
    
    // 读取 base64 图片
    const base64String = arguments[0];
    const byteCharacters = atob(base64String);
    const byteNumbers = new Array(byteCharacters.length);
    for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    const byteArray = new Uint8Array(byteNumbers);
    const blob = new Blob([byteArray], {type: 'image/png'});
    
    // 创建文件
    const file = new File([blob], 'article7_cover.png', {type: 'image/png'});
    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    fileInput.files = dataTransfer.files;
    
    console.log('Files:', fileInput.files.length);
    fileInput.dispatchEvent(new Event('change', {bubbles: true}));
    return 'uploaded';
    """
    
    result = driver.execute_script(js, img_data)
    print(f"   上传结果: {result}")
    time.sleep(10)  # 等待上传
    
    # 检查页面
    print("4. 检查结果...")
    print(f"   URL: {driver.current_url}")
    
    # 截图
    driver.save_screenshot('result.png')
    print("   截图已保存")
    
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()

finally:
    driver.quit()
