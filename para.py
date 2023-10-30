# time: 2023/10/30 14:22
# author: YanJP

import numpy as np
MHz=1e6
B=1*MHz
N=600  #子载波数量

K=5

N_tile=24
N_fov=12

bitrate=1e6  #in bps

P=100  #w
H = np.sqrt(np.random.exponential(1e-6, size=(N,K)))
n0=1e-9  #噪声功率

L=5

def cal_r(b,snr):
    return b*np.log2(1+snr)