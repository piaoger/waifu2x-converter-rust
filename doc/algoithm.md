
# algorithms

##  convolution filter

http://stackoverflow.com/questions/19413386/gaussian-blur-mean-filter-convolution


## nn.SpatialConvolution


module = nn.SpatialConvolution(nInputPlane, nOutputPlane, kW, kH, [dW], [dH])

Applies a 2D convolution over an input image composed of several input planes. The input tensor in forward(input) is expected to be a 3D tensor (width x height x nInputPlane).

The parameters are the following:

nInputPlane
    The number of expected input planes in the image given into forward().
nOutputPlane
    The number of output planes the convolution layer will produce.
kW
    The kernel width of the convolution
kH
    The kernel height of the convolution
dW
    The step of the convolution in the width dimension. Default is 1.
dH
    The step of the convolution in the height dimension. Default is 1.

Note that depending of the size of your kernel, several (of the last) columns or rows of the input image might be lost. It is up to the user to add proper padding in images.

If the input image is a 3D tensor width x height x nInputPlane, the output image size will be owidth x oheight x nOutputPlane where

owidth  = (width  - kW) / dW + 1
oheight = (height - kH) / dH + 1 .

The parameters of the convolution can be found in self.weight (Tensor of size kH x kW x nInputPlane x nOutputPlane) and self.bias (Tensor of size nOutputPlane). The corresponding gradients can be found in self.gradWeight and self.gradBias.

The output value of the layer can be precisely described as:

output[i][j][k] = bias[k]
  + sum_l sum_{s=1}^kW sum_{t=1}^kH weight[s][t][l][k]
                                    * input[dW*(i-1)+s)][dH*(j-1)+t][l]
