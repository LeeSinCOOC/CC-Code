import mxnet

print(mxnet.__version__)

from mxnet import nd
from mxnet.gluon import nn

print(mxnet.cpu())
print(mxnet.gpu())



a = nd.array([1, 2, 3], ctx=mxnet.gpu())
print(a)

import gluoncv as gcv
print(gcv.utils.check_version('0.6.0'))
