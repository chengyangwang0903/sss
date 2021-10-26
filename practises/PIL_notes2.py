#使用PIL生成验证码
import random
from PIL import Image,ImageDraw,ImageFont
class GeneratrCoder():
    #生成随机内容（A~Z）
    def get_Text(self):
        return chr(random.randint(65,90))
    #生成随机前景色
    def font_color(self):
        return (random.randint(60,120),
                random.randint(60, 120),
                random.randint(60, 120))
    #生成随机背景色
    def back_color(self):
        return (random.randint(110,180),
                random.randint(110,180),
                random.randint(110,180))
    #生成验证码
    def encoder(self):
        #生成画板
        w,h=240,60
        panel=Image.new(size=(w,h),color=(255,255,255),mode="RGB")
        #生成画笔
        draw=ImageDraw.Draw(panel)
        #创建字体
        font=ImageFont.truetype(font="C:\Windows\Fonts\Arial.ttf",size=30)
        #给画板上色
        for x in range(w):
            for y in range(h):
                draw.point((x,y),fill=self.back_color())
        #填入内容
        for i in range(4):
            draw.text((60*i+15,10),text=self.get_Text(),fill=self.font_color(),font=font)
        return panel
if __name__=='__main__':
    gen=GeneratrCoder()
    img=gen.encoder()
    img.show()
#作业：
#1.实现等比缩放（将任意的图像等比缩放为（230，230）的大小）
#2.通过矩阵操作实现查看RGB三个通道
#3.使用numpy将图像切成四份并展示
#4.使用plt实现多图轮播效果





