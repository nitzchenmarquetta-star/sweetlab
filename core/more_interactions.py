#!/usr/bin/env python3
"""
甜蜜实验室 - 更多互动功能
"""

import random
from typing import Dict, List


class MoreInteractions:
    """更多互动功能"""

    def __init__(self):
        self.name_games = {
            'couple': {
                'name': '💕 情侣名生成',
                'templates': [
                    "{name1}的{name2}",
                    "{name2}的{name1}",
                    "{name1}与{name2}",
                    "{name1}&{name2}",
                    "唯有{name1}与{name2}",
                    "{name1}心里的{name2}"
                ]
            },
            'nickname': {
                'name': '😜 外号生成',
                'templates': [
                    "小{name}",
                    "{name}宝",
                    "阿{name}",
                    "{name}仔",
                    "大{name}",
                    "{name}酱"
                ]
            }
        }

        self.truth_or_dare = {
            'truth': [
                "你最想改变自己的一件事是什么？",
                "如果你有超能力，你希望是什么？",
                "你做过最疯狂的事是什么？",
                "你理想中的约会是什么样的？",
                "你第一次喜欢一个人是什么时候？",
                "如果可以回到过去，你想回到哪一刻？"
            ],
            'dare': [
                "给对方唱首歌",
                "对对方说一句土味情话",
                "模仿对方的口头禅",
                "给对方发条撒娇的消息",
                "和对方对视10秒",
                "给对方讲个笑话"
            ]
        }

        self.lucky_draw_items = {
            'items': [
                "💕 今日运势：超好运！",
                "🎁 今日幸运物：糖果",
                "💖 今日幸运色：粉色",
                "✨ 今日箴言：勇敢一点！",
                "🌟 今日提示：会有好事发生！",
                "🍀 今日运势：好运连连！"
            ]
        }

    def generate_couple_name(self, name1: str, name2: str) -> Dict:
        """生成情侣名

        Args:
            name1: 第一个人的名字
            name2: 第二个人的名字

        Returns:
            生成结果
        """
        if not name1 or not name2:
            return {
                'success': False,
                'error': '请输入两个人的名字哦～'
            }

        template = random.choice(self.name_games['couple']['templates'])
        couple_name = template.format(name1=name1, name2=name2)

        return {
            'success': True,
            'name1': name1,
            'name2': name2,
            'couple_name': couple_name
        }

    def generate_nickname(self, name: str) -> Dict:
        """生成外号

        Args:
            name: 名字

        Returns:
            生成结果
        """
        if not name:
            return {
                'success': False,
                'error': '请输入名字哦～'
            }

        # 取名字的最后一个字
        if len(name) >= 1:
            char = name[-1]
        else:
            char = name

        template = random.choice(self.name_games['nickname']['templates'])
        nickname = template.format(name=char)

        return {
            'success': True,
            'name': name,
            'nickname': nickname
        }

    def truth_or_dare(self, choice: str = 'random') -> Dict:
        """真心话大冒险

        Args:
            choice: 选择（truth/dare/random）

        Returns:
            结果
        """
        if choice == 'random':
            choice = random.choice(['truth', 'dare'])

        if choice == 'truth':
            content = random.choice(self.truth_or_dare['truth'])
            type_name = '真心话'
        else:
            content = random.choice(self.truth_or_dare['dare'])
            type_name = '大冒险'

        return {
            'success': True,
            'type': choice,
            'type_name': type_name,
            'content': content
        }

    def lucky_draw(self) -> Dict:
        """每日抽签

        Returns:
            抽签结果
        """
        item = random.choice(self.lucky_draw_items['items'])

        return {
            'success': True,
            'item': item
        }

    def list_games(self) -> List[Dict]:
        """列出所有互动游戏"""
        return [
            {
                'id': 'couple_name',
                'name': '💕 情侣名生成'
            },
            {
                'id': 'nickname',
                'name': '😜 外号生成'
            },
            {
                'id': 'truth_or_dare',
                'name': '🎮 真心话大冒险'
            },
            {
                'id': 'lucky_draw',
                'name': '🍀 每日抽签'
            }
        ]
