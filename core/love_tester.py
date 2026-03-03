#!/usr/bin/env python3
"""
甜蜜实验室 - 爱情/友情测试器
"""

import random
import hashlib
from typing import Dict, List


class LoveTester:
    """爱情/友情测试器"""

    def __init__(self):
        self.result_templates = {
            'high': [
                "天生一对！契合度 {score}%！",
                "太配了！契合度 {score}%！",
                "绝配！契合度 {score}%！",
                "命中注定！契合度 {score}%！"
            ],
            'medium': [
                "很合适！契合度 {score}%！",
                "不错哦！契合度 {score}%！",
                "有缘分！契合度 {score}%！",
                "很配！契合度 {score}%！"
            ],
            'low': [
                "需要多磨合～ 契合度 {score}%",
                "加油哦！契合度 {score}%",
                "慢慢来～ 契合度 {score}%",
                "还有提升空间！契合度 {score}%"
            ]
        }

        self.analysis_templates = {
            'romantic': [
                "你们的相遇，就像命中注定～",
                "TA 的一举一动，都能牵动你的心～",
                "和 TA 在一起，总是很开心～",
                "你们在一起，总是有说不完的话～"
            ],
            'friendship': [
                "你们是最好的朋友！",
                "和 TA 在一起，总是很放松～",
                "你们是彼此的最佳损友！",
                "你们的友谊，让人羡慕～"
            ]
        }

    def calculate_score(self, name1: str, name2: str, 
                       birthday1: str = '', birthday2: str = '') -> int:
        """计算契合度分数

        Args:
            name1: 第一个人的名字
            name2: 第二个人的名字
            birthday1: 第一个人生日（可选）
            birthday2: 第二个人生日（可选）

        Returns:
            契合度分数 (0-100)
        """
        # 用名字生成一个稳定的随机种子
        combined = (name1 + name2 + birthday1 + birthday2).encode('utf-8')
        seed = int(hashlib.md5(combined).hexdigest(), 16) % 1000000
        random.seed(seed)

        # 生成 40-99 的分数（不会太低，太伤人了 😂）
        score = random.randint(40, 99)

        return score

    def test(self, name1: str, name2: str,
             birthday1: str = '', birthday2: str = '',
             relationship_type: str = 'romantic') -> Dict:
        """测试契合度

        Args:
            name1: 第一个人的名字
            name2: 第二个人的名字
            birthday1: 第一个人生日（可选）
            birthday2: 第二个人生日（可选）
            relationship_type: 关系类型（romantic/friendship）

        Returns:
            测试结果
        """
        if not name1 or not name2:
            return {
                'success': False,
                'error': '请输入两个人的名字哦～'
            }

        # 计算分数
        score = self.calculate_score(name1, name2, birthday1, birthday2)

        # 根据分数选择模板
        if score >= 80:
            template_type = 'high'
        elif score >= 60:
            template_type = 'medium'
        else:
            template_type = 'low'

        # 选择结果文案
        result_template = random.choice(self.result_templates[template_type])
        result_text = result_template.format(score=score)

        # 选择分析文案
        if relationship_type not in self.analysis_templates:
            relationship_type = 'romantic'

        analysis = random.choice(self.analysis_templates[relationship_type])

        # 生成分享文案
        share_text = f"我和{name2}的契合度是 {score}%！你也来试试吧～"

        return {
            'success': True,
            'name1': name1,
            'name2': name2,
            'birthday1': birthday1,
            'birthday2': birthday2,
            'relationship_type': relationship_type,
            'score': score,
            'result': result_text,
            'analysis': analysis,
            'share_text': share_text
        }

    def test_batch(self, name1: str, names: List[str],
                   relationship_type: str = 'romantic') -> Dict:
        """批量测试

        Args:
            name1: 第一个人的名字
            names: 要测试的名字列表
            relationship_type: 关系类型

        Returns:
            批量测试结果
        """
        results = []
        for name2 in names:
            result = self.test(name1, name2, '', '', relationship_type)
            if result.get('success'):
                results.append({
                    'name': name2,
                    'score': result.get('score'),
                    'result': result.get('result')
                })

        # 按分数排序
        results.sort(key=lambda x: x['score'], reverse=True)

        return {
            'success': True,
            'name1': name1,
            'results': results
        }
