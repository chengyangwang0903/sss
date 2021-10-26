from PIL import Image
import numpy as np
'''
'''

img=Image.open(r"sheep.png")
# print(img)
# img.show()
w,h=img.size
print(w,h)
print(img.getbands())#返回元组通道
print(img.mode)#返回字符串通道模式
p=img.getpixel((100,100))#查看某个像素值
print(p)

img1=img.convert("L")#转为1通道灰度图
print(img1.mode)
# img.show()
p1=img1.getpixel((100,100))#查看某个像素值
print(p1)

img2=img1.convert("RGB")
print(img2.mode)#转为RGB
# img.show()
p2=img2.getpixel((100,100))#查看某个像素值
print(p2)

#缩放
img3=img.resize((230,230))
# img3=img.resize((w//4,h//4))#等比缩放
# img3.show()
img3.save("2.jpg")
#抠图
img4=img.crop((0,400,500,1200))
# img4.show()
img4.save("3.jpg")
#旋转
img5=img4.rotate(45)
# img5.show()
#粘贴
img1.paste(img4)
# img1.show()

#翻转
img6=img4.transpose(Image.FLIP_LEFT_RIGHT)#左右翻转
# img6.show()
img7=img4.transpose(Image.FLIP_TOP_BOTTOM)#上下翻转
# img7.show()

#画图
#创建画笔
# draw=ImageDraw.Draw(img4)
# draw.rectangle((100,100,200,200),outline="red",width=3,fill="purple")#画矩形
# img4.show()

#拓展：滤波器
# img8=img4.filter(ImageFilter.CONTOUR)#铅笔画
# img8.show()
# img9=img4.filter(ImageFilter.BLUR)#模糊
# img9.show()
# img10=img4.filter(ImageFilter.EMBOSS)#浮雕
# img10.show()

#PIL和numpy结合
img_data=np.array(img)
print(img_data)
print(img_data.shape)#格式(h,w,c)
B_data=img_data[...,1]
print(f"B_data类型{B_data.dtype}")
B1_data=np.expand_dims(B_data,axis=2)
back_data=np.zeros((1757,886,1),dtype=np.uint8)
print(f"back_data类型{back_data.dtype}")
blue_data=np.concatenate((back_data,B1_data,back_data),axis=2)
B_data=B_data.transpose((1,0))#改变图片的data也能翻转
print(B_data.shape)
print(f"bule_data类型{blue_data.dtype}")
# bule_data=np.array(blue_data,dtype="uint8")
#numpy转图片
img11=Image.fromarray(blue_data)
print(img11.mode)
# img11.show()
img_data1=img_data[:850,:450,:]
img_data2=img_data[:850,450:,:]
img_data3=img_data[850:,:450,:]
img_data4=img_data[850:,450:,:]
img_1=Image.fromarray(img_data1)
img_2=Image.fromarray(img_data2)
img_3=Image.fromarray(img_data3)
img_4=Image.fromarray(img_data4)
img_1.show()
img_2.show()
img_3.show()
img_4.show()

