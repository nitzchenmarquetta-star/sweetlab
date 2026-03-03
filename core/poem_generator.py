#!/usr/bin/env python3
"""
甜蜜实验室 - 藏头诗/藏名诗生成器
"""

import random
from typing import List, Dict


class PoemGenerator:
    """藏头诗生成器"""

    def __init__(self):
        self.style_templates = {
            'romantic': {
                'name': '浪漫古风',
                'patterns': [
                    "{0}家有女初长成，",
                    "{1}颜如花笑倾城。",
                    "{2}心已许君可知，",
                    "{3}生不负相思情。"
                ],
                'ending': "愿得一心人，白首不相离。"
            },
            'cute': {
                'name': '可爱卖萌',
                'patterns': [
                    "{0}是天上小星星，",
                    "{1}闪一闪亮晶晶。",
                    "{2}见你就开心，",
                    "{3}欢喜欢你！"
                ],
                'ending': "超级喜欢你！🥰"
            },
            'funny': {
                'name': '搞笑搞怪',
                'patterns': [
                    "{0}吃货一个，",
                    "{1}顿不能少。",
                    "{2}肉都给你，",
                    "{3}想就管饱！"
                ],
                'ending': "爱吃是福！🍗"
            },
            'modern': {
                'name': '现代文艺',
                'patterns': [
                    "{0}光洒在你脸上，",
                    "{1}影刻在我心上。",
                    "{2}光流转岁月长，",
                    "{3}你在我身旁。"
                ],
                'ending': "有你在，就是最好的时光。"
            }
        }

    def generate_acrostic(self, name: str, style: str = 'romantic') -> Dict:
        """生成藏头诗

        Args:
            name: 名字（2-4字）
            style: 风格（romantic/cute/funny/modern）

        Returns:
            生成结果
        """
        if not name or len(name) < 2:
            return {
                'success': False,
                'error': '名字至少2个字哦～'
            }

        if len(name) > 4:
            name = name[:4]

        if style not in self.style_templates:
            style = 'romantic'

        template = self.style_templates[style]
        patterns = template['patterns']

        # 根据名字长度选择合适的 pattern
        if len(name) == 2:
            lines = self._generate_2char(name, template)
        elif len(name) == 3:
            lines = self._generate_3char(name, template)
        else:  # 4字
            lines = self._generate_4char(name, template)

        poem = '\n'.join(lines)
        ending = template.get('ending', '')

        return {
            'success': True,
            'name': name,
            'style': style,
            'style_name': template['name'],
            'poem': poem,
            'ending': ending,
            'full_text': f"{poem}\n\n{ending}" if ending else poem
        }

    def _generate_2char(self, name: str, template: Dict) -> List[str]:
        """生成2字藏头诗"""
        c1, c2 = name[0], name[1]

        templates_2char = [
            [
                f"{c1}眸如水映星光，",
                f"{c2}影婀娜入梦长。",
                "春风拂过花开处，",
                "正是人间好时光。"
            ],
            [
                f"{c1}山盟海誓在心间，",
                f"{c2}水长流情不断。",
                "愿得一心长相守，",
                "此生不负好姻缘。"
            ]
        ]

        return random.choice(templates_2char)

    def _generate_3char(self, name: str, template: Dict) -> List[str]:
        """生成3字藏头诗"""
        c1, c2, c3 = name[0], name[1], name[2]

        templates_3char = [
            [
                f"{c1}见倾心难忘怀，",
                f"{c2}见倾心更难捱。",
                f"{c3}生有幸遇见你，",
                "从此心上不分开。"
            ],
            [
                f"{c1}风拂面柳依依，",
                f"{c2}水潺潺情依依。",
                f"{c3}花盛开香满溢，",
                "良辰美景不负你。"
            ]
        ]

        return random.choice(templates_3char)

    def _generate_4char(self, name: str, template: Dict) -> List[str]:
        """生成4字藏头诗"""
        c1, c2, c3, c4 = name[0], name[1], name[2], name[3]

        templates_4char = [
            [
                f"{c1}见钟情难自禁，",
                f"{c2}见倾心更情深。",
                f"{c3}生有幸遇见你，",
                f"{c4}世相伴永不分。"
            ],
            [
                f"{c1}光暖暖照心田，",
                f"{c2}影翩翩在眼前。",
                f"{c3}花盛开香满院，",
                f"{c4}意绵绵到永远。"
            ],
            [
                f"{c1}风轻拂柳丝长，",
                f"{c2}水潺潺绕画廊。",
                f"{c3}月如钩照西窗，",
                f"{c4}思悠悠想情郎。"
            ]
        ]

        return random.choice(templates_4char)

    def list_styles(self) -> List[Dict]:
        """列出所有风格"""
        return [
            {'id': key, 'name': value['name']}
            for key, value in self.style_templates.items()
        ]
