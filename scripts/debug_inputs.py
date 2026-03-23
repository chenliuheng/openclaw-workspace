from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
driver = webdriver.Chrome(options=options)

driver.get('https://creator.xiaohongshu.com/publish/publish?type=image')
import time
time.sleep(5)

# 打印所有可输入元素
inputs = driver.find_elements('css selector', 'input')
print('Inputs:', len(inputs))
for i, inp in enumerate(inputs):
    try:
        placeholder = inp.get_attribute('placeholder')
        inp_type = inp.get_attribute('type')
        print(f'{i}: placeholder={placeholder}, type={inp_type}')
    except:
        pass

# 打印所有文本区域
textareas = driver.find_elements('css selector', 'textarea')
print('Textareas:', len(textareas))

# 打印所有 contenteditable 元素
editables = driver.find_elements('css selector', '[contenteditable]')
print('Contenteditables:', len(editables))

driver.quit()
