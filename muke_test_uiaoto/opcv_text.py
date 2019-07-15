#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/3/26


# CNN + dlib + face detector
# CNN模型的人脸检测准确率比基于HOG的方法好，但是对计算能力要求大
# 预训练模型： mmod_human_face_detector.dat
import cv2
import dlib


if __name__ == "__main__":
    cnn_face_detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")

    img_path = "./faces/2008_007676.jpg"
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    # opencv读取图片是BGR格式，需要将其转换成RGB格式
    b, g, r = cv2.split(img)
    img2 = cv2.merge([r, g, b])  # 融合三个颜色通道生成新图片

    # 使用cnn_face_detector进行人脸检测，并打印人脸
    dets = cnn_face_detector(img, 1)
    print("Number of faces detected: {}".format(len(dets)))
    # 便利索引
    for index, face in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(
            index, face.rect.left(), face.rect.top(), face.rect.right(), face.rect.bottom(), face.confidence))
        # 在图片中标注人脸并显示
        left = face.rect.left()
        top = face.rect.top()
        right = face.rect.right()
        bottom = face.rect.bottom()
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)
        cv2.namedWindow("faces", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("faces", img)
    k = cv2.waitKey(0)
    cv2.destroyAllWindows()

