"""
微信公众号自动发布 - 完整版
基于官方API实现：素材上传、草稿创建、发布
"""
import requests
import time
import json
import os

class WeChatPublisher:
    def __init__(self, appid, appsecret):
        self.appid = appid
        self.appsecret = appsecret
        self.access_token = None
        self.token_expires = 0
        self.api_base = "https://api.weixin.qq.com/cgi-bin"
    
    def get_access_token(self):
        """获取access_token（带缓存）"""
        if self.access_token and time.time() < self.token_expires:
            print(f"   使用缓存token")
            return self.access_token
        
        print("   获取新token...")
        url = f"{self.api_base}/token"
        params = {
            "grant_type": "client_credential",
            "appid": self.appid,
            "secret": self.appsecret
        }
        
        resp = requests.get(url, params=params, timeout=10)
        data = resp.json()
        
        if "access_token" in data:
            self.access_token = data["access_token"]
            self.token_expires = time.time() + data.get("expires_in", 7200) - 300
            print(f"   Token获取成功: {self.access_token[:20]}...")
            return self.access_token
        else:
            print(f"   Token获取失败: {data}")
            raise Exception(f"获取token失败: {data}")
    
    def upload_image(self, image_path):
        """上传图片素材（用于封面等）"""
        token = self.get_access_token()
        url = f"{self.api_base}/media/uploadimg"
        params = {"access_token": token}
        
        print(f"   上传图片: {image_path}")
        with open(image_path, "rb") as f:
            files = {"media": f}
            resp = requests.post(url, params=params, files=files, timeout=60)
        
        result = resp.json()
        print(f"   上传结果: {result}")
        
        if "url" in result:
            return result["url"]
        elif "media_id" in result:
            return result["media_id"]
        else:
            raise Exception(f"图片上传失败: {result}")
    
    def upload_news_image(self, image_path):
        """上传图文消息内的图片（返回URL用于正文显示）"""
        token = self.get_access_token()
        url = f"{self.api_base}/media/upload"
        params = {
            "access_token": token,
            "type": "image"
        }
        
        print(f"   上传图文图片: {image_path}")
        with open(image_path, "rb") as f:
            files = {"media": f}
            resp = requests.post(url, params=params, files=files, timeout=60)
        
        result = resp.json()
        print(f"   图文图片结果: {result}")
        
        if "media_id" in result:
            return result["media_id"]
        else:
            raise Exception(f"图文图片上传失败: {result}")
    
    def create_draft(self, articles):
        """创建草稿（新建图文素材）"""
        token = self.get_access_token()
        url = f"{self.api_base}/draft/add"
        params = {"access_token": token}
        
        # 处理文章内容，转换换行
        processed_articles = []
        for article in articles:
            processed = article.copy()
            # 确保content是HTML格式
            if "content" in processed:
                # 简单转换换行为<br>
                processed["content"] = processed["content"].replace("\n", "<br>")
            processed_articles.append(processed)
        
        print(f"   创建草稿: {len(processed_articles)}篇文章")
        resp = requests.post(url, params=params, json={"articles": processed_articles}, timeout=30)
        result = resp.json()
        print(f"   草稿结果: {result}")
        
        if "media_id" in result:
            return result["media_id"]
        else:
            raise Exception(f"创建草稿失败: {result}")
    
    def get_draft_count(self):
        """获取草稿数量"""
        token = self.get_access_token()
        url = f"{self.api_base}/draft/count"
        params = {"access_token": token}
        
        resp = requests.get(url, params=params, timeout=10)
        return resp.json()
    
    def get_drafts(self, offset=0, count=10):
        """获取草稿列表"""
        token = self.get_access_token()
        url = f"{self.api_base}/draft/list"
        params = {"access_token": token}
        
        data = {
            "offset": offset,
            "count": count,
            "no_content": 0  # 包含内容
        }
        
        resp = requests.post(url, params=params, json=data, timeout=30)
        return resp.json()
    
    def publish_draft(self, media_id):
        """发布草稿到公众号"""
        token = self.get_access_token()
        url = f"{self.api_base}/freepublish/submit"
        params = {"access_token": token}
        
        print(f"   发布草稿: {media_id}")
        data = {"media_id": media_id}
        resp = requests.post(url, params=params, json=data, timeout=30)
        result = resp.json()
        print(f"   发布结果: {result}")
        
        return result
    
    def auto_publish(self, title, content, cover_image_path, author="", need_publish=True):
        """
        一键自动发布
        
        Args:
            title: 文章标题
            content: 正文内容（支持换行）
            cover_image_path: 封面图片路径
            author: 作者
            need_publish: 是否立即发布，False则只创建草稿
        
        Returns:
            发布结果
        """
        try:
            # 1. 上传封面图
            print("=" * 50)
            print("步骤1: 上传封面图片")
            thumb_media_id = self.upload_image(cover_image_path)
            print(f"   封面上传成功: {thumb_media_id[:30]}...")
            
            # 2. 构建图文结构
            print("=" * 50)
            print("步骤2: 构建图文")
            
            # 摘要取内容前120字
            digest = content[:120] if len(content) > 120 else content
            
            article = {
                "title": title,
                "author": author,
                "content": content,
                "content_source_url": "",
                "thumb_media_id": thumb_media_id,
                "digest": digest,
                "show_cover_pic": 1  # 显示封面
            }
            
            # 3. 创建草稿
            print("=" * 50)
            print("步骤3: 创建草稿")
            media_id = self.create_draft([article])
            print(f"   草稿创建成功: {media_id}")
            
            # 4. 发布
            if need_publish:
                print("=" * 50)
                print("步骤4: 发布文章")
                result = self.publish_draft(media_id)
                print("=" * 50)
                return result
            else:
                print("=" * 50)
                print("已创建草稿，未发布")
                return {"media_id": media_id, "status": "draft_only"}
                
        except Exception as e:
            print(f"错误: {e}")
            return {"error": str(e)}


def test_connection():
    """测试连接"""
    publisher = WeChatPublisher(
        appid="wx12d848b4520f2ed6",
        appsecret="f739baad0e3212611c35d05300bb1dc2"
    )
    
    try:
        token = publisher.get_access_token()
        print(f"✅ 连接成功! Token: {token[:30]}...")
        return True
    except Exception as e:
        print(f"❌ 连接失败: {e}")
        return False


if __name__ == "__main__":
    test_connection()
