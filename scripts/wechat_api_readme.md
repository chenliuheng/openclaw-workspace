# 微信公众号自动发布方案

## 需要的凭证
要使用微信公众号API，需要：
1. **AppID** (应用ID)
2. **AppSecret** (应用密钥)

这些在公众号后台的"设置与开发" -> "基本配置"中可以找到。

## API 能力

### 已实现功能
1. **获取 access_token** - 调用微信API的凭证
2. **上传图片素材** - 上传封面图等
3. **创建草稿** - 将图文内容存入草稿箱
4. **发布草稿** - 将草稿发布到公众号

### 自动化流程
```
1. 获取 access_token（2小时有效，需缓存）
2. 上传封面图片 → 获取 media_id
3. 构建图文结构 → 创建草稿
4. 获取草稿ID → 自动发布
```

## 代码实现
```python
import requests
import time
import json

class WeChatPublisher:
    def __init__(self, appid, appsecret):
        self.appid = appid
        self.appsecret = appsecret
        self.access_token = None
        self.token_expires = 0
    
    def get_access_token(self):
        """获取access_token"""
        if self.access_token and time.time() < self.token_expires:
            return self.access_token
        
        url = f"https://api.weixin.qq.com/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": self.appid,
            "secret": self.appsecret
        }
        
        resp = requests.get(url, params=params)
        data = resp.json()
        
        if "access_token" in data:
            self.access_token = data["access_token"]
            self.token_expires = time.time() + data.get("expires_in", 7200) - 300
            return self.access_token
        else:
            raise Exception(f"获取token失败: {data}")
    
    def upload_image(self, image_path):
        """上传图片获取media_id"""
        token = self.get_access_token()
        url = f"https://api.weixin.qq.com/cgi-bin/media/uploadimg"
        params = {"access_token": token}
        
        with open(image_path, "rb") as f:
            files = {"media": f}
            resp = requests.post(url, params=params, files=files)
        
        return resp.json()
    
    def create_draft(self, articles):
        """创建草稿"""
        token = self.get_access_token()
        url = f"https://api.weixin.qq.com/cgi-bin/draft/add"
        params = {"access_token": token}
        
        data = {"articles": articles}
        resp = requests.post(url, params=params, json=data)
        
        return resp.json()
    
    def publish_draft(self, media_id):
        """发布草稿"""
        token = self.get_access_token()
        url = f"https://api.weixin.qq.com/cgi-bin/freepublish/submit"
        params = {"access_token": token}
        
        data = {"media_id": media_id}
        resp = requests.post(url, params=params, json=data)
        
        return resp.json()
    
    def auto_publish(self, title, content, cover_image_path, author=""):
        """一键自动发布"""
        # 1. 上传封面图
        print("1. 上传封面图...")
        img_result = self.upload_image(cover_image_path)
        if "media_id" not in img_result:
            raise Exception(f"封面上传失败: {img_result}")
        
        # 2. 构建图文
        article = {
            "title": title,
            "author": author,
            "content": content,
            "content_source_url": "",
            "thumb_media_id": img_result["media_id"],
            "digest": content[:120],
            "show_cover_pic": 1
        }
        
        # 3. 创建草稿
        print("2. 创建草稿...")
        draft_result = self.create_draft([article])
        if "media_id" not in draft_result:
            raise Exception(f"创建草稿失败: {draft_result}")
        
        print(f"   草稿创建成功: {draft_result['media_id']}")
        
        # 4. 发布
        print("3. 发布文章...")
        publish_result = self.publish_draft(draft_result["media_id"])
        
        return publish_result


# 使用示例
if __name__ == "__main__":
    # 需要填入你的公众号AppID和AppSecret
    APPID = "your_appid"
    APPSECRET = "your_appsecret"
    
    publisher = WeChatPublisher(APPID, APPSECRET)
    
    title = "行政姐妹救星！宴会排座10秒搞定"
    content = """姐妹们！酒店宴会排座还在用Excel手动一个一个排吗？
    
    ...正文内容...
    
    #酒店管理 #宴会排座"""
    
    result = publisher.auto_publish(
        title=title,
        content=content,
        cover_image_path="cover.jpg"
    )
    
    print(f"发布结果: {result}")
```

## 待确认
- 公众号的 AppID 和 AppSecret

请提供这些信息，我就可以完成自动化配置！
