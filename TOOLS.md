# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## 小红书自动发布
- 技能位置：C:\Users\陈流恒\.openclaw\skills\xiaohongshu-publisher\
- 主脚本：scripts/xiaohongshu_final.py
- 使用：python xiaohongshu_final.py
- 依赖：selenium（已安装）

---

## 邮件配置
- 网易邮箱：chenliuheng@163.com
- SMTP：smtp.163.com
- 端口：25
- 脚本位置：C:\Users\陈流恒\.openclawworkspace\sendmail.ps1

---

Add whatever helps you do your job. This is your cheat sheet.
