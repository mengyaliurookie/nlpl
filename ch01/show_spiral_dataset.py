import sys
sys.path.append('..') # 为了引入父目录的文件而进行的设定
from dataset import spiral
import matplotlib.pyplot as plt


x,t=spiral.load_data()
print('x',x.shape)
print('t',t.shape)