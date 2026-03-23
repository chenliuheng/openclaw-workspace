from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def publish_weixin_article():
    """公众号自动发布 - 使用已登录的浏览器"""
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

用了它之后工作效率直接翻倍，老板都夸我安排得井井地道！
    
#酒店管理 #宴会排座 #行政必备 #职场干货"""
    
    try:
        # 1. 直接打开新建图文消息页面（使用token）
        print("1. 打开新建图文消息页面...")
        driver.get('https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&type=10&token=1210270285&lang=zh_CN')
        time.sleep(5)
        
        # 检查是否需要登录
        if '请重新登录' in driver.page_source:
            print("   需要重新登录!")
            return False, "需要扫码登录"
        
        # 2. 输入标题
        print("2. 输入标题...")
        try:
            # 使用JavaScript直接设置标题
            driver.execute_script("""
                var titleInput = document.querySelector('input[name="title"]');
                if(titleInput) {
                    titleInput.value = arguments[0];
                    titleInput.dispatchEvent(new Event('input', {bubbles: true}));
                }
            """, title)
            print("   标题输入成功")
        except Exception as e:
            print(f"   输入标题失败: {e}")
        
        time.sleep(2)
        
        # 3. 输入正文 - 需要切换到iframe
        print("3. 输入正文...")
        try:
            # 切换到富文本编辑器iframe
            driver.switch_to.frame(0)
            
            # 在body中输入内容
            driver.execute_script("""
                var body = document.querySelector('body');
                if(body) {
                    body.innerHTML = arguments[0];
                    body.dispatchEvent(new Event('input', {bubbles: true}));
                }
            """, content.replace('\n', '<br>'))
            
            # 切回主文档
            driver.switch_to.default_content()
            print("   正文输入成功")
        except Exception as e:
            print(f"   输入正文失败: {e}")
            driver.switch_to.default_content()
        
        time.sleep(3)
        
        # 4. 保存或发布
        print("4. 保存...")
        driver.execute_script("""
            var buttons = document.querySelectorAll('button, a');
            for(var i=0; i<buttons.length; i++) {
                if(buttons[i].textContent && buttons[i].textContent.indexOf('保存') > -1) {
                    buttons[i].click();
                    return;
                }
            }
        """)
        
        time.sleep(3)
        print("完成!")
        return True, "执行完成"
        
    except Exception as e:
        return False, str(e)
    finally:
        pass

if __name__ == "__main__":
    success, msg = publish_weixin_article()
    print(f"结果: {msg}")
