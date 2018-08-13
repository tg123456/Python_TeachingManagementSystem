import os
import sys
#获取项目所在文件目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#将项目添加到sys.path中
sys.path.append(BASE_DIR)

from core import core

if __name__ == "__main__":
    core.main()



