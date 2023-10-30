# time: 2023/10/30 14:22
# author: YanJP

import numpy as np
MHz=1e6
B=1*MHz
N_c=600  #子载波数量

K=5

N_tile=24
N_fov=12

bitrate=1e6  #in bps

P=100  #w
H = np.sqrt(np.random.exponential(1e-6, size=(N_c,K)))
n0=1e-9  #噪声功率

L=5

#agent设置
state_dim=2
action_dim=10  #先设定每个用户可以选择最多10个子载波


def cal_r(b,snr):
    return b*np.log2(1+snr)