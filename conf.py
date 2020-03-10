# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Prism",
    "type": "local",
    "path": "../Templates/Prism"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "AyagawaSeirin/diary@gh-pages"
}

# 站点设置
site_name = "Seirin's Diary"
site_logo = "${static_prefix}logo.jpg"
site_build_date = "2020-03-10T02:26+08:00"
author = "AyagawaSeirin"
email = "AyagawaSeirin@outlook.com"
author_homepage = "https://moegirl.life"
description = "皮皮凛的个人日记站点"
key_words = ['皮皮凛', '个人日记', 'AyagawaSeirin', '绫川星凛']
language = 'zh-CN'
external_links = [
    {
        "name": "皮皮凛の小窝",
        "url": "https://qwq.best",
        "brief": "咱的博客主站"
    },
    {
        "name": "主页",
        "url": "https://seir.in",
        "brief": ""
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/AyagawaSeirin",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/AyagawaSeirin",
        "icon": "gi gi-github"
    },
    {
        "name": "Telegram",
        "url": "https://t.me/AyagawaSeirin",
        "icon": "gi gi-telegram"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
