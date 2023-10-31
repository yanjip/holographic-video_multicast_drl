# time: 2023/10/30 14:22
# author: YanJP

import numpy as np
seed=0
MHz=1e6
B=1*MHz
N_c=600  #子载波数量

K=5

N_tile=24
N_fov=12

bitrate=1e6  #in bps

Pmax=100  #w
average_power_loss = 1e-3
sigma = np.sqrt(average_power_loss / 2)
rayleigh_samples = sigma * np.random.randn(N_c,K) + 1j * sigma * np.random.randn(N_c,K)
h =abs(rayleigh_samples)

n0=1e-9  #噪声功率

L=5

#agent设置
state_dim=10
action_dim=10  #先设定每个用户可以选择最多10个子载波

def get_object(power,N_channel):
    return -power-0.01*N_channel




if __name__ == '__main__':

    pass