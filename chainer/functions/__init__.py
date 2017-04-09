"""Collection of :class:`~chainer.Function` implementations."""

from chainer.functions.activation import clipped_relu  # NOQA
from chainer.functions.activation import crelu  # NOQA
from chainer.functions.activation import elu  # NOQA
from chainer.functions.activation import hard_sigmoid  # NOQA
from chainer.functions.activation import leaky_relu  # NOQA
from chainer.functions.activation import log_softmax  # NOQA
from chainer.functions.activation import lstm  # NOQA
from chainer.functions.activation import maxout  # NOQA
from chainer.functions.activation import prelu  # NOQA
from chainer.functions.activation import relu  # NOQA
from chainer.functions.activation import sigmoid  # NOQA
from chainer.functions.activation import slstm  # NOQA
from chainer.functions.activation import softmax  # NOQA
from chainer.functions.activation import softplus  # NOQA
from chainer.functions.activation import tanh  # NOQA
from chainer.functions.array import broadcast  # NOQA
from chainer.functions.array import cast  # NOQA
from chainer.functions.array import concat  # NOQA
from chainer.functions.array import copy  # NOQA
from chainer.functions.array import depth2space  # NOQA
from chainer.functions.array import dstack  # NOQA
from chainer.functions.array import expand_dims  # NOQA
from chainer.functions.array import flatten  # NOQA
from chainer.functions.array import fliplr  # NOQA
from chainer.functions.array import flipud  # NOQA
from chainer.functions.array import get_item  # NOQA
from chainer.functions.array import hstack  # NOQA
from chainer.functions.array import pad  # NOQA
from chainer.functions.array import permutate  # NOQA
from chainer.functions.array import reshape  # NOQA
from chainer.functions.array import resize_images  # NOQA
from chainer.functions.array import rollaxis  # NOQA
from chainer.functions.array import select_item  # NOQA
from chainer.functions.array import separate  # NOQA
from chainer.functions.array import space2depth  # NOQA
from chainer.functions.array import split_axis  # NOQA
from chainer.functions.array import squeeze  # NOQA
from chainer.functions.array import stack  # NOQA
from chainer.functions.array import swapaxes  # NOQA
from chainer.functions.array import tile  # NOQA
from chainer.functions.array import transpose  # NOQA
from chainer.functions.array import transpose_sequence  # NOQA
from chainer.functions.array import vstack  # NOQA
from chainer.functions.array import where  # NOQA
from chainer.functions.connection import bilinear  # NOQA
from chainer.functions.connection import convolution_2d  # NOQA
from chainer.functions.connection import convolution_nd  # NOQA
from chainer.functions.connection import deconvolution_2d  # NOQA
from chainer.functions.connection import deconvolution_nd  # NOQA
from chainer.functions.connection import dilated_convolution_2d  # NOQA
from chainer.functions.connection import embed_id  # NOQA
from chainer.functions.connection import linear  # NOQA
from chainer.functions.connection import n_step_lstm  # NOQA
from chainer.functions.evaluation import accuracy  # NOQA
from chainer.functions.evaluation import binary_accuracy  # NOQA
from chainer.functions.evaluation import classification_summary  # NOQA
from chainer.functions.loss import black_out  # NOQA
from chainer.functions.loss import contrastive  # NOQA
from chainer.functions.loss import crf1d  # NOQA
from chainer.functions.loss import cross_covariance  # NOQA
from chainer.functions.loss import ctc  # NOQA
from chainer.functions.loss import decov  # NOQA
from chainer.functions.loss import hinge  # NOQA
from chainer.functions.loss import huber_loss  # NOQA
from chainer.functions.loss import mean_absolute_error  # NOQA
from chainer.functions.loss import mean_squared_error  # NOQA
from chainer.functions.loss import negative_sampling  # NOQA
from chainer.functions.loss import sigmoid_cross_entropy  # NOQA
from chainer.functions.loss import softmax_cross_entropy  # NOQA
from chainer.functions.loss import triplet  # NOQA
from chainer.functions.loss import vae  # NOQA  # NOQA
from chainer.functions.math import average  # NOQA
from chainer.functions.math import basic_math  # NOQA
from chainer.functions.math import batch_l2_norm_squared  # NOQA
from chainer.functions.math import bias  # NOQA
from chainer.functions.math import ceil  # NOQA
from chainer.functions.math import clip  # NOQA
from chainer.functions.math import det  # NOQA
from chainer.functions.math import exponential  # NOQA
from chainer.functions.math import exponential_m1  # NOQA
from chainer.functions.math import floor  # NOQA
from chainer.functions.math import fmod  # NOQA
from chainer.functions.math import hyperbolic  # NOQA
from chainer.functions.math import identity  # NOQA
from chainer.functions.math import inv  # NOQA
from chainer.functions.math import linear_interpolate  # NOQA
from chainer.functions.math import logarithm_1p  # NOQA
from chainer.functions.math import logsumexp  # NOQA
from chainer.functions.math import matmul  # NOQA
from chainer.functions.math import maximum  # NOQA
from chainer.functions.math import minimum  # NOQA
from chainer.functions.math import minmax  # NOQA
from chainer.functions.math import scale  # NOQA
from chainer.functions.math import sqrt  # NOQA
from chainer.functions.math import square  # NOQA
from chainer.functions.math import squared_difference  # NOQA
from chainer.functions.math import sum  # NOQA
from chainer.functions.math import trigonometric  # NOQA
from chainer.functions.noise import dropout  # NOQA
from chainer.functions.noise import gaussian  # NOQA
from chainer.functions.noise import zoneout  # NOQA
from chainer.functions.normalization import batch_normalization  # NOQA
from chainer.functions.normalization import l2_normalization  # NOQA
from chainer.functions.normalization import local_response_normalization  # NOQA
from chainer.functions.pooling import average_pooling_2d  # NOQA
from chainer.functions.pooling import average_pooling_nd  # NOQA
from chainer.functions.pooling import max_pooling_2d  # NOQA
from chainer.functions.pooling import max_pooling_nd  # NOQA
from chainer.functions.pooling import roi_pooling_2d  # NOQA
from chainer.functions.pooling import spatial_pyramid_pooling_2d  # NOQA
from chainer.functions.pooling import unpooling_2d  # NOQA
from chainer.functions.pooling import unpooling_nd  # NOQA
from chainer.functions.pooling import upsampling_2d  # NOQA
from chainer.functions.theano import theano_function  # NOQA
from chainer.functions.util import forget  # NOQA


# import class and function
from chainer.functions.activation.clipped_relu import clipped_relu  # NOQA
from chainer.functions.activation.clipped_relu import ClippedReLU  # NOQA
from chainer.functions.activation.crelu import crelu  # NOQA
from chainer.functions.activation.crelu import CReLU  # NOQA
from chainer.functions.activation.elu import elu  # NOQA
from chainer.functions.activation.elu import ELU  # NOQA
from chainer.functions.activation.hard_sigmoid import hard_sigmoid  # NOQA
from chainer.functions.activation.hard_sigmoid import HardSigmoid  # NOQA
from chainer.functions.activation.leaky_relu import leaky_relu  # NOQA
from chainer.functions.activation.leaky_relu import LeakyReLU  # NOQA
from chainer.functions.activation.log_softmax import log_softmax  # NOQA
from chainer.functions.activation.log_softmax import LogSoftmax  # NOQA
from chainer.functions.activation.lstm import lstm  # NOQA
from chainer.functions.activation.lstm import LSTM  # NOQA
from chainer.functions.activation.maxout import maxout  # NOQA
from chainer.functions.activation.prelu import prelu  # NOQA
from chainer.functions.activation.relu import relu  # NOQA
from chainer.functions.activation.relu import ReLU  # NOQA
from chainer.functions.activation.sigmoid import sigmoid  # NOQA
from chainer.functions.activation.sigmoid import Sigmoid  # NOQA
from chainer.functions.activation.slstm import slstm  # NOQA
from chainer.functions.activation.slstm import SLSTM  # NOQA
from chainer.functions.activation.softmax import softmax  # NOQA
from chainer.functions.activation.softmax import Softmax  # NOQA
from chainer.functions.activation.softplus import softplus  # NOQA
from chainer.functions.activation.softplus import Softplus  # NOQA
from chainer.functions.activation.tanh import tanh  # NOQA
from chainer.functions.activation.tanh import Tanh  # NOQA

from chainer.functions.array.broadcast import broadcast  # NOQA
from chainer.functions.array.broadcast import Broadcast  # NOQA
from chainer.functions.array.broadcast import broadcast_to  # NOQA
from chainer.functions.array.broadcast import BroadcastTo  # NOQA
from chainer.functions.array.cast import cast  # NOQA
from chainer.functions.array.cast import Cast  # NOQA
from chainer.functions.array.concat import concat  # NOQA
from chainer.functions.array.concat import Concat  # NOQA
from chainer.functions.array.copy import copy  # NOQA
from chainer.functions.array.copy import Copy  # NOQA
from chainer.functions.array.depth2space import depth2space  # NOQA
from chainer.functions.array.depth2space import Depth2Space  # NOQA
from chainer.functions.array.dstack import dstack  # NOQA
from chainer.functions.array.expand_dims import expand_dims  # NOQA
from chainer.functions.array.expand_dims import ExpandDims  # NOQA
from chainer.functions.array.flatten import flatten  # NOQA
from chainer.functions.array.flatten import Flatten  # NOQA
from chainer.functions.array.fliplr import fliplr  # NOQA
from chainer.functions.array.fliplr import FlipLR  # NOQA
from chainer.functions.array.flipud import flipud  # NOQA
from chainer.functions.array.flipud import FlipUD  # NOQA
from chainer.functions.array.get_item import get_item  # NOQA
from chainer.functions.array.get_item import GetItem  # NOQA
from chainer.functions.array.hstack import hstack  # NOQA
from chainer.functions.array.pad import pad  # NOQA
from chainer.functions.array.pad import Pad  # NOQA
from chainer.functions.array.permutate import permutate  # NOQA
from chainer.functions.array.permutate import Permutate  # NOQA
from chainer.functions.array.reshape import reshape  # NOQA
from chainer.functions.array.reshape import Reshape  # NOQA
from chainer.functions.array.resize_images import resize_images  # NOQA
from chainer.functions.array.resize_images import ResizeImages  # NOQA
from chainer.functions.array.rollaxis import rollaxis  # NOQA
from chainer.functions.array.rollaxis import Rollaxis  # NOQA
from chainer.functions.array.select_item import select_item  # NOQA
from chainer.functions.array.select_item import SelectItem  # NOQA
from chainer.functions.array.separate import separate  # NOQA
from chainer.functions.array.space2depth import space2depth  # NOQA
from chainer.functions.array.space2depth import Space2Depth  # NOQA
from chainer.functions.array.split_axis import split_axis  # NOQA
from chainer.functions.array.split_axis import SplitAxis  # NOQA
from chainer.functions.array.squeeze import squeeze  # NOQA
from chainer.functions.array.squeeze import Squeeze  # NOQA
from chainer.functions.array.stack import stack  # NOQA
from chainer.functions.array.swapaxes import swapaxes  # NOQA
from chainer.functions.array.swapaxes import Swapaxes  # NOQA
from chainer.functions.array.tile import tile  # NOQA
from chainer.functions.array.tile import Tile  # NOQA
from chainer.functions.array.transpose import transpose  # NOQA
from chainer.functions.array.transpose import Transpose  # NOQA
from chainer.functions.array.transpose_sequence import transpose_sequence  # NOQA
from chainer.functions.array.transpose_sequence import TransposeSequence  # NOQA
from chainer.functions.array.vstack import vstack  # NOQA
from chainer.functions.array.where import where  # NOQA
from chainer.functions.array.where import Where  # NOQA

from chainer.functions.connection.bilinear import bilinear  # NOQA
from chainer.functions.connection.convolution_2d import convolution_2d  # NOQA
from chainer.functions.connection.convolution_nd import convolution_nd  # NOQA
from chainer.functions.connection.deconvolution_2d import deconvolution_2d  # NOQA
from chainer.functions.connection.deconvolution_nd import deconvolution_nd  # NOQA
from chainer.functions.connection.dilated_convolution_2d import dilated_convolution_2d  # NOQA
from chainer.functions.connection.embed_id import embed_id  # NOQA
from chainer.functions.connection.linear import linear  # NOQA
from chainer.functions.connection.n_step_lstm import n_step_lstm  # NOQA
from chainer.functions.connection.n_step_lstm import NStepLSTM  # NOQA

from chainer.functions.evaluation.accuracy import accuracy  # NOQA
from chainer.functions.evaluation.accuracy import Accuracy  # NOQA
from chainer.functions.evaluation.binary_accuracy import binary_accuracy  # NOQA
from chainer.functions.evaluation.binary_accuracy import BinaryAccuracy  # NOQA
from chainer.functions.evaluation.classification_summary import classification_summary  # NOQA
from chainer.functions.evaluation.classification_summary import ClassificationSummary  # NOQA
from chainer.functions.evaluation.classification_summary import f1_score  # NOQA
from chainer.functions.evaluation.classification_summary import precision  # NOQA
from chainer.functions.evaluation.classification_summary import recall  # NOQA
from chainer.functions.evaluation.r2_score import r2_score  # NOQA

from chainer.functions.loss.black_out import black_out  # NOQA
from chainer.functions.loss.contrastive import contrastive  # NOQA
from chainer.functions.loss.contrastive import Contrastive  # NOQA
from chainer.functions.loss.crf1d import argmax_crf1d  # NOQA
from chainer.functions.loss.crf1d import crf1d  # NOQA
from chainer.functions.loss.cross_covariance import cross_covariance  # NOQA
from chainer.functions.loss.cross_covariance import CrossCovariance  # NOQA
from chainer.functions.loss.ctc import connectionist_temporal_classification  # NOQA
from chainer.functions.loss.ctc import ConnectionistTemporalClassification  # NOQA
from chainer.functions.loss.decov import decov  # NOQA
from chainer.functions.loss.decov import DeCov  # NOQA
from chainer.functions.loss.hinge import hinge  # NOQA
from chainer.functions.loss.hinge import Hinge  # NOQA
from chainer.functions.loss.huber_loss import huber_loss  # NOQA
from chainer.functions.loss.huber_loss import HuberLoss  # NOQA
from chainer.functions.loss.mean_absolute_error import mean_absolute_error  # NOQA
from chainer.functions.loss.mean_absolute_error import MeanAbsoluteError  # NOQA
from chainer.functions.loss.mean_squared_error import mean_squared_error  # NOQA
from chainer.functions.loss.mean_squared_error import MeanSquaredError  # NOQA
from chainer.functions.loss.negative_sampling import negative_sampling  # NOQA
from chainer.functions.loss.sigmoid_cross_entropy import sigmoid_cross_entropy  # NOQA
from chainer.functions.loss.sigmoid_cross_entropy import SigmoidCrossEntropy  # NOQA
from chainer.functions.loss.softmax_cross_entropy import softmax_cross_entropy  # NOQA
from chainer.functions.loss.softmax_cross_entropy import SoftmaxCrossEntropy  # NOQA
from chainer.functions.loss.triplet import triplet  # NOQA
from chainer.functions.loss.triplet import Triplet  # NOQA
from chainer.functions.loss.vae import bernoulli_nll  # NOQA
from chainer.functions.loss.vae import gaussian_kl_divergence  # NOQA
from chainer.functions.loss.vae import gaussian_nll  # NOQA

from chainer.functions.math.average import average  # NOQA
from chainer.functions.math.basic_math import absolute  # NOQA
from chainer.functions.math.batch_l2_norm_squared import batch_l2_norm_squared  # NOQA
from chainer.functions.math.batch_l2_norm_squared import BatchL2NormSquared  # NOQA
from chainer.functions.math.bias import bias  # NOQA
from chainer.functions.math.ceil import ceil  # NOQA
from chainer.functions.math.ceil import Ceil  # NOQA
from chainer.functions.math.clip import clip  # NOQA
from chainer.functions.math.clip import Clip  # NOQA
from chainer.functions.math.det import batch_det  # NOQA
from chainer.functions.math.det import BatchDet  # NOQA
from chainer.functions.math.det import det  # NOQA
from chainer.functions.math.exponential import exp  # NOQA
from chainer.functions.math.exponential import Exp  # NOQA
from chainer.functions.math.exponential import log  # NOQA
from chainer.functions.math.exponential import Log  # NOQA
from chainer.functions.math.exponential import log10  # NOQA
from chainer.functions.math.exponential import Log10  # NOQA
from chainer.functions.math.exponential import log2  # NOQA
from chainer.functions.math.exponential import Log2  # NOQA
from chainer.functions.math.exponential_m1 import expm1  # NOQA
from chainer.functions.math.exponential_m1 import Expm1  # NOQA
from chainer.functions.math.floor import floor  # NOQA
from chainer.functions.math.floor import Floor  # NOQA
from chainer.functions.math.fmod import fmod  # NOQA
from chainer.functions.math.fmod import Fmod  # NOQA
from chainer.functions.math.hyperbolic import cosh  # NOQA
from chainer.functions.math.hyperbolic import Cosh  # NOQA
from chainer.functions.math.hyperbolic import sinh  # NOQA
from chainer.functions.math.hyperbolic import Sinh  # NOQA
from chainer.functions.math.identity import identity  # NOQA
from chainer.functions.math.identity import Identity  # NOQA
from chainer.functions.math.inv import batch_inv  # NOQA
from chainer.functions.math.inv import BatchInv  # NOQA
from chainer.functions.math.inv import inv  # NOQA
from chainer.functions.math.inv import Inv  # NOQA
from chainer.functions.math.linear_interpolate import linear_interpolate  # NOQA
from chainer.functions.math.linear_interpolate import LinearInterpolate  # NOQA
from chainer.functions.math.logarithm_1p import Log1p  # NOQA
from chainer.functions.math.logarithm_1p import log1p  # NOQA
from chainer.functions.math.logsumexp import logsumexp  # NOQA
from chainer.functions.math.logsumexp import LogSumExp  # NOQA
from chainer.functions.math.matmul import batch_matmul  # NOQA
from chainer.functions.math.matmul import BatchMatMul  # NOQA
from chainer.functions.math.matmul import matmul  # NOQA
from chainer.functions.math.matmul import MatMul  # NOQA
from chainer.functions.math.matmul import numpy_like_matmul  # NOQA
from chainer.functions.math.matmul import NumpyLikeMatMul  # NOQA
from chainer.functions.math.maximum import maximum  # NOQA
from chainer.functions.math.maximum import Maximum  # NOQA
from chainer.functions.math.minimum import minimum  # NOQA
from chainer.functions.math.minimum import Minimum  # NOQA
from chainer.functions.math.minmax import argmax  # NOQA
from chainer.functions.math.minmax import ArgMax  # NOQA
from chainer.functions.math.minmax import argmin  # NOQA
from chainer.functions.math.minmax import ArgMin  # NOQA
from chainer.functions.math.minmax import max  # NOQA
from chainer.functions.math.minmax import Max  # NOQA
from chainer.functions.math.minmax import min  # NOQA
from chainer.functions.math.minmax import Min  # NOQA
from chainer.functions.math.scale import scale  # NOQA
from chainer.functions.math.sqrt import rsqrt  # NOQA
from chainer.functions.math.sqrt import sqrt  # NOQA
from chainer.functions.math.sqrt import Sqrt  # NOQA
from chainer.functions.math.square import square  # NOQA
from chainer.functions.math.square import Square  # NOQA
from chainer.functions.math.squared_difference import squared_difference  # NOQA
from chainer.functions.math.squared_difference import SquaredDifference  # NOQA
from chainer.functions.math.sum import sum  # NOQA
from chainer.functions.math.sum import Sum  # NOQA
from chainer.functions.math.trigonometric import arccos  # NOQA
from chainer.functions.math.trigonometric import Arccos  # NOQA
from chainer.functions.math.trigonometric import arcsin  # NOQA
from chainer.functions.math.trigonometric import Arcsin  # NOQA
from chainer.functions.math.trigonometric import arctan  # NOQA
from chainer.functions.math.trigonometric import Arctan  # NOQA
from chainer.functions.math.trigonometric import cos  # NOQA
from chainer.functions.math.trigonometric import Cos  # NOQA
from chainer.functions.math.trigonometric import sin  # NOQA
from chainer.functions.math.trigonometric import Sin  # NOQA
from chainer.functions.math.trigonometric import tan  # NOQA
from chainer.functions.math.trigonometric import Tan  # NOQA

from chainer.functions.noise.dropout import dropout  # NOQA
from chainer.functions.noise.dropout import Dropout  # NOQA
from chainer.functions.noise.gaussian import gaussian  # NOQA
from chainer.functions.noise.gaussian import Gaussian  # NOQA
from chainer.functions.noise.zoneout import zoneout  # NOQA
from chainer.functions.noise.zoneout import Zoneout  # NOQA

from chainer.functions.normalization.batch_normalization import batch_normalization  # NOQA
from chainer.functions.normalization.batch_normalization import fixed_batch_normalization  # NOQA
from chainer.functions.normalization.l2_normalization import normalize  # NOQA
from chainer.functions.normalization.l2_normalization import NormalizeL2  # NOQA
from chainer.functions.normalization.local_response_normalization import local_response_normalization  # NOQA
from chainer.functions.normalization.local_response_normalization import LocalResponseNormalization  # NOQA

from chainer.functions.pooling.average_pooling_2d import average_pooling_2d  # NOQA
from chainer.functions.pooling.average_pooling_2d import AveragePooling2D  # NOQA
from chainer.functions.pooling.average_pooling_nd import average_pooling_nd  # NOQA
from chainer.functions.pooling.average_pooling_nd import AveragePoolingND  # NOQA
from chainer.functions.pooling.max_pooling_2d import max_pooling_2d  # NOQA
from chainer.functions.pooling.max_pooling_2d import MaxPooling2D  # NOQA
from chainer.functions.pooling.max_pooling_nd import max_pooling_nd  # NOQA
from chainer.functions.pooling.max_pooling_nd import MaxPoolingND  # NOQA
from chainer.functions.pooling.roi_pooling_2d import roi_pooling_2d  # NOQA
from chainer.functions.pooling.roi_pooling_2d import ROIPooling2D  # NOQA
from chainer.functions.pooling.spatial_pyramid_pooling_2d import spatial_pyramid_pooling_2d  # NOQA
from chainer.functions.pooling.spatial_pyramid_pooling_2d import SpatialPyramidPooling2D  # NOQA
from chainer.functions.pooling.unpooling_2d import Unpooling2D  # NOQA
from chainer.functions.pooling.unpooling_2d import unpooling_2d  # NOQA
from chainer.functions.pooling.unpooling_nd import unpooling_nd  # NOQA
from chainer.functions.pooling.unpooling_nd import UnpoolingND  # NOQA
from chainer.functions.pooling.upsampling_2d import Upsampling2D  # NOQA
from chainer.functions.pooling.upsampling_2d import upsampling_2d  # NOQA

from chainer.functions.theano.theano_function import TheanoFunction  # NOQA

from chainer.functions.util.forget import forget  # NOQA
from chainer.functions.util.forget import Forget  # NOQA

# Import for backward compatibility
from chainer.links.activation.prelu import PReLU  # NOQA

from chainer.links.connection.bilinear import Bilinear  # NOQA
from chainer.links.connection.convolution_2d import Convolution2D  # NOQA
from chainer.links.connection.dilated_convolution_2d import DilatedConvolution2D  # NOQA
from chainer.links.connection.embed_id import EmbedID  # NOQA
from chainer.links.connection.inception import Inception  # NOQA
from chainer.links.connection.inceptionbn import InceptionBN  # NOQA
from chainer.links.connection.linear import Linear  # NOQA
from chainer.links.connection.parameter import Parameter  # NOQA

from chainer.links.loss.hierarchical_softmax import BinaryHierarchicalSoftmax  # NOQA
from chainer.links.loss.negative_sampling import NegativeSampling  # NOQA

from chainer.links.normalization.batch_normalization import BatchNormalization  # NOQA
