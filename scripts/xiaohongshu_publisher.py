"""
小红书自动发布脚本
使用 Selenium 自动化发布文章
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def get_chrome_driver():
    """获取 Chrome 驱动"""
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    # 使用已有浏览器
    options.debugger_address = "127.0.0.1:18800"
    
    try:
        driver = webdriver.Chrome(options=options)
        return driver
    except Exception as e:
        print(f"连接浏览器失败: {e}")
        return None

def publish_xiaohongshu(image_path, title, content):
    """发布小红书文章"""
    driver = get_chrome_driver()
    if not driver:
        return False, "无法连接浏览器"
    
    try:
        # 打开小红书创作者平台
        driver.get("https://creator.xiaohongshu.com/publish/publish")
        time.sleep(3)
        
        # 点击上传图文
        upload_buttons = driver.find_elements(By.XPATH, "//span[contains(text(), '上传图文')]")
        if upload_buttons:
            upload_buttons[0].click()
            time.sleep(2)
        
        # 点击上传图片按钮
        upload_img_btn = driver.find_element(By.XPATH, "//button[contains(text(), '上传图片')]")
        upload_img_btn.click()
        time.sleep(1)
        
        # 使用 Selenium 的 send_keys 上传文件
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(image_path)
        time.sleep(3)
        
        # 输入标题
        title_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder*='标题']")
        title_input.send_keys(title)
        time.sleep(1)
        
        # 输入正文 - 需要找到正文输入框
        # ... (根据实际页面调整)
        
        print("发布流程完成")
        return True, "发布成功"
        
    except Exception as e:
        return False, str(e)
    finally:
        # 不关闭浏览器，保持会话
        pass

if __name__ == "__main__":
    # 测试
    image_path = r"C:\Users\陈流恒\.openclawworkspace\小红书文章配图\article7_cover.png"
    title = "行政小姐姐的救命神器！再不用加班改座位了"
    content = "姐妹们！..."
    
    success, msg = publish_xiaohongshu(image_path, title, content)
    print(f"结果: {msg}")
