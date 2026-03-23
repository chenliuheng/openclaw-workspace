from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def publish_weixin():
    options = Options()
    options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
    driver = webdriver.Chrome(options=options)
    
    title = "行政姐妹救星！宴会排座10秒搞定"
    content = """姐妹们！酒店宴会排座还在用Excel手动一个一个排吗？

作为一个酒店行政人员，每次宴会活动最头疼的就是排座问题了！200人的宴会，光是排座就要花上大半天，还经常出错...

今天必须给你们分享这个神器——AI智能排座系统！

✅ 输入宾客名单，一键自动排座，10分钟搞定200人！
✅ 临时换人？群里实时通知，再也不怕信息滞后
✅ 客户隐私保护，再也不用大声喊话换座位啦
✅ 支持多种场景：婚宴、年会、会议、发布会

用了它之后工作效率直接翻倍，老板都夸我安排得井井有条！

#酒店管理 #宴会排座 #行政必备 #职场干货"""
    
    try:
        # 1. 打开发布页面
        print("1. 打开编辑页面...")
        driver.get('https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&type=10&token=1210270285&lang=zh_CN')
        time.sleep(8)
        
        # 2. 输入标题
        print("2. 输入标题...")
        driver.execute_script(f'''
            var inputs = document.querySelectorAll("input");
            for(var i=0; i<inputs.length; i++) {{
                if(inputs[i].placeholder && inputs[i].placeholder.includes("标题")) {{
                    inputs[i].value = "{title}";
                    inputs[i].dispatchEvent(new Event("input", {{bubbles: true}}));
                    console.log("Title set");
                    break;
                }}
            }}
        ''')
        time.sleep(2)
        
        # 3. 点击正文区域并输入
        print("3. 输入正文...")
        driver.execute_script(f'''
            // 点击正文区域激活
            var textareas = document.querySelectorAll("div[contenteditable='true']");
            for(var i=0; i<textareas.length; i++) {{
                if(textareas[i].textContent.includes("从这里开始写正文")) {{
                    textareas[i].click();
                    textareas[i].innerHTML = `{content.replace(chr(10), "<br>")}`;
                    textareas[i].dispatchEvent(new Event("input", {{bubbles: true}}));
                    console.log("Content set");
                    break;
                }}
            }}
        ''')
        time.sleep(3)
        
        # 4. 点击发表按钮
        print("4. 点击发表...")
        driver.execute_script('''
            var buttons = document.querySelectorAll("button");
            for(var i=0; i<buttons.length; i++) {
                if(buttons[i].textContent && buttons[i].textContent.includes("发表")) {
                    buttons[i].click();
                    console.log("Publish clicked");
                    break;
                }
            }
        ''')
        
        time.sleep(5)
        print("完成!")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pass

if __name__ == "__main__":
    publish_weixin()
