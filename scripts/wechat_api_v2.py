"""
微信公众号自动发布 - 修复版
解决中文乱码问题
"""
import requests

class WeChatPublisher:
    def __init__(self, appid, appsecret):
        self.appid = appid
        self.appsecret = appsecret
        self.token = None
    
    def get_token(self):
        url = 'https://api.weixin.qq.com/cgi-bin/token'
        params = {'grant_type': 'client_credential', 'appid': self.appid, 'secret': self.appsecret}
        r = requests.get(url, params=params)
        self.token = r.json()['access_token']
        return self.token
    
    def upload_cover(self, image_path):
        """上传封面图片"""
        token = self.get_token()
        url = 'https://api.weixin.qq.com/cgi-bin/material/add_material'
        with open(image_path, 'rb') as f:
            files = {'media': ('cover.jpg', f, 'image/jpeg')}
            r = requests.post(url, params={'access_token': token, 'type': 'image'}, files=files)
        return r.json()['media_id']
    
    def create_draft(self, title, content, author, thumb_media_id):
        """创建草稿 - 关键：使用charset=utf-8解决中文乱码"""
        token = self.get_token()
        url = 'https://api.weixin.qq.com/cgi-bin/draft/add'
        
        article = {
            'title': title,
            'author': author,
            'content': content,
            'thumb_media_id': thumb_media_id,
            'show_cover_pic': 1
        }
        
        # 关键：添加charset=utf-8
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        r = requests.post(url, params={'access_token': token}, json={'articles': [article]}, headers=headers)
        return r.json()


# 使用示例
if __name__ == "__main__":
    publisher = WeChatPublisher(
        appid='wx12d848b4520f2ed6',
        appsecret='f739baad0e3212611c35d05300bb1dc2'
    )
    
    # 上传封面
    thumb_id = publisher.upload_cover('star.jpg')
    
    # 创建草稿
    result = publisher.create_draft(
        title='宴会排座10秒搞定',
        content='姐妹们！酒店宴会排座还在用Excel手动排吗？...',
        author='老恒',
        thumb_media_id=thumb_id
    )
    print(result)
