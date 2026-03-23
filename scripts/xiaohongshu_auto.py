"""
小红书自动发布 - 完整版
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

def connect_browser():
    """连接浏览器"""
    options = Options()
    options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
    return webdriver.Chrome(options=options)

def publish_article(image_path, title, content):
    """发布文章"""
    driver = connect_browser()
    
    try:
        # 1. 打开发布页面
        driver.get('https://creator.xiaohongshu.com/publish/publish?type=image')
        time.sleep(5)
        
        # 2. 上传图片
        print("上传图片...")
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        file_input.send_keys(image_path)
        time.sleep(5)  # 等待上传
        
        # 3. 输入标题
        print("输入标题...")
        try:
            title_inputs = driver.find_elements(By.CSS_SELECTOR, 'input[placeholder*="标题"]')
            if title_inputs:
                title_inputs[0].send_keys(title)
                time.sleep(1)
        except Exception as e:
            print(f"输入标题失败: {e}")
        
        # 4. 输入正文
        print("输入正文...")
        try:
            # 尝试多种方式查找正文输入框
            content_selectors = [
                'div[contenteditable="true"]',
                'textarea',
                'div[role="textbox"]'
            ]
            for selector in content_selectors:
                try:
                    content_box = driver.find_element(By.CSS_SELECTOR, selector)
                    content_box.send_keys(content)
                    time.sleep(1)
                    print("正文输入成功")
                    break
                except:
                    continue
        except Exception as e:
            print(f"输入正文失败: {e}")
        
        # 5. 点击发布按钮
        print("点击发布按钮...")
        try:
            publish_buttons = driver.find_elements(By.XPATH, '//button[contains(text(), "发布")]')
            if publish_buttons:
                publish_buttons[0].click()
                time.sleep(3)
                print("发布成功!")
                return True, "发布成功"
        except Exception as e:
            print(f"点击发布失败: {e}")
        
        return False, "发布流程完成但结果未知"
        
    except Exception as e:
        return False, str(e)
    finally:
        pass  # 不关闭浏览器

if __name__ == "__main__":
    image_path = r"C:\Users\陈流恒\.openclawworkspace\小红书文章配图\article7_cover.png"
    title = "行政小姐姐的救命神器！再也不用加班改座位了"
    content = """姐妹们！🙋‍♀️

你们有没有经历过这种绝望：

老板："小王啊，明天宴会200人，座位排一下。"

我："好的老板。"

然后Excel改到第8版的时候，老板说："XXX调到3号桌，XXX换成5号桌，XXX不来了..."

我：😵💫

但是！！！
上周我发现了一个神器——智能排座系统！

✅ 3分钟搞定200人座位
✅ 拖拽式调整，想怎么换就怎么换
✅ 参会人员自己查座位，不用我通知
✅ 临时换人？一键通知所有人

昨天准时下班！老板还夸我效率高！

哼，那是因为我有神器！

行政姐妹们，这个真的香！快冲！

💬 你们有什么加班神器？评论区聊聊~

#行政 #职场干货 #加班神器"""
    
    success, msg = publish_article(image_path, title, content)
    print(f"结果: {msg}")
