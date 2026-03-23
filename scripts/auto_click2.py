from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
driver = webdriver.Chrome(options=options)

driver.get('https://creator.xiaohongshu.com/publish/publish')
time.sleep(5)

# Click 上传图文 button
result = driver.execute_script("""
var spans = document.querySelectorAll("span");
for(var i=0; i<spans.length; i++) {
    if(spans[i].textContent && spans[i].textContent.indexOf("上传图文") > -1 && spans[i].textContent.indexOf("上传视频") == -1) {
        spans[i].click();
        break;
    }
}
""")
print("Clicked 上传图文")

time.sleep(3)

# Click 文字配图 button
result2 = driver.execute_script("""
var btns = document.querySelectorAll("button, span");
for(var i=0; i<btns.length; i++) {
    if(btns[i].textContent && btns[i].textContent.indexOf("文字配图") > -1) {
        btns[i].click();
        break;
    }
}
""")
print("Clicked 文字配图")

time.sleep(3)
driver.save_screenshot('C:/Users/陈流恒/.openclawworkspace/scripts/tuwen_wenzi.png')
print("Screenshot saved")

driver.quit()
print("Done!")
