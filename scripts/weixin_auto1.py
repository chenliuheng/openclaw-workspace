from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
driver = webdriver.Chrome(options=options)

driver.get('https://mp.weixin.qq.com/')
time.sleep(5)

# 查找并点击'文章'按钮
js = """
var spans = document.querySelectorAll("span");
for(var i=0; i<spans.length; i++) {
    if(spans[i].textContent && spans[i].textContent.indexOf("文章") > -1 && spans[i].textContent.length < 10) {
        console.log("Found:", spans[i].textContent);
        spans[i].click();
        return "clicked";
    }
}
return "not found";
"""
print(driver.execute_script(js))
time.sleep(3)
driver.save_screenshot('C:/Users/陈流恒/.openclawworkspace/scripts/weixin_step1.png')
driver.quit()
print("Done!")
