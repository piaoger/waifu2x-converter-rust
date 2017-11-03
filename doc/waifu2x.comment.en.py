# -*- coding: utf-8 -*-

# waifu2x.py by @marcan42 based on https://github.com/nagadomi/waifu2x
# MIT license, see https://github.com/nagadomi/waifu2x/blob/master/LICENSE

# 必要なモジュールのインポート

# import modules
import json, sys, numpy as np
from scipy import misc, signal
from PIL import Image


# Model export script: https://mrcn.st/t/export_model.lua (needs a working waifu2x install)

#infile, outfile,
modelpath = sys.argv[1:]
model = json.load(open(modelpath))

# layer 1:
#   * nInputPlane : number of input planes
#   * nOutputPlane : number of out planes
#   * weight : The set of weighting matrix for performing convolution operation on the input plane
#     - nInputPlane: That packs the number of weight matrix is nOutputPlane number entered. All elements of the matrix is a float value.
#     - For example, the first time are 32 things you pack one of the weighting matrix,
#       2 tier are 32 things you pack 32 weight matrix is (the number of that is the matrix 1024) entered。
#     - One of the weighting matrix has become all 3x3 matrix. Accordingly, the size of the plane whenever performing convolution once reduced by vertical and horizontal one element.
#     - Calculating the time of the anchor (position of the matrix around the convolution) is believed to be likely (2,2) (otherwise, the output plane ends up moving in a strange direction).
#   * bias : Output plane for one (by adding to all elements) multiplied by bias value
#     - float values are prepared for the number of nOutputPlane.
#   * kW,kH : Unused values (seems to be the weight matrix one size. Are all in the case of models is distributed 3x3)

# color space: RGBA --> RCbCr
im = Image.open(infile).convert("YCbCr")
im = misc.fromimage(im.resize((2*im.size[0], 2*im.size[1]), resample=Image.NEAREST)).astype("float32")
# After resizing NearestNeighbor method input image to the width and height of 2 times, and it can be handled matrix representation in scipy,
# The type of the element to the 32bit-float

planes = [np.pad(im[:,:,0], len(model), "edge") / 255.0]
# 画像データの周りに、画像の端をコピーする形で、モデルの大きさ(核の行列の大きさ)分だけパッドを入れ、0~1の間でクリップする
# このplanesは輝度情報のみを取り出している(!)
# オリジナルのwaifu2xも、reconstruct時に入力をYUV色空間に変換した後、Yのみを取り出して処理している


 #  weight x 32, bias x 32
 #  [{
 #    "weight": [
 #      [
 #        [
 #          [
 #            -0.0092529794201255,
 #            -0.10844283550978,
 #            -0.021117901429534
 #          ]
 #        ]
 #      ]
 #    ],
 #    "nOutputPlane": 32,
 #    "kW": 3,
 #    "kH": 3,
 #    "bias": [
 #    ],
 #    "nInputPlane": 1
 # }]


# Calculate the required number of times of the convolution operation
count = sum(step["nInputPlane"] * step["nOutputPlane"] for step in model)# 畳み込み演算の必要回数を計算
# つまり、countの数だけ入力平面に対する重み行列の畳み込みが行われる。
progress = 0

for step in model: # ループ:ステップ(1つのモデル階層) 始め
    assert step["nInputPlane"] == len(planes)
    # このステップのモデルに定義された入力平面の数と実際の入力平面の数は一致していなければならない
    assert step["nOutputPlane"] == len(step["weight"]) == len(step["bias"])
    # モデルの出力平面はモデルの重み行列集合の数とそのバイアスの数と一致していなければならない
    # つまり、各ステップの重み行列集合の数とそのバイアスの数だけ、そのステップによって平面が出力される

    o_planes = [] # 出力平面の格納場所を初期化

    # >>> x=[1,2,3]
    # >>> y=[4,5,6]
    # >>> zipped = zip(x,y)
    # >>> zipped
    #[(1, 4), (2, 5), (3, 6)]
    for bias, weights in zip(step["bias"], step["weight"]): # ループ:バイアス&重み行列集合 始め
        partial = None # partialをNone(null値)に初期化
        for ip, kernel in zip(planes, weights): # ループ:入力平面&核(重み行列) 始め

            # fftconvolve: Convolve two N-dimensional arrays using FFT
            p = signal.fftconvolve(ip, np.float32(kernel), "valid") # 入力平面に対して核を畳み込み演算
            if partial is None:
                partial = p # 最初の畳み込み演算の結果を代入
            else:
                partial += p # 畳み込み演算の結果を加算したものを代入
                # したがって、partialにはこのステップにおける全ての入力平面に対する重み行列の畳み込み演算の結果の総和が入る
            progress += 1
            sys.stderr.write("\r%.1f%%..." % (100 * progress / float(count)))
        # ループ:入力平面&核 終わり
        partial += np.float32(bias) # 計算したpartialにバイアスを加算(バイアスは1つの数値なので、partial全体にバイアスがかかる)
        # ここまでが1つの出力平面の生成処理
        o_planes.append(partial) # 出力平面の集合にpartialを加える
    # ループ:バイアス&重み 終わり
    planes = [np.maximum(p, 0) + 0.1 * np.minimum(p, 0) for p in o_planes]
    # 出力平面(を表す行列)に存在する負の値を0.1倍する

    # この時点で、出力平面このステップにおけるnOutputPlaneの数だけ生成される

# ループ:ステップ 終わり

assert len(planes) == 1 # 最後のステップにおける出力平面は1つでなければならない
im[:,:,0] = np.clip(planes[0], 0, 1) * 255
# 得られた出力平面の全要素を0~1にクリップした後、
misc.toimage(im, mode="YCbCr").convert("RGB").save(outfile)
sys.stderr.write("Done\n")
