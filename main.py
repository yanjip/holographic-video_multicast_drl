'''
@Author  ：Yan JP
@Created on Date：2023/10/25 23:09 
'''
import para
import numpy as np
class user():
    def __init__(self,id,fov_id,):
        self.id=id
        self.fov_id=fov_id

    pass

class user_all():
    def __init__(self):
        self.users=[user]*para.K
        self.fovs=np.random.randint(0,10,size=para.K)
        for u in range(para.K):
            self.users[u]=user(u,self.fovs[u])

    def group(self,):

        pass
if __name__ == '__main__':
    U=user_all()
    print('heoo')
