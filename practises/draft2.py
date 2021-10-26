import torch
from torch import nn, optim
import matplotlib.pyplot as plt
import os
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'
xs = torch.unsqueeze(torch.arange(-50, 51), dim=1) / 50
ys = xs.pow(2) * torch.rand(101, 1).uniform_(0, 3)

class line(nn.Module):
    def __init__(self):
        super().__init__()
        #构造神经网络层有序的容器
        self.layer = nn.Sequential(
            nn.Linear(1, 20),#第一层
            nn.ReLU(),#激活函数
            nn.Linear(20, 64),
            nn.ReLU(),
            nn.Linear(64, 20),
            nn.Sigmoid(),
            nn.Linear(20, 1)
        )

    def forward(self, x):
        return self.layer(x)

if __name__ == '__main__':
    net = line()
    opt = optim.Adam(net.parameters())
    loss_func = nn.MSELoss()
    plt.ion()
    while 1:
        zs = net.forward(xs)
        loss = loss_func(zs, ys)

        opt.zero_grad()
        loss.backward()
        opt.step()

        plt.cla()
        plt.plot(xs, ys, ".")
        plt.plot(xs, zs.detach())
        plt.title(f"loss:{loss:.4f}")
        plt.pause(0.0001)
    plt.ioff()
    plt.show()
