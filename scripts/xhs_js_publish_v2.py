from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def fix_publish_v2():
    options = Options()
    options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
    driver = webdriver.Chrome(options=options)
    
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
        driver.get('https://creator.xiaohongshu.com/publish/publish?type=image')
        time.sleep(5)
        
        # 点击上传图文
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
        
        # 点击文字配图
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
        
        # 输入封面文字
        driver.execute_script("""
            var textareas = document.querySelectorAll('textarea');
            for(var i=0; i<textareas.length; i++) {
                if(textareas[i].offsetParent != null && !textareas[i].placeholder) {
                    textareas[i].value = '酒店宴会排座神器';
                    textareas[i].dispatchEvent(new Event('input', {bubbles: true}));
                    break;
                }
            }
        """)
        time.sleep(2)
        
        # 点击生成图片
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
        
        # 点击下一步
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
        
        # 使用placeholder精确查找标题框
        print("填写标题...")
        driver.execute_script(f"""
            var inputs = document.querySelectorAll('input[placeholder*="标题"], textarea[placeholder*="标题"]');
            for(var i=0; i<inputs.length; i++) {{
                if(inputs[i].offsetParent != null) {{
                    inputs[i].value = '{title}';
                    inputs[i].dispatchEvent(new Event('input', {{bubbles: true}}));
                    console.log('Title filled');
                    break;
                }}
            }}
        """)
        time.sleep(2)
        
        # 查找正文框 - 没有placeholder或包含"真诚分享"
        print("填写正文...")
        driver.execute_script(f"""
            var textareas = document.querySelectorAll('textarea');
            for(var i=0; i<textareas.length; i++) {{
                var ph = textareas[i].getAttribute('placeholder') || '';
                if(ph.indexOf('真诚分享') > -1 || ph.indexOf('标题') == -1) {{
                    if(textareas[i].offsetParent != null) {{
                        textareas[i].value = `{content}`;
                        textareas[i].dispatchEvent(new Event('input', {{bubbles: true}}));
                        console.log('Content filled');
                        break;
                    }}
                }}
            }}
        """)
        time.sleep(3)
        
        # 点击发布
        print("点击发布...")
        driver.execute_script("""
            var buttons = document.querySelectorAll('button');
            for(var i=0; i<buttons.length; i++) {
                if(buttons[i].textContent && buttons[i].textContent.indexOf('发布') > -1 && buttons[i].textContent.indexOf('暂存') == -1) {
                    buttons[i].click();
                    console.log('Published!');
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
    fix_publish_v2()
