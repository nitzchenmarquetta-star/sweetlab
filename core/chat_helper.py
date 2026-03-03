#!/usr/bin/env python3
"""
甜蜜实验室 - 聊天话术助手
"""

import random
from typing import Dict, List


class ChatHelper:
    """聊天话术助手"""

    def __init__(self):
        self.reply_templates = {
            'flirty': {
                'name': '撩人',
                'templates': [
                    "哈哈，你也太可爱了吧！",
                    "和你聊天好开心～",
                    "你怎么这么有趣！",
                    "有点想你了～",
                    "今天也很开心能和你聊天！"
                ]
            },
            'cute': {
                'name': '可爱',
                'templates': [
                    "歪歪歪，在吗在吗～",
                    "今天也超级喜欢你哦！",
                    "你最最最棒了！",
                    "给你小心心！❤️",
                    "呜呜，好想见你！"
                ]
            },
            'funny': {
                'name': '搞笑',
                'templates': [
                    "哈哈哈哈你是想笑死我继承我的蚂蚁花呗吗？",
                    "你的幽默感绝了！",
                    "你咋这么逗！",
                    "哈哈哈哈我不行了！",
                    "你是搞笑派来的逗比吗？"
                ]
            },
            'normal': {
                'name': '正常',
                'templates': [
                    "哈哈哈",
                    "好的好的",
                    "嗯嗯",
                    "这样啊",
                    "好有意思！"
                ]
            }
        }

        self.topic_starters = {
            'first_chat': {
                'name': '初次聊天',
                'templates': [
                    "在干嘛呢？",
                    "今天过得怎么样？",
                    "忙吗？",
                    "有什么好玩的事吗？",
                    "哈喽哈喽～"
                ]
            },
            'ambiguous': {
                'name': '暧昧期',
                'templates': [
                    "在想你～",
                    "今天有没有想我？",
                    "有空吗？想约你～",
                    "和你聊天很开心",
                    "你在干嘛呢？"
                ]
            },
            'couple': {
                'name': '情侣日常',
                'templates': [
                    "想你了宝贝",
                    "今天也爱你哦～",
                    "在干嘛呢？",
                    "有空吗？",
                    "想你想你想你！"
                ]
            }
        }

        self.earthy_flirt = {
            'name': '土味情话',
            'templates': [
                "你知道你和星星的区别吗？星星在天上，你在我心里。",
                "我最近学了一门新技能，叫'喜欢你'。",
                "你累不累啊？你都在我心里跑了一整天了。",
                "我发现我最近有点怕你，因为我怕老婆。",
                "你是哪里人？不，你是我的心上人。",
                "我的手被划了一道口子，你也划一道，这样我们就是两口子了。",
                "猜猜我的心在哪边？左边？错了，在你那边。",
                "你有打火机吗？没有？那你是怎么点燃我的心的？",
                "你是我的今日限定。",
                "我想买一块地。什么地？你的死心塌地。"
            ]
        }

    def generate_reply(self, message: str, style: str = 'normal') -> Dict:
        """生成回复

        Args:
            message: 对方说的话
            style: 风格（flirty/cute/funny/normal）

        Returns:
            生成结果
        """
        if style not in self.reply_templates:
            style = 'normal'

        template = self.reply_templates[style]
        templates = template['templates']

        # 随机选择 3 个不同的
        if len(templates) >= 3:
            selected = random.sample(templates, 3)
        else:
            selected = templates

        return {
            'success': True,
            'message': message,
            'style': style,
            'style_name': template['name'],
            'replies': selected
        }

    def generate_topic_starter(self, scene: str = 'first_chat') -> Dict:
        """生成话题开场白

        Args:
            scene: 场景（first_chat/ambiguous/couple）

        Returns:
            生成结果
        """
        if scene not in self.topic_starters:
            scene = 'first_chat'

        template = self.topic_starters[scene]
        templates = template['templates']

        # 随机选择 3 个
        if len(templates) >= 3:
            selected = random.sample(templates, 3)
        else:
            selected = templates

        return {
            'success': True,
            'scene': scene,
            'scene_name': template['name'],
            'starters': selected
        }

    def generate_earthy_flirt(self, count: int = 3) -> Dict:
        """生成土味情话

        Args:
            count: 生成数量

        Returns:
            生成结果
        """
        templates = self.earthy_flirt['templates']

        if count > len(templates):
            count = len(templates)

        selected = random.sample(templates, count)

        return {
            'success': True,
            'count': count,
            'flirts': selected
        }

    def list_styles(self) -> List[Dict]:
        """列出所有回复风格"""
        return [
            {'id': key, 'name': value['name']}
            for key, value in self.reply_templates.items()
        ]

    def list_scenes(self) -> List[Dict]:
        """列出所有场景"""
        return [
            {'id': key, 'name': value['name']}
            for key, value in self.topic_starters.items()
        ]
