# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : cv_test.py
# Time       ：2023/4/25 14:49
# Author     ：Soozi
# version    ：python 3.8
# Description： 页面中有多个相同的原始匹配多个元素返回位置
"""

import cv2
import numpy as np
# =================================
# 6种模板匹配方法，一种匹配不上可以换着用
# cv2.TM_CCOEFF
# cv2.TM_CCOEFF_NORMED
# cv2.TM_CCORR
# cv2.TM_CCORR_NORMED
# cv2.TM_SQDIFF
# cv2.TM_SQDIFF_NORMED
# =================================

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

im_rgb = cv2.imread(r'E:\test_material\full.png')

cv2.imshow('im', im_rgb)
im_gray = cv2.cvtColor(im_rgb, cv2.COLOR_BGR2GRAY)  # 颜色空间转换

template = cv2.imread(r'E:\test_material\audio.png', 0)
w, h = template.shape[::-1]  # 取宽和高

res = cv2.matchTemplate(im_gray, template, cv2.TM_CCOEFF_NORMED)  # 模板匹配
threshold = 0.9
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(im_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

cv2.imshow('res.png', im_rgb)
cv2.waitKey(0)
