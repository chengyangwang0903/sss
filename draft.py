import torch
from torch import nn,optim
import random
import matplotlib.pyplot as plt
xs=torch.unsqueeze(torch.arange(-20,21),dim=1)/20#矩阵为(40,1),除以20是为了归化到(-1,1)
ys=[i.pow(3)*random.randint(1,6) for i in xs]
ys=torch.stack(ys)#列表转为tensor
class line(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.l1=nn.Linear(1,20)#第一层网络层
        self.s1=nn.ReLU()#激活函数

        self.l2=nn.Linear(20,64)
        self.s2=nn.ReLU()

        self.l3=nn.Linear(64,128)
        self.s3=nn.ReLU()

        self.l4=nn.Linear(128,64)
        self.s4=nn.ReLU()

        self.l5=nn.Linear(64,1)#最后一层网络层不需要relu激活函数,因为输出结果有正有负,而relu值域>=0
    def forward(self,x):
        fc1=self.l1(x)
        fc1=self.s1(fc1)

        fc2=self.l2(fc1)
        fc2=self.s1(fc2)

        fc3=self.l3(fc2)
        fc3=self.s1(fc3)

        fc4=self.l4(fc3)
        fc4=self.s1(fc4)

        fc5=self.l5(fc4)
        return fc5
if __name__=="__main__":
        net=line()
        opt=optim.Adam(net.parameters())
        loss_func=nn.MSELoss()
        plt.ion()
        while 1:
            z=net.forward(xs)
            loss=loss_func(z,ys)

            opt.zero_grad()
            loss.backward()
            opt.step()

            plt.cla()
            plt.plot(xs,ys,".")
            plt.plot(xs,z.detach())
            plt.title(f"loss:{loss.item()}")
            plt.pause(0.001)

        plt.ioff()
        plt.show()

