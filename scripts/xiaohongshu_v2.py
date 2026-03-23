"""
小红书自动发布 - 使用 JavaScript 强制上传
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

def connect_browser():
    options = Options()
    options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
    return webdriver.Chrome(options=options)

def publish_article(image_path, title, content):
    driver = connect_browser()
    
    try:
        # 1. 打开发布页面
        print("1. 打开发布页面...")
        driver.get('https://creator.xiaohongshu.com/publish/publish?type=image')
        time.sleep(5)
        
        # 2. 使用 JavaScript 查找并显示文件输入框
        print("2. 查找文件上传控件...")
        js_code = """
        // 找到所有隐藏的文件输入框
        const inputs = document.querySelectorAll('input[type=\"file\"]');
        for (let input of inputs) {
            input.style.display = 'block';
            input.style.opacity = '1';
            input.style.visibility = 'visible';
            console.log('Found file input:', input);
        }
        return inputs.length;
        """
        result = driver.execute_script(js_code)
        print(f"   找到 {result} 个文件输入框")
        
        # 3. 上传图片
        print("3. 上传图片...")
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        abs_path = os.path.abspath(image_path)
        file_input.send_keys(abs_path)
        print(f"   已选择文件: {abs_path}")
        time.sleep(8)  # 等待上传
        
        # 4. 输入标题
        print("4. 输入标题...")
        try:
            # 尝试多种选择器
            title_selectors = [
                'input[placeholder*=\"标题\"]',
                'input[placeholder*=\"标题\"]',
                'input[class*=\"title\"]'
            ]
            for selector in title_selectors:
                try:
                    title_input = driver.find_element(By.CSS_SELECTOR, selector)
                    title_input.send_keys(title)
                    print("   标题输入成功")
                    break
                except:
                    continue
        except Exception as e:
            print(f"   输入标题失败: {e}")
        
        time.sleep(2)
        
        # 5. 输入正文 - 使用 contenteditable div
        print("5. 输入正文...")
        try:
            content_js = """
            const editors = document.querySelectorAll('div[contenteditable=\"true\"]');
            if (editors.length > 0) {
                editors[0].innerHTML = arguments[0];
                editors[0].dispatchEvent(new Event('input', {bubbles: true}));
                return 'success';
            }
            return 'not found';
            """
            result = driver.execute_script(content_js, content)
            print(f"   正文输入结果: {result}")
        except Exception as e:
            print(f"   输入正文失败: {e}")
        
        time.sleep(2)
        
        # 6. 点击发布按钮
        print("6. 点击发布...")
        try:
            publish_js = """
            const buttons = Array.from(document.querySelectorAll('button'));
            const publishBtn = buttons.find(b => b.textContent.includes('发布') || b.textContent.includes('发記'));
            if (publishBtn) {
                publishBtn.click();
                return 'clicked';
            }
            return 'not found';
            """
            result = driver.execute_script(publish_js)
            print(f"   发布点击结果: {result}")
        except Exception as e:
            print(f"   点击发布失败: {e}")
        
        time.sleep(3)
        print("完成!")
        return True, "执行完成"
        
    except Exception as e:
        return False, str(e)
    finally:
        pass

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
