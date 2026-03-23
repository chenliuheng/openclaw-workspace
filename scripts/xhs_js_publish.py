from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def fix_publish():
    options = Options()
    options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
    driver = webdriver.Chrome(options=options)
    
    # 标题和正文
    title = "行政姐妹救星！宴会排座10秒搞定"
    content = """姐妹们！酒店宴会排座还在用Excel手动一个一个排吗？👋

作为一个酒店行政人员，每次宴会活动最头疼的就是排座问题了！200人的宴会，光是排座就要花上大半天，还经常出错...

今天必须给你们分享这个神器——AI智能排座系统！

✅ 输入宾客名单，一键自动排座，10分钟搞定200人！
✅ 临时换人？群里实时通知，再也不怕信息滞后
✅ 客户隐私保护，再也不用大声喊话换座位啦
✅ 支持多种场景：婚宴、年会、会议、发布会

用了它之后工作效率直接翻倍，老板都夸我安排得井井有条！"""
    
    try:
        # 1. 打开发布页面
        print("1. 打开发布页面...")
        driver.get('https://creator.xiaohongshu.com/publish/publish?type=image')
        time.sleep(5)
        
        # 2. 点击上传图文
        print("2. 点击上传图文...")
        driver.execute_script("""
            var spans = document.querySelectorAll('span');
            for(var i=0; i<spans.length; i++) {
                if(spans[i].textContent && spans[i].textContent.indexOf('上传图文') > -1 && spans[i].textContent.indexOf('上传视频') == -1) {
                    spans[i].click();
                    break;
                }
            }
        """)
        time.sleep(3)
        
        # 3. 点击文字配图
        print("3. 点击文字配图...")
        driver.execute_script("""
            var spans = document.querySelectorAll('span, button');
            for(var i=0; i<spans.length; i++) {
                if(spans[i].textContent && spans[i].textContent.indexOf('文字配图') > -1) {
                    spans[i].click();
                    break;
                }
            }
        """)
        time.sleep(3)
        
        # 4. 输入封面文字
        print("4. 输入封面文字...")
        driver.execute_script("""
            var textareas = document.querySelectorAll('textarea, input[type="text"]');
            for(var i=0; i<textareas.length; i++) {
                if(textareas[i].offsetParent != null) {
                    textareas[i].value = '酒店宴会排座神器';
                    textareas[i].dispatchEvent(new Event('input', {bubbles: true}));
                    break;
                }
            }
        """)
        time.sleep(2)
        
        # 5. 点击生成图片
        print("5. 点击生成图片...")
        driver.execute_script("""
            var elements = document.querySelectorAll('span, button, div');
            for(var i=0; i<elements.length; i++) {
                if(elements[i].textContent && elements[i].textContent.indexOf('生成图片') > -1) {
                    elements[i].click();
                    break;
                }
            }
        """)
        time.sleep(8)
        
        # 6. 点击下一步
        print("6. 点击下一步...")
        driver.execute_script("""
            var buttons = document.querySelectorAll('button');
            for(var i=0; i<buttons.length; i++) {
                if(buttons[i].textContent && buttons[i].textContent.indexOf('下一步') > -1) {
                    buttons[i].click();
                    break;
                }
            }
        """)
        time.sleep(5)
        
        # 7. 使用JavaScript直接填写标题和正文
        print("7. 填写标题和正文...")
        driver.execute_script(f"""
            // 查找所有输入框
            var inputs = document.querySelectorAll('input, textarea, div[contenteditable="true"]');
            
            // 标题框 - 通常是第一个有placeholder的input
            for(var i=0; i<inputs.length; i++) {{
                if(inputs[i].placeholder && inputs[i].placeholder.indexOf('标题') > -1) {{
                    inputs[i].value = '{title}';
                    inputs[i].dispatchEvent(new Event('input', {{bubbles: true}}));
                    console.log('Title filled');
                    break;
                }}
            }}
            
            // 正文框 - 找没有placeholder的div/textarea
            for(var i=0; i<inputs.length; i++) {{
                if((inputs[i].tagName === 'TEXTAREA' || inputs[i].getAttribute('contenteditable') === 'true') 
                   && !inputs[i].placeholder 
                   && inputs[i].offsetParent != null) {{
                    inputs[i].innerHTML = '{content}';
                    inputs[i].dispatchEvent(new Event('input', {{bubbles: true}}));
                    console.log('Content filled');
                    break;
                }}
            }}
        """)
        time.sleep(3)
        
        # 8. 点击发布
        print("8. 点击发布...")
        driver.execute_script("""
            var buttons = document.querySelectorAll('button');
            for(var i=0; i<buttons.length; i++) {
                if(buttons[i].textContent && buttons[i].textContent.indexOf('发布') > -1 && buttons[i].textContent.indexOf('暂存') == -1) {
                    buttons[i].click();
                    console.log('Publish clicked');
                    break;
                }
            }
        """)
        
        time.sleep(5)
        print("完成!")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pass

if __name__ == "__main__":
    fix_publish()
