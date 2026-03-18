import sys
import os;

print("命令行参数如下：")
for i in sys.argv:
    print(i)

print('The PYTHON PATH is', sys.path)

print(os.getcwd())