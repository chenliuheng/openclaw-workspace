from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
driver = webdriver.Chrome(options=options)

# 打开发布页面
driver.get('https://creator.xiaohongshu.com/publish/publish?type=image')
time.sleep(5)

# 使用 DataTransfer 上传文件
image_path = r'C:\Users\陈流恒\.openclawworkspace\小红书文章配图\article7_cover.png'
abs_path = os.path.abspath(image_path)

js = """
const fileInput = document.querySelector('input[type="file"]');
const file = new File([""], arguments[0], {type: "image/png"});
const dataTransfer = new DataTransfer();
dataTransfer.items.add(file);
fileInput.files = dataTransfer.files;
fileInput.dispatchEvent(new Event('change', {bubbles: true}));
return 'uploaded';
"""

result = driver.execute_script(js, abs_path)
print('Result:', result)
time.sleep(5)

driver.quit()
