__author__ = 'oliver'

from pycocotools.coco import COCO
from pycocoevalcap.eval import COCOEvalCap
import matplotlib.pyplot as plt
import skimage.io as io
import pylab



def run(dataset,algName,outDir):

    pylab.rcParams['figure.figsize'] = (10.0, 8.0)

    import json
    from json import encoder
    encoder.FLOAT_REPR = lambda o: format(o, '.3f')

    # set up file names and pathes
    # dataDir='./data/'+dataset
    # dataDir= '/media/SSD/projects/NeuralTalkAnimator'
    dataType='val'

    # annFile='%s/annotations/captions_%s.json'%(dataDir,dataType)
    # annFile='/media/SSD/projects/NeuralTalkAnimator/data/youtube2text/captions_val2014.json'
    dataDir = 'data/'+dataset
    annFile='%s/captions_%s.json'%(dataDir,dataType)
    subtypes=['results', 'evalImgs', 'eval']
    [resFile, evalImgsFile, evalFile]= \
    ['%s/captions_%s_%s_%s.json'%(outDir,dataType,algName,subtype) for subtype in subtypes]

    coco = COCO(annFile)
    cocoRes = coco.loadRes(resFile)

    # create cocoEval object by taking coco and cocoRes
    cocoEval = COCOEvalCap(coco, cocoRes)

    # evaluate on a subset of images by setting
    # cocoEval.params['image_id'] = cocoRes.getImgIds()
    # please remove this line when evaluating the full validation set
    cocoEval.params['image_id'] = cocoRes.getImgIds()

    # evaluate results
    cocoEval.evaluate()

    # print output evaluation scores
    scores = list()
    for metric, score in cocoEval.eval.items():
        print '%s: %.3f'%(metric, score)
        scores.append(score)

    print 'inside metrics'
    return scores