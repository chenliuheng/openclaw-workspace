from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
driver = webdriver.Chrome(options=options)

time.sleep(2)

# Fill title
title_js = """
var titleInput = document.querySelector('input[placeholder*=title]');
if(!titleInput) titleInput = document.querySelector('input[placeholder*=标]');
if(titleInput) {
    titleInput.value = "行政姐妹救星！宴会排座10秒搞定";
    titleInput.dispatchEvent(new Event('input', {bubbles: true}));
    titleInput.dispatchEvent(new Event('change', {bubbles: true}));
}
"""
result = driver.execute_script(title_js)
print('Title filled')

time.sleep(1)

# Fill body
body_js = """
var textareas = document.querySelectorAll('textarea, div[contenteditable]');
for(var t of textareas) {
    if(t.offsetParent !== null && t.innerHTML.length < 100 && t.innerText.length < 100) {
        t.innerHTML = "姐妹们！酒店宴会排座还在用Excel手动一个一个排吗？👋<br><br>作为一个酒店行政人员，每次宴会活动最头疼的就是排座问题了！200人的宴会，光是排座就要花上大半天，还经常出错...<br><br今天必须给你们分享这个神器——AI智能排座系统！<br><br>✅ 输入宾客名单，一键自动排座，10分钟搞定200人！<br>✅ 临时换人？群里实时通知，再也不怕信息滞后<br>✅ 客户隐私保护，再也不用大声喊话换座位啦<br>✅ 支持多种场景：婚宴、年会、会议、发布会<br><br>用了它之后工作效率直接翻倍，老板都夸我安排得井井有条！<br><br>#酒店管理 #宴会排座 #行政必备 #职场干货 #酒店人 #会议策划";
        return 'body filled';
    }
}
return 'body not found';
"""
result2 = driver.execute_script(body_js)
print('Body result:', result2)

time.sleep(2)
driver.save_screenshot('C:/Users/陈流恒/.openclawworkspace/scripts/filled_result.png')
print('Done')
driver.quit()
