import torch
from torch import nn,optim
import matplotlib.pyplot as plt

import os
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'#解决OMP问题

xs=torch.unsqueeze(torch.arange(-20,21),dim=1)/20
ys=0.01*xs+0.01
class line1(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers=nn.Sequential(
            nn.Linear(1,20),
            nn.Linear(20,64),
            nn.Linear(64,20),
            nn.Linear(20,1)
        )
    def forward(self,xs):
        return self.layers(xs)
class line2(nn.Module):
    def __init__(self):
        super().__init__()
        self.w1=nn.Parameter(torch.randn(1,20))
        self.b1=nn.Parameter(torch.randn(20))
        self.w2 = nn.Parameter(torch.randn(20, 64))
        self.b2 = nn.Parameter(torch.randn(64))
        self.w3 = nn.Parameter(torch.randn(64, 20))
        self.b3 = nn.Parameter(torch.randn(20))
        self.w4 = nn.Parameter(torch.randn(20, 1))
        self.b4 = nn.Parameter(torch.randn(1))
    def forward(self,xs):
        f1=torch.matmul(xs,self.w1)+self.b1
        f2=torch.matmul(f1,self.w2)+self.b2
        f3=torch.matmul(f2,self.w3)+self.b3
        f4=torch.matmul(f3,self.w4)+self.b4
        return f4
if __name__ == '__main__':
    net1=line1()
    net2=line2()
    opt1=optim.Adam(net1.parameters())
    opt2 = optim.Adam(net2.parameters())
    loss_func=nn.MSELoss()
    plt.ion()
    while 1:
        zs1=net1.forward(xs)
        loss1=loss_func(zs1,ys)

        zs2 = net2.forward(xs)
        loss2 = loss_func(zs2, ys)

        opt1.zero_grad()
        loss1.backward()
        opt1.step()

        opt2.zero_grad()
        loss2.backward()
        opt2.step()

        plt.subplot(1,2,1)
        plt.cla()
        plt.plot(xs, ys, 'r.')
        plt.title(f"loss1:{loss1:.4f}")
        plt.plot(xs,ys,'.')
        plt.plot(xs,zs1.detach())
        plt.pause(0.001)

        plt.subplot(1,2,2)
        plt.cla()
        plt.plot(xs, ys, 'r.')
        plt.title(f"loss2:{loss2:.4f}")
        plt.plot(xs, ys, '.')
        plt.plot(xs, zs2.detach())
        plt.pause(0.001)

    plt.ioff()
    plt.show()
