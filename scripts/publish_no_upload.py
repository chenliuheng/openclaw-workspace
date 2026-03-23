# 小红书图文发布 - 不需要外部图片上传
# 只用小红书内置的"文字配图"生成封面

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def publish_without_upload():
    options = Options()
    options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
    driver = webdriver.Chrome(options=options)
    
    try:
        # 1. 打开发布页面
        print("1. 打开发布页面...")
        driver.get('https://creator.xiaohongshu.com/publish/publish')
        time.sleep(5)
        
        # 2. 点击"上传图文"tab
        print("2. 点击上传图文...")
        # 尝试查找并点击图文tab
        tabs = driver.find_elements("css selector", ".publish-tab-item, [class*=tab]")
        for t in tabs:
            if "图文" in t.text and "视频" not in t.text:
                t.click()
                print("   点击成功")
                break
        
        time.sleep(3)
        
        # 3. 点击"文字配图"按钮
        print("3. 点击文字配图...")
        try:
            wenzi_btn = driver.find_element("xpath", "//span[contains(text(),'文字配图')]")
            wenzi_btn.click()
            print("   文字配图 clicked")
        except Exception as e:
            print(f"   找不到文字配图按钮: {e}")
        
        time.sleep(5)
        
        # 4. 输入封面文字
        print("4. 输入封面文字...")
        try:
            textarea = driver.find_element("css selector", "textarea, input[type=text], [contenteditable=true]")
            textarea.send_keys("酒店宴会排座神器")
            print("   文字输入成功")
        except Exception as e:
            print(f"   输入失败: {e}")
        
        time.sleep(2)
        
        # 5. 生成图片
        print("5. 点击生成...")
        try:
            generate_btn = driver.find_element("xpath", "//button[contains(text(),'生成')]")
            generate_btn.click()
            print("   生成 clicked")
        except Exception as e:
            print(f"   找不到生成按钮: {e}")
        
        time.sleep(10)
        
        # 截图保存
        driver.save_screenshot('C:/Users/陈流恒/.openclawworkspace/scripts/publish_result.png')
        print("6. 截图保存")
        
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        pass

if __name__ == "__main__":
    publish_without_upload()
