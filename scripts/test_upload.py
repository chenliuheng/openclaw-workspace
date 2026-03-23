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
    # 尝试点击"上传图文"按钮
    upload_btns = driver.find_elements(By.XPATH, '//span[contains(text(), "上传图文")]')
    print(f'Found {len(upload_btns)} upload buttons')
    if upload_btns:
        upload_btns[0].click()
        print('Clicked upload')
        time.sleep(3)
        
    # 检查页面
    print('URL:', driver.current_url)
    
    # 截图
    driver.save_screenshot('upload_page.png')
    print('Screenshot saved')
    
except Exception as e:
    print(f'Error: {e}')

driver.quit()
