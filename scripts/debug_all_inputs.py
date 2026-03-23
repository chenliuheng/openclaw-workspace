from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
driver = webdriver.Chrome(options=options)

driver.get('https://creator.xiaohongshu.com/publish/publish?type=image')
time.sleep(8)

# 使用 JavaScript 打印页面中所有可能的输入元素
js = """
const results = [];

// 查找所有 input
document.querySelectorAll('input').forEach(el => {
    results.push({
        tag: 'input',
        type: el.type,
        placeholder: el.placeholder,
        id: el.id,
        name: el.name,
        class: el.className
    });
});

// 查找所有 textarea
document.querySelectorAll('textarea').forEach(el => {
    results.push({
        tag: 'textarea',
        placeholder: el.placeholder,
        id: el.id,
        name: el.name
    });
});

// 查找所有 contenteditable
document.querySelectorAll('[contenteditable]').forEach(el => {
    results.push({
        tag: 'contenteditable',
        id: el.id,
        class: el.className
    });
});

// 查找所有带有 role="textbox" 的元素
document.querySelectorAll('[role="textbox"]').forEach(el => {
    results.push({
        tag: 'role=textbox',
        id: el.id,
        class: el.className
    });
});

return JSON.stringify(results, null, 2);
"""

result = driver.execute_script(js)
print(result)

driver.quit()
