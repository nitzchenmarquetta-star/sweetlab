#!/usr/bin/env python3
"""
甜蜜实验室 - 情话/表白文案生成器
"""

import random
from typing import List, Dict


class LoveGenerator:
    """情话/表白文案生成器"""

    def __init__(self):
        self.style_templates = {
            'romantic': {
                'name': '温柔浪漫',
                'templates': [
                    "遇见你，是我这辈子最幸运的事。",
                    "想和你一起，看遍世间所有的风景。",
                    "你笑起来，整个世界都亮了。",
                    "春风十里，不如你。",
                    "愿得一心人，白首不相离。",
                    "有你在身边，就是最好的时光。",
                    "每天最开心的事，就是见到你。",
                    "想把全世界最好的，都给你。"
                ]
            },
            'funny': {
                'name': '搞笑搞怪',
                'templates': [
                    "你知道你和星星的区别吗？星星在天上，你在我心里。",
                    "我最近学了一门新技能，叫'喜欢你'。",
                    "你累不累啊？你都在我心里跑了一整天了。",
                    "我发现我最近有点怕你，因为我怕老婆。",
                    "你是哪里人？不，你是我的心上人。",
                    "我的手被划了一道口子，你也划一道，这样我们就是两口子了。",
                    "猜猜我的心在哪边？左边？错了，在你那边。",
                    "你有打火机吗？没有？那你是怎么点燃我的心的？"
                ]
            },
            'cute': {
                'name': '可爱卖萌',
                'templates': [
                    "歪歪歪，有人在吗？我超级喜欢你！🥰",
                    "今天也超级喜欢你哦～ 💕",
                    "想做你的小朋友，被你宠坏～",
                    "你是最最最好的！✨",
                    "今天也想见到你！🥺",
                    "给你小心心！❤️❤️❤️",
                    "你最可爱了，不接受反驳！",
                    "超级超级喜欢你！比心！💕"
                ]
            },
            'direct': {
                'name': '直球表白',
                'templates': [
                    "我喜欢你，做我对象吧。",
                    "别想了，我就是喜欢你。",
                    "没有理由，就是喜欢你。",
                    "要不要在一起？",
                    "我想和你在一起。",
                    "做我女朋友/男朋友吧。",
                    "我对你有意思，你看着办。",
                    "没什么好说的，我就是喜欢你。"
                ]
            },
            'literary': {
                'name': '文艺小清新',
                'templates': [
                    "于千万人之中遇见你，没有早一步，也没有晚一步。",
                    "愿岁月可回首，且以深情共白头。",
                    "斯人若彩虹，遇上方知有。",
                    "春水初生，春林初盛，春风十里，不如你。",
                    "时光静好，与君语；细水流年，与君同；繁华落尽，与君老。",
                    "愿有岁月可回首，且以深情共白头。",
                    "你是我的半截的诗，不许别人更改一个字。",
                    "草在结它的种子，风在摇它的叶子，我们站着，不说话，就十分美好。"
                ]
            }
        }

        self.scene_templates = {
            'first_meet': {
                'name': '初次见面',
                'templates': [
                    "还记得第一次见到你的时候，阳光洒在你脸上，我就知道，这就是我要找的人。",
                    "人生若只如初见，那该多好。不过，现在也很好，因为有你。",
                    "第一次见到你，我就知道，这个人，我想和她/他有故事。"
                ]
            },
            'anniversary': {
                'name': '纪念日',
                'templates': [
                    "一周年快乐！这一年，因为有你，每一天都很特别。",
                    "不知不觉，我们已经在一起一年了。谢谢你，陪我走过这一年。",
                    "纪念日快乐！未来的每一年，都想和你一起过。"
                ]
            },
            'confession': {
                'name': '表白',
                'templates': [
                    "其实，我喜欢你很久了。今天，终于鼓起勇气告诉你。",
                    "我不想再做朋友了，我想和你在一起。",
                    "不知道从什么时候开始，我满脑子都是你。"
                ]
            },
            'goodnight': {
                'name': '晚安',
                'templates': [
                    "晚安，梦里见。",
                    "早点睡，明天还要想你呢。",
                    "晚安，希望梦里有你。"
                ]
            }
        }

    def generate(self, style: str = 'romantic', 
                 name: str = '', 
                 scene: str = '') -> Dict:
        """生成情话/表白文案

        Args:
            style: 风格（romantic/funny/cute/direct/literary）
            name: 对方名字（可选）
            scene: 场景（first_meet/anniversary/confession/goodnight）

        Returns:
            生成结果
        """
        if style not in self.style_templates:
            style = 'romantic'

        template = self.style_templates[style]
        templates = template['templates']

        # 如果有场景，优先用场景模板
        if scene and scene in self.scene_templates:
            scene_template = self.scene_templates[scene]
            templates = scene_template['templates'] + templates

        # 随机选择一个模板
        text = random.choice(templates)

        # 如果有名字，把"你"替换成名字
        if name:
            text = text.replace("你", name)

        return {
            'success': True,
            'style': style,
            'style_name': template['name'],
            'scene': scene,
            'scene_name': self.scene_templates.get(scene, {}).get('name', ''),
            'name': name,
            'text': text
        }

    def generate_batch(self, style: str = 'romantic', count: int = 3) -> Dict:
        """批量生成

        Args:
            style: 风格
            count: 生成数量

        Returns:
            生成结果
        """
        if style not in self.style_templates:
            style = 'romantic'

        template = self.style_templates[style]
        templates = template['templates']

        # 随机选择 count 个不重复的
        if count > len(templates):
            count = len(templates)

        selected = random.sample(templates, count)

        return {
            'success': True,
            'style': style,
            'style_name': template['name'],
            'count': count,
            'texts': selected
        }

    def list_styles(self) -> List[Dict]:
        """列出所有风格"""
        return [
            {'id': key, 'name': value['name']}
            for key, value in self.style_templates.items()
        ]

    def list_scenes(self) -> List[Dict]:
        """列出所有场景"""
        return [
            {'id': key, 'name': value['name']}
            for key, value in self.scene_templates.items()
        ]
