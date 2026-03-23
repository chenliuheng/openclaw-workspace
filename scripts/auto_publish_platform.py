"""
运营文章自动发布平台
统一调度：小红书 + 微信公众号
"""
import os
import sys

def get_articles_from_feishu():
    """从飞书表格获取今天需要发布的文章"""
    # 这里需要读取飞书多维表格
    # 返回格式: [{"platform": "小红书", "title": "xxx", "content": "xxx", "image": "xxx"}, ...]
    pass

def publish_xiaohongshu(title, content, image_path):
    """发布到小红书"""
    sys.path.insert(0, os.path.dirname(__file__))
    from xiaohongshu_final import publish_article
    return publish_article(image_path, title, content)

def publish_weixin(title, content, image_path=None):
    """发布到微信公众号"""
    sys.path.insert(0, os.path.dirname(__file__))
    from weixin_publisher import publish_weixin as pw
    return pw(title, content, image_path)

def auto_publish_today():
    """自动发布今天的文章"""
    print("=" * 50)
    print("开始执行今日运营文章自动发布")
    print("=" * 50)
    
    # 1. 获取今天需要发布的文章
    # TODO: 从飞书表格读取
    articles = [
        {
            "platform": "小红书",
            "title": "行政小姐姐的救命神器！再也不用加班改座位了",
            "content": """姐妹们！

你们有没有经历过这种绝望：

老板："小王啊，明天宴会200人，座位排一下。"

然后Excel改到第8版的时候...

上周我发现了一个神器——智能排座系统！

✅ 3分钟搞定200人座位
✅ 拖拽式调整
✅ 参会人员自己查座位
✅ 临时换人，一键通知

昨天准时下班！老板还夸我效率高！

#行政 #职场干货 #加班神器""",
            "image": r"C:\Users\陈流恒\.openclawworkspace\小红书文章配图\article7_cover.png"
        }
    ]
    
    # 2. 逐个发布
    results = []
    for article in articles:
        platform = article["platform"]
        title = article["title"]
        content = article["content"]
        image = article.get("image")
        
        print(f"\n正在发布到 {platform}...")
        print(f"  标题: {title}")
        
        try:
            if platform == "小红书":
                success, msg = publish_xiaohongshu(title, content, image)
            elif platform == "微信公众号":
                success, msg = publish_weixin(title, content, image)
            else:
                success, msg = False, f"未知平台: {platform}"
            
            results.append({
                "platform": platform,
                "title": title,
                "success": success,
                "message": msg
            })
            
            print(f"  结果: {msg}")
            
        except Exception as e:
            print(f"  错误: {e}")
            results.append({
                "platform": platform,
                "title": title,
                "success": False,
                "message": str(e)
            })
    
    # 3. 汇总结果
    print("\n" + "=" * 50)
    print("发布完成!")
    print("=" * 50)
    
    success_count = sum(1 for r in results if r["success"])
    total_count = len(results)
    
    print(f"成功: {success_count}/{total_count}")
    
    for r in results:
        status = "✅" if r["success"] else "❌"
        print(f"{status} {r['platform']}: {r['title']}")
    
    return results

if __name__ == "__main__":
    auto_publish_today()
