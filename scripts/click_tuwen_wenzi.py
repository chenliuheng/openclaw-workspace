from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
driver = webdriver.Chrome(options=options)

driver.get('https://creator.xiaohongshu.com/publish/publish?type=image')
time.sleep(5)

# Click on the second '上传图文' button
js = """
const spans = document.querySelectorAll('span');
let count = 0;
for (let s of spans) {
    if (s.textContent && s.textContent.includes("上传图文") && count >= 1) {
        s.click();
        return 'clicked second';
    }
    if (s.textContent && s.textContent.includes("上传图文")) {
        count++;
    }
}
return 'not found';
"""
print(driver.execute_script(js))
time.sleep(3)

# Click 文字配图 button
js2 = """
const buttons = document.querySelectorAll('button, span');
for (let b of buttons) {
    if (b.textContent && b.textContent.includes("文字配图")) {
        b.click();
        return 'clicked 文字配图';
    }
}
return 'not found';
"""
print(driver.execute_script(js2))
time.sleep(3)

driver.save_screenshot('C:/Users/陈流恒/.openclawworkspace/scripts/tuwen_result.png')
print('Screenshot saved')
driver.quit()
