from keras_ocr import pipeline
import keras_ocr

from matplotlib import pyplot as plt

pipeline = keras_ocr.pipeline.Pipeline()

image = "placa.jpg"

import numpy as np
prediction = pipeline.recognize(image)

#fig, axs = plt.subplots(nrows = le)