#!/usr/bin/env python3
"""
甜蜜实验室 - 头像风格化模块
"""

import os
import sys
from pathlib import Path
from typing import Dict, List
import random

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))


class AvatarStyler:
    """头像风格化器"""

    def __init__(self):
        self.styles = {
            'candy': {
                'name': '🍬 糖果色',
                'description': '甜蜜的马卡龙色系',
                'filters': ['brightness', 'pastel', 'warm']
            },
            'anime': {
                'name': '🎮 二次元',
                'description': '日系动漫风格',
                'filters': ['cartoon', 'brightness', 'contrast']
            },
            'vintage': {
                'name': '📷 复古风',
                'description': '怀旧复古滤镜',
                'filters': ['sepia', 'vignette', 'grain']
            },
            'ins': {
                'name': '✨ ins 风',
                'description': 'ins 网红滤镜',
                'filters': ['brightness', 'contrast', 'cool']
            },
            'sketch': {
                'name': '✏️ 素描风',
                'description': '手绘素描效果',
                'filters': ['sketch', 'contrast']
            }
        }

    def list_styles(self) -> List[Dict]:
        """列出所有风格"""
        return [
            {
                'id': key,
                'name': value['name'],
                'description': value['description']
            }
            for key, value in self.styles.items()
        ]

    def apply_style(self, image_path: str, style: str = 'candy',
                   output_path: str = None) -> Dict:
        """应用风格到头像

        注意：这是一个演示版本，用 OpenCV 实现简单的滤镜效果
        真实生产环境可以接入更专业的 AI 模型

        Args:
            image_path: 输入图片路径
            style: 风格（candy/anime/vintage/ins/sketch）
            output_path: 输出图片路径（可选）

        Returns:
            处理结果
        """
        try:
            import cv2
            import numpy as np
        except ImportError:
            return {
                'success': False,
                'error': '需要安装 OpenCV: pip install opencv-python numpy'
            }

        # 读取图片
        img = cv2.imread(image_path)
        if img is None:
            return {
                'success': False,
                'error': f'无法读取图片: {image_path}'
            }

        if style not in self.styles:
            style = 'candy'

        style_info = self.styles[style]

        # 应用滤镜
        result = img.copy()

        if style == 'candy':
            result = self._filter_candy(result)
        elif style == 'anime':
            result = self._filter_anime(result)
        elif style == 'vintage':
            result = self._filter_vintage(result)
        elif style == 'ins':
            result = self._filter_ins(result)
        elif style == 'sketch':
            result = self._filter_sketch(result)

        # 确定输出路径
        if output_path is None:
            base, ext = os.path.splitext(image_path)
            output_path = f"{base}_{style}{ext}"

        # 确保输出目录存在
        from utils.helpers import ensure_dir
        ensure_dir(os.path.dirname(output_path))

        # 保存结果
        cv2.imwrite(output_path, result)

        return {
            'success': True,
            'input_path': image_path,
            'output_path': output_path,
            'style': style,
            'style_name': style_info['name']
        }

    def _filter_candy(self, img):
        """糖果色滤镜"""
        # 提高亮度，增加饱和度，暖色调
        img_float = img.astype(float)

        # 提高亮度
        img_float = img_float * 1.1

        # 增加饱和度
        img_hsv = cv2.cvtColor(img_float.astype(np.uint8), cv2.COLOR_BGR2HSV)
        img_hsv[:, :, 1] = img_hsv[:, :, 1] * 1.3
        img_result = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

        # 限制范围
        img_result = np.clip(img_result, 0, 255).astype(np.uint8)

        return img_result

    def _filter_anime(self, img):
        """二次元滤镜"""
        # 边缘增强 + 色彩量化
        img_float = img.astype(float)

        # 卡通化
        num_colors = 16
        img_float = img_float // (256 // num_colors) * (256 // num_colors)

        # 边缘检测
        gray = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_BGR2GRAY)
        edges = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
        edges = cv2.threshold(edges, 30, 255, cv2.THRESH_BINARY)[1]

        # 合并
        img_result = img_float.astype(np.uint8)
        img_result[edges > 0] = img_result[edges > 0] * 0.7

        return img_result

    def _filter_vintage(self, img):
        """复古滤镜"""
        # 棕褐色调 + 暗角 + 颗粒
        img_float = img.astype(float)

        # 棕褐色调
        img_sepia = cv2.transform(img_float.astype(np.uint8), np.array([
            [0.272, 0.534, 0.131],
            [0.349, 0.686, 0.168],
            [0.393, 0.769, 0.189]
        ]))

        # 暗角
        rows, cols = img.shape[:2]
        X_result = cv2.getGaussianKernel(cols, cols / 2.5)
        Y_result = cv2.getGaussianKernel(rows, rows / 2.5)
        mask = Y_result * X_result.T
        mask = mask / mask.max()

        img_result = img_sepia.astype(float)
        for i in range(3):
            img_result[:, :, i] = img_result[:, :, i] * mask

        return img_result.astype(np.uint8)

    def _filter_ins(self, img):
        """ins 风滤镜"""
        # 提高对比度，冷色调，稍微过曝
        img_float = img.astype(float)

        # 提高对比度
        img_float = (img_float - 128) * 1.2 + 128

        # 冷色调
        img_float[:, :, 0] = img_float[:, :, 0] * 1.1
        img_float[:, :, 2] = img_float[:, :, 2] * 0.9

        # 限制范围
        img_result = np.clip(img_float, 0, 255).astype(np.uint8)

        return img_result

    def _filter_sketch(self, img):
        """素描滤镜"""
        # 转灰度 + 边缘检测
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        inv_gray = 255 - gray

        # 高斯模糊
        blurred = cv2.GaussianBlur(inv_gray, (21, 21), 0)

        # 颜色减淡混合
        def dodge(front, back):
            result = back * 255.0 / (255.0 - front)
            result[result > 255] = 255
            result[front == 255] = 255
            return result.astype(np.uint8)

        img_result = dodge(blurred, gray)

        # 转回彩色（保留素描效果）
        img_result = cv2.cvtColor(img_result, cv2.COLOR_GRAY2BGR)

        return img_result
