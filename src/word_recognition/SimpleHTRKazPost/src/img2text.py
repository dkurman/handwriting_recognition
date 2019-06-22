import cv2
from DataLoader import DataLoader, Batch
from Model import Model, DecoderType
from SamplePreprocessor import preprocess
import tensorflow as tf

def img2text(img):
    tf.reset_default_graph()
    decoderType = DecoderType.BeamSearch

    fnCharList = './word_recognition/SimpleHTRKazPost/model/charList.txt'
    model = Model(open(fnCharList).read(), decoderType, mustRestore=True)
    img = preprocess(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), Model.imgSize)
    batch = Batch(None, [img])
    (recognized, probability) = model.inferBatch(batch, True)

    return recognized[0], probability[0]
