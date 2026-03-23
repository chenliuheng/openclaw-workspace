from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def fix_publish():
    options = Options()
    options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
    driver = webdriver.Chrome(options=options)
    
    try:
        # 1. 打开发布页面
        print("1. 打开页面...")
        driver.get('https://creator.xiaohongshu.com/publish/publish?type=image')
        time.sleep(5)
        
        # 2. 点击上传图文 - 用JavaScript
        print("2. 点击上传图文...")
        driver.execute_script("""
            var spans = document.querySelectorAll('span');
            for(var i=0; i<spans.length; i++) {
                if(spans[i].textContent && spans[i].textContent.includes('上传图文') && !spans[i].textContent.includes('上传视频')) {
                    spans[i].click();
                    return;
                }
            }
        """)
        time.sleep(3)
        
        # 3. 点击文字配图
        print("3. 点击文字配图...")
        driver.execute_script("""
            var btns = document.querySelectorAll('button, span');
            for(var i=0; i<btns.length; i++) {
                if(btns[i].textContent && btns[i].textContent.includes('文字配图')) {
                    btns[i].click();
                    return;
                }
            }
        """)
        time.sleep(3)
        
        # 4. 输入封面文字
        print("4. 输入封面文字...")
        driver.execute_script("""
            var textareas = document.querySelectorAll('textarea');
            for(var i=0; i<textareas.length; i++) {
                if(textareas[i].offsetParent != null) {
                    textareas[i].value = '酒店宴会排座神器';
                    return;
                }
            }
        """)
        time.sleep(2)
        
        # 5. 生成图片
        print("5. 生成图片...")
        driver.execute_script("""
            var elements = document.querySelectorAll('span, button');
            for(var i=0; i<elements.length; i++) {
                if(elements[i].textContent && elements[i].textContent.includes('生成图片')) {
                    elements[i].click();
                    return;
                }
            }
        """)
        time.sleep(10)
        
        # 6. 下一步
        print("6. 下一步...")
        driver.execute_script("""
            var buttons = document.querySelectorAll('button');
            for(var i=0; i<buttons.length; i++) {
                if(buttons[i].textContent && buttons[i].textContent.includes('下一步')) {
                    buttons[i].click();
                    return;
                }
            }
        """)
        time.sleep(5)
        
        # 7. 关键修复：用正确的顺序填写标题和正文
        print("7. 填写标题和正文...")
        
        # 先清空并填写标题（第一个有placeholder的输入框）
        driver.execute_script("""
            var inputs = document.querySelectorAll('input, textarea');
            for(var i=0; i<inputs.length; i++) {
                if(inputs[i].placeholder && inputs[i].placeholder.includes('标题') && inputs[i].offsetParent != null) {
                    inputs[i].value = '';
                    inputs[i].focus();
                    // 使用 clipboard API 粘贴
                    return;
                }
            }
        """)
        time.sleep(1)
        
        # 使用 send_keys 直接发送内容到标题框
        title_input = None
        try:
            title_input = driver.find_element("css selector", "input[placeholder*='标题']")
        except:
            pass
        
        if title_input:
            title_input.clear()
            title_input.send_keys("行政姐妹救星！宴会排座10秒搞定")
            print("   标题填写成功")
        else:
            print("   找不到标题框，尝试备用方案")
        
        time.sleep(2)
        
        # 填写正文 - 找到没有placeholder的textarea
        driver.execute_script("""
            var textareas = document.querySelectorAll('textarea');
            for(var i=0; i<textareas.length; i++) {
                var ph = textareas[i].getAttribute('placeholder') || '';
                if((ph.includes('真诚分享') || ph === '') && textareas[i].offsetParent != null) {
                    // 聚焦并输入
                    textareas[i].focus();
                    return;
                }
            }
        """)
        time.sleep(1)
        
        content = """姐妹们！酒店宴会排座还在用Excel手动一个一个排吗？👋

作为一个酒店行政人员，每次宴会活动最头疼的就是排座问题了！200人的宴会，光是排座就要花上大半天，还经常出错...

今天必须给你们分享这个神器——AI智能排座系统！

✅ 输入宾客名单，一键自动排座，10分钟搞定200人！
✅ 临时换人？群里实时通知，再也不怕信息滞后
✅ 客户隐私保护，再也不用大声喊话换座位啦
✅ 支持多种场景：婚宴、年会、会议、发布会

用了它之后工作效率直接翻倍，老板都夸我安排得井井有条！"""
        
        # 找到正文框并输入
        try:
            content_input = driver.find_element("css selector", "textarea:not([placeholder*='标题'])")
            content_input.send_keys(content)
            print("   正文填写成功")
        except Exception as e:
            print(f"   正文字写失败: {e}")
        
        time.sleep(3)
        
        # 8. 发布
        print("8. 点击发布...")
        driver.execute_script("""
            var buttons = document.querySelectorAll('button');
            for(var i=0; i<buttons.length; i++) {
                if(buttons[i].textContent && buttons[i].textContent.includes('发布') && !buttons[i].textContent.includes('暂存')) {
                    buttons[i].click();
                    return;
                }
            }
        """)
        
        print("完成！")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pass

if __name__ == "__main__":
    fix_publish()
