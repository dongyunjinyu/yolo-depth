import cv2
import numpy as np


def a1(image):
    """灰度变换"""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def a2(image):
    """对比度变换"""
    return cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(image)


def a3(image):
    """直方图均衡"""
    return cv2.equalizeHist(image)


def a4(image):
    """锐化"""
    kernel = np.array([[0, 1, 0],
                       [1, -3, 1],
                       [0, 1, 0]])
    return cv2.filter2D(image, -1, kernel)


def a5(image):
    """中值滤波"""
    return cv2.medianBlur(image, 3)


def a6(image):
    """高斯滤波"""
    return cv2.GaussianBlur(image, (3, 3), 1)
