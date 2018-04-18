
## Color Space

Color space conversion in Waifu2x: RGABA --> RGB --> YCbCr --> Y

YCbCr

   YCbCr is subset of YUV

   Y：明亮度（Luminance或Luma），也就是灰阶值。“亮度”是透过RGB输入信号来建立的，方法是将RGB信号的特定部分叠加到一起。

    U&V：色度（Chrominance或Chroma），作用是描述影像色彩及饱和度，用于指定像素的颜色。“色度”则定义了颜色的两个方面─色调与饱和度，分别用Cr和CB来表示。

   Cb：反映的是RGB输入信号蓝色部分与RGB信号亮度值之间的差异。
   Cr：反映了RGB输入信号红色部分与RGB信号亮度值之间的差异。


[Wiki: YCBCr](https://en.wikipedia.org/wiki/YCbCr}


See: http://blog.csdn.net/alfredtofu/article/details/6303305

YCbCr是YUV经过缩放和偏移的翻版，可以看做YUV的子集。主要用于优化彩色视频信号的传输，使其向后相容老式黑白电视。与RGB视频信号传输相比，它最大的优点在于只需占用极少的频宽（RGB要求三个独立的视频信号同时传输）。

Y：明亮度（Luminance或Luma），也就是灰阶值。“亮度”是透过RGB输入信号来建立的，方法是将RGB信号的特定部分叠加到一起。

U&V：色度（Chrominance或Chroma），作用是描述影像色彩及饱和度，用于指定像素的颜色。“色度”则定义了颜色的两个方面─色调与饱和度，分别用Cr和CB来表示。

Cb：反映的是RGB输入信号蓝色部分与RGB信号亮度值之间的差异。
Cr：反映了RGB输入信号红色部分与RGB信号亮度值之间的差异。

在以下两个公式中RGB和YCbCr各分量的值的范围均为0-255。

RGB--> YCbCr

这个公式来自：Genesis Microchip. gm6010/gm6015 Programming Guide[M]. California US: Genesis Microchip Company, 2002:85-90

|Y  |   |16 |              |65.738   129.057  25.06 |   |R|
|Cb | = |128| +  (1/256) * |-37.945  -74.494  112.43| * |G|
|Cr |   |128|              |112.439  -94.154  -18.28|   |B|

即：

Y   = 0.257*R+0.564*G+0.098*B+16
Cb = -0.148*R-0.291*G+0.439*B+128
Cr  = 0.439*R-0.368*G-0.071*B+128

YCbCr--> RGB

这个公式来自：Genesis Microchip. gm6015 Preliminary Data Sheet[M]. California US: Genesis Microchip Company, 2001:33-34

|R|             |298.082  0        408.58   |   |Y -16  |
|G| = (1/256) * |298.082  -100.291 -208.12  | * |Cb-128 |
|B|             |298.082  516.411  0        |   |Cr-128 |

即：

R = 1.164*(Y-16)+1.596*(Cr-128)
G = 1.164*(Y-16)-0.392*(Cb-128)-0.813*(Cr-128)
B = 1.164*(Y-16)+2.017*(Cb-128)

