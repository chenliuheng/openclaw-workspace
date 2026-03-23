from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
driver = webdriver.Chrome(options=options)

# 导航到编辑页面
driver.get('https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&type=10&token=1210270285&lang=zh_CN')
time.sleep(5)

# 点击保存草稿按钮
js = """
var buttons = document.querySelectorAll("button");
for(var i=0; i<buttons.length; i++) {
    if(buttons[i].textContent && buttons[i].textContent.indexOf("保存为草稿") > -1) {
        buttons[i].click();
        return "clicked";
    }
}
return "not found";
"""
print(driver.execute_script(js))

time.sleep(3)
driver.quit()
print('Done!')
