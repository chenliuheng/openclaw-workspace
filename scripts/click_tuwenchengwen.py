from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
driver = webdriver.Chrome(options=options)

driver.get('https://creator.xiaohongshu.com/publish/publish?type=image')
time.sleep(10)

# 查找并点击上传图文按钮
js = """
const buttons = document.querySelectorAll('button, span, div');
for (let b of buttons) {
    if (b.textContent && b.textContent.includes('上传图文') && !b.textContent.includes('上传视频')) {
        console.log('Found button:', b.textContent);
        b.click();
        return 'clicked';
    }
}
return 'not found';
"""
result = driver.execute_script(js)
print('Result:', result)

time.sleep(3)
driver.save_screenshot('C:/Users/陈流恒/.openclawworkspace/scripts/after_click.png')
driver.quit()
