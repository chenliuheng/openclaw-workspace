"""
小红书自动发布 - 今天文章测试版
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import base64

def connect_browser():
    options = Options()
    options.add_experimental_option('debuggerAddress', '127.0.0.1:18800')
    return webdriver.Chrome(options=options)

def upload_image(driver, image_path):
    """上传图片"""
    with open(image_path, 'rb') as f:
        img_data = base64.b64encode(f.read()).decode('utf-8')
    
    js = """
    const fileInput = document.querySelector('input[type="file"]');
    const base64String = arguments[0];
    const byteCharacters = atob(base64String);
    const byteNumbers = new Array(byteCharacters.length);
    for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    const byteArray = new Uint8Array(byteNumbers);
    const blob = new Blob([byteArray], {type: 'image/png'});
    const file = new File([blob], 'cover.png', {type: 'image/png'});
    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    fileInput.files = dataTransfer.files;
    fileInput.dispatchEvent(new Event('change', {bubbles: true}));
    return 'done';
    """
    return driver.execute_script(js, img_data)

def publish_today():
    """发布今天的小红书文章"""
    driver = connect_browser()
    
    # 今天文章内容
    title = "行政小姐姐的救命神器！再也不用加班改座位了"
    content = """行政姐妹们集合！🙋‍♀️

你们有没有经历过这种绝望：

老板："小王啊，明天宴会200人，座位排一下。"

我："好的老板。"

然后Excel改到第8版的时候，老板说：" XXX调到3号桌，XXX换成5号桌，XXX不来了..."

我：😵💫

但是！！！

上周我发现了一个神器——智能排座系统！

✅ 3分钟搞定200人座位
✅ 拖拽式调整，想怎么换就怎么换
✅ 参会人员自己查座位，不用我通知
✅ 临时换人？一键通知所有人

昨天准时下班！老板还夸我效率高！

哼，那是因为我有神器！

行政姐妹们，这个真的香！快冲！

💬 你们有什么加班神器？评论区聊聊~

#行政 #职场干货 #加班神器"""
    
    image_path = r"C:\Users\陈流恒\.openclawworkspace\小红书文章配图\article7_cover.png"
    
    try:
        # 1. 打开发布页面
        print("1. 打开发布页面...")
        driver.get('https://creator.xiaohongshu.com/publish/publish?type=image')
        time.sleep(8)
        
        # 2. 上传图片
        print("2. 上传图片...")
        upload_image(driver, image_path)
        print("   图片上传完成")
        time.sleep(15)  # 等待上传处理
        
        # 3. 输入标题
        print("3. 输入标题...")
        title_js = """
        const inputs = document.querySelectorAll('input');
        for (let inp of inputs) {
            if (inp.placeholder && inp.placeholder.includes('标题')) {
                inp.value = arguments[0];
                inp.dispatchEvent(new Event('input', {bubbles: true}));
                return 'done';
            }
        }
        // 尝试其他选择器
        const divs = document.querySelectorAll('div[contenteditable="true"]');
        if (divs.length > 0) {
            divs[0].focus();
            document.execCommand('insertText', false, arguments[0]);
            return 'done-input';
        }
        return 'not found';
        """
        result = driver.execute_script(title_js, title)
        print(f"   标题输入结果: {result}")
        time.sleep(3)
        
        # 4. 输入正文
        print("4. 输入正文...")
        # 尝试多种方式
        content_js = """
        // 方式1: 查找富文本编辑器
        const editors = document.querySelectorAll('div[contenteditable="true"]');
        if (editors.length > 0) {
            // 尝试点击激活
            editors[0].click();
            editors[0].focus();
            // 使用 execCommand 插入内容
            document.execCommand('insertText', false, arguments[0]);
            return 'done-editor';
        }
        
        // 方式2: 查找 textarea
        const textareas = document.querySelectorAll('textarea');
        if (textareas.length > 0) {
            textareas[0].value = arguments[0];
            textareas[0].dispatchEvent(new Event('input', {bubbles: true}));
            return 'done-textarea';
        }
        
        return 'not found';
        """
        result = driver.execute_script(content_js, content)
        print(f"   正文输入结果: {result}")
        time.sleep(3)
        
        # 5. 截图保存当前状态
        print("5. 保存截图...")
        driver.save_screenshot('publish_status.png')
        print("   截图已保存")
        
        # 6. 尝试点击发布
        print("6. 点击发布...")
        publish_js = """
        const buttons = Array.from(document.querySelectorAll('button'));
        const btn = buttons.find(b => b.textContent.includes('发布') && !b.textContent.includes('发布中'));
        if (btn) {
            btn.click();
            return 'clicked';
        }
        // 尝试查找其他可能的发布按钮
        const spans = Array.from(document.querySelectorAll('span'));
        const publishSpan = spans.find(s => s.textContent.includes('发布'));
        if (publishSpan) {
            const parentBtn = publishSpan.closest('button');
            if (parentBtn) {
                parentBtn.click();
                return 'clicked-parent';
            }
        }
        return 'not found';
        """
        result = driver.execute_script(publish_js)
        print(f"   发布点击结果: {result}")
        time.sleep(5)
        
        print("\n完成! 请检查发布结果")
        
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
    finally:
        pass

if __name__ == "__main__":
    publish_today()
