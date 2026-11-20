# 看图片.py —— 先搞清楚"图片是什么"
# 用法：在此文件夹下运行  python 看图片.py

from PIL import Image
import numpy as np

# 1. 打开图片，变成 numpy 数组
img = np.array(Image.open("示例图片.png"))

print("=" * 40)
print("形状 shape :", img.shape)      # (高, 宽, 3)
print("类型 dtype :", img.dtype)      # uint8
print("最小值     :", img.min())      # 0
print("最大值     :", img.max())      # 255
print("=" * 40)

# 2. 取几个具体像素看看
print("左上角 像素 [0,0]      :", img[0, 0])
print("第 100 行第 50 列 像素 :", img[100, 50])
print("中间 像素 [120,160]    :", img[120, 160])
print("=" * 40)

# 3. 单独看三个通道
print("R 通道形状:", img[:, :, 0].shape)
print("G 通道形状:", img[:, :, 1].shape)
print("B 通道形状:", img[:, :, 2].shape)
print("=" * 40)

# 4. 显示图片（会弹出看图窗口）
Image.open("示例图片.png").show()

print("看完关掉图片窗口就行。接下来去做 练习-图像处理.py 里的三个任务。")
