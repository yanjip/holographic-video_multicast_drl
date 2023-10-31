# time: 2023/10/30 15:06
# author: YanJP

import  numpy as np
import para
import trans

def cal_r(p,h):
    return para.B*np.log2(1+p*(h**2)/para.n0)

def get_p_each(p,hk):
    D_m=0
    for h in hk:
        D_m+=cal_r(p,h)
    return D_m

def pre_process_action(hk, request_D):
    D_m=0
    a=0
    for h in hk:
        D_m+=cal_r(para.Pmax,h)
        a+=1
        if D_m>request_D:
            break
    return a
def cal_p(D,hk):

    delta=100
    pl=0
    ph=para.Pmax
    while True:
        pm=(pl+ph)/2
        D_m=get_p_each(pm,hk)
        if abs(D_m - D) <= delta:
            ans=pm
            break
        if D_m < D:
            pl=pm
        else:
            ph=pm
        # print("-----------now Power:{}---------".format(pm))
    print("-----------now Power:{}---------".format(ans))
    return ans

class env_():
    def __init__(self):
        self.action_dim=para.action_dim
        self.observation_space=(para.state_dim,)
        self.UserAll=trans.generate()
        self.reward=0

    def reset(self,):
        self.index=0
        self.pos=0
        self.res_p=[]
        self.now_h=para.h[0:para.action_dim]
        self.Nc_left=para.N_c
        # obs=np.concatenate((self.now_h,self.Nc_left),axis=0)
        obs=self.now_h
        return obs
        # state：[time_step, carrier_left, ]
        pass
    def step(self,action,):
        self.index+=1
        self.pos+=action
        self.Nc_left -= action
        request_D=para.bitrate*para.N_fov
        action_threshold=pre_process_action(self.now_h,request_D)  #最小的子载波数目，按照最大的发射功率算的
        if action>action_threshold:
            punish=action-action_threshold
        else: punish=0
        p=cal_p(request_D,self.now_h[0:action])
        self.res_p.append(p)
        reward=para.get_object(p,action)  #p越小越好，子载波数越小越好

        self.now_h=para.h[self.pos:self.pos+para.action_dim]
        obs=self.now_h

        if self.index==para.K:
            self.done=1.0
            obs=np.array([0.0]*para.K)
        return obs, reward, self.done, None



        pass