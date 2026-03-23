# Step 1: Click second 上传图文 tab
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
driver = webdriver.Chrome(options=options)

# Navigate to publish page
driver.get('https://creator.xiaohongshu.com/publish/publish')
time.sleep(5)

# Click second 上传图文 button
result = driver.execute_script("""
const spans = document.querySelectorAll('span');
let count = 0;
for (let s of spans) {
    if (s.textContent && s.textContent.includes('上传图文') && count >= 1) {
        s.click();
        return 'clicked second tab';
    }
    if (s.textContent && s.textContent.includes('上传图文')) {
        count++;
    }
}
return 'not found';
""")
print(result)

time.sleep(3)
driver.save_screenshot('C:/Users/陈流恒/.openclawworkspace/scripts/step1.png')

# Click 文字配图 button
result2 = driver.execute_script("""
const buttons = document.querySelectorAll('button, span');
for (let b of buttons) {
    if (b.textContent && b.textContent.includes('文字配图')) {
        b.click();
        return 'clicked 文字配图';
    }
}
return '文字配图 not found';
""")
print(result2)

time.sleep(3)
driver.save_screenshot('C:/Users/陈流恒/.openclawworkspace/scripts/step2.png')
driver.quit()

print("Done!")
