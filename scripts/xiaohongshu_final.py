"""
小红书自动发布脚本 - 最终版
使用方法: python xiaohongshu_final.py
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import base64

def connect_browser():
    """连接浏览器"""
    options = Options()
    options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
    return webdriver.Chrome(options=options)

def upload_image_with_datatransfer(driver, image_path):
    """使用 DataTransfer 上传图片"""
    # 读取图片并转为 base64
    with open(image_path, 'rb') as f:
        img_data = base64.b64encode(f.read()).decode('utf-8')
    
    js = """
    const fileInput = document.querySelector('input[type="file"]');
    const base64String = arguments[0];
    const byteCharacters = atob(base64String);
    const byteNumbers = new Array(byteCharacters.length);
    for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    const byteArray = new Uint8Array(byteNumbers);
    const blob = new Blob([byteArray], {type: 'image/png'});
    const file = new File([blob], 'cover.png', {type: 'image/png'});
    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    fileInput.files = dataTransfer.files;
    fileInput.dispatchEvent(new Event('change', {bubbles: true}));
    return 'done';
    """
    return driver.execute_script(js, img_data)

def publish_article(image_path, title, content):
    """发布文章"""
    driver = connect_browser()
    
    try:
        # 1. 打开发布页面
        print("1. 打开发布页面...")
        driver.get('https://creator.xiaohongshu.com/publish/publish?type=image')
        time.sleep(5)
        
        # 2. 上传图片
        print("2. 上传图片...")
        result = upload_image_with_datatransfer(driver, image_path)
        print(f"   结果: {result}")
        time.sleep(10)
        
        # 3. 输入标题
        print("3. 输入标题...")
        try:
            title_js = """
            const inputs = document.querySelectorAll('input');
            for (let inp of inputs) {
                if (inp.placeholder && inp.placeholder.includes('标题')) {
                    inp.value = arguments[0];
                    inp.dispatchEvent(new Event('input', {bubbles: true}));
                    return 'done';
                }
            }
            return 'not found';
            """
            driver.execute_script(title_js, title)
        except Exception as e:
            print(f"   标题输入失败: {e}")
        
        time.sleep(2)
        
        # 4. 输入正文
        print("4. 输入正文...")
        try:
            content_js = """
            const editors = document.querySelectorAll('div[contenteditable="true"]');
            if (editors.length > 0) {
                editors[0].innerHTML = arguments[0];
                editors[0].dispatchEvent(new Event('input', {bubbles: true}));
                return 'done';
            }
            return 'not found';
            """
            driver.execute_script(content_js, content.replace('\n', '<br>'))
        except Exception as e:
            print(f"   正文输入失败: {e}")
        
        time.sleep(2)
        
        # 5. 点击发布按钮
        print("5. 点击发布...")
        try:
            publish_js = """
            const buttons = Array.from(document.querySelectorAll('button'));
            const btn = buttons.find(b => b.textContent.includes('发布'));
            if (btn) {
                btn.click();
                return 'clicked';
            }
            return 'not found';
            """
            driver.execute_script(publish_js)
        except Exception as e:
            print(f"   发布失败: {e}")
        
        time.sleep(3)
        print("完成!")
        return True, "执行完成"
        
    except Exception as e:
        return False, str(e)
    finally:
        pass  # 不关闭浏览器

if __name__ == "__main__":
    image_path = r"C:\Users\陈流恒\.openclawworkspace\小红书文章配图\article7_cover.png"
    title = "行政小姐姐的救命神器！再也不用加班改座位了"
    content = """姐妹们！

你们有没有经历过这种绝望：

老板："小王啊，明天宴会200人，座位排一下。"

然后Excel改到第8版的时候，老板说各种调整...

但是！！！
上周我发现了一个神器——智能排座系统！

✅ 3分钟搞定200人座位
✅ 拖拽式调整
✅ 参会人员自己查座位
✅ 临时换人，一键通知

昨天准时下班！老板还夸我效率高！

#行政 #职场干货 #加班神器"""
    
    success, msg = publish_article(image_path, title, content)
    print(f"最终结果: {msg}")
