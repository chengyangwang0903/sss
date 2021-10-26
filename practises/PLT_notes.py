import matplotlib.pyplot as plt
import numpy as np
# from PIL import Image
# img=Image.open("sheep.png")
# plt.imshow(img)
# plt.axis(False)#隐藏坐标轴
# plt.show()
'''
a=[]
b=[]
#开启绘画
plt.ion()
for i in range(100):
    a.append(i**2)
    b.append(i)
    #清屏
    plt.cla()
    #绘制折线图
    plt.plot(b,a)
    #暂停
    plt.pause(0.0001)
#关闭绘画
plt.ioff()
#展示最终结果
plt.show()
'''
x=np.random.randn(20)
y=np.random.randn(20)

#绘制点图
plt.scatter(x,y,label="like",c="blue",marker="s")
#添加数据
x=np.random.randn(10)
y=np.random.randn(10)
plt.scatter(x,y,label="dislike",c="red",marker="*")
#显示图例
plt.legend()

plt.show()




