# 检查环境.py —— 一键体检，把结果打印到屏幕上
# 用法：在终端里输入  python 检查环境.py

import sys      # sys 是 Python 自带的工具箱，这里用来查版本和路径
import shutil   # shutil 也是自带的，用来找 git / code 这类外部程序在哪

print("=" * 46)
print("Python 版本：", sys.version)
print("Python 路径：", sys.executable)
print("=" * 46)

for tool in ["git", "code"]:
    path = shutil.which(tool)
    if path:
        print(f"{tool:<6} 已就绪 -> {path}")
    else:
        print(f"{tool:<6} 没找到（多半是 PATH 没配好，把这段发我）")

print("=" * 46)
print("第三方库（上到对应周次才需要，现在没有是正常的）：")
for lib in ["numpy", "cv2", "matplotlib", "torch"]:
    try:
        __import__(lib)
        print(f"  {lib:<12} 已装")
    except ImportError:
        print(f"  {lib:<12} 未装")
print("=" * 46)
