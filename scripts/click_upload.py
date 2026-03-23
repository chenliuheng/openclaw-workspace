from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
driver = webdriver.Chrome(options=options)

driver.get('https://creator.xiaohongshu.com/publish/publish?type=image')
time.sleep(5)

try:
    # 使用 JavaScript 点击
    js_code = '''
    const buttons = document.querySelectorAll('button, span');
    for (let btn of buttons) {
        if (btn.textContent.includes('上传图文')) {
            console.log('Found:', btn.textContent);
            btn.click();
            return 'clicked';
        }
    }
    return 'not found';
    '''
    result = driver.execute_script(js_code)
    print(f'Result: {result}')
    time.sleep(3)
    
    # 截图
    driver.save_screenshot('after_click.png')
    print('Screenshot saved')
    
except Exception as e:
    print(f'Error: {e}')

driver.quit()
