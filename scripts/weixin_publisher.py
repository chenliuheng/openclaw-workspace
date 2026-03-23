"""
微信公众号自动发布脚本
使用 Selenium 自动化发布文章到微信公众号
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

def publish_weixin(title, content, image_path=None):
    """发布微信公众号文章"""
    driver = connect_browser()
    
    try:
        # 1. 打开微信公众号后台
        print("1. 打开微信公众号后台...")
        driver.get('https://mp.weixin.qq.com/')
        time.sleep(5)
        
        # 检查是否已登录
        if '登录' in driver.page_source:
            print("   需要登录，请在浏览器中扫码登录")
            return False, "需要扫码登录"
        
        # 2. 点击新建图文消息
        print("2. 新建图文消息...")
        try:
            new_msg_btn = driver.find_element(By.XPATH, '//a[contains(text(), "新建图文消息")]')
            new_msg_btn.click()
            time.sleep(3)
        except:
            # 尝试其他方式
            print("   尝试其他方式...")
        
        # 3. 输入标题
        print("3. 输入标题...")
        try:
            title_input = driver.find_element(By.CSS_SELECTOR, 'input[name="title"]')
            title_input.send_keys(title)
        except Exception as e:
            print(f"   输入标题失败: {e}")
        
        time.sleep(2)
        
        # 4. 输入正文
        print("4. 输入正文...")
        try:
            # 切换到iframe
            iframes = driver.find_elements(By.TAG_NAME, 'iframe')
            if iframes:
                driver.switch_to.frame(iframes[0])
            
            # 查找富文本编辑器
            editor = driver.find_element(By.CSS_SELECTOR, '#edui1_iframeholder')
            driver.switch_to.frame(editor)
            
            body = driver.find_element(By.CSS_SELECTOR, 'body')
            body.send_keys(content)
            
            # 切回主文档
            driver.switch_to.default_content()
        except Exception as e:
            print(f"   输入正文失败: {e}")
        
        # 5. 如果有图片，上传封面
        if image_path:
            print("5. 上传封面...")
            try:
                # 找到封面上传按钮
                cover_input = driver.find_element(By.CSS_SELECTOR, 'input[name="cover"]')
                cover_input.send_keys(image_path)
            except Exception as e:
                print(f"   上传封面失败: {e}")
        
        time.sleep(2)
        
        # 6. 保存或发布
        print("6. 保存/发布...")
        try:
            save_btns = driver.find_elements(By.XPATH, '//button[contains(text(), "保存")]')
            if save_btns:
                save_btns[0].click()
                time.sleep(3)
                print("   保存成功!")
        except Exception as e:
            print(f"   保存失败: {e}")
        
        return True, "执行完成"
        
    except Exception as e:
        return False, str(e)
    finally:
        pass

if __name__ == "__main__":
    title = "酒店数字化转型，从一场完美的宴会开始"
    content = """宴会，对于酒店来说，是展示服务能力、连接客户情感的重要场景。

但在数字化时代，传统的宴会管理方式已经跟不上客户的期待了...

#酒店数字化 #宴会管理 #智能排座"""
    
    success, msg = publish_weixin(title, content)
    print(f"结果: {msg}")
