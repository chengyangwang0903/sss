#作业：
#1.实现等比缩放（将任意的图像等比缩放为（230，230）的大小）
#2.通过矩阵操作实现查看RGB三个通道
#3.使用numpy将图像切成四份并展示
#4.使用plt实现多图轮播效果

from PIL import Image,ImageDraw,ImageFont
import random

class create_encoder():
    def back_color(self):
        return (random.randint(60,120),
                random.randint(60,120),
                random.randint(60,120)
                )
    def font_color(self):
        return (random.randint(110,180),
                random.randint(110,180),
                random.randint(110,180)
                )
    def letter(self):
        return chr(random.randint(97,122))
    def encoder(self):
        panel=Image.new(mode="RGB",size=(240,60),color=(255,255,255))
        draw=ImageDraw.Draw(panel)
        fonts=ImageFont.truetype(font="C:\Windows\Fonts\Arial.ttf",size=40)
        for i in range(240):
            for j in range(60):
                draw.point((i,j),fill=self.back_color())
        for i in range(4):
            draw.text((60*i+10,10),fill=self.font_color(),font=fonts,text=self.letter())
        return panel
if __name__ == '__main__':
    a=create_encoder()
    img=a.encoder()
    img.show()