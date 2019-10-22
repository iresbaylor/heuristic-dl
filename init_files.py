import numpy as np
import json

def read_classifications_file():
    classificationsFile = open('classifications.json')
    classificationsData = json.load(classificationsFile)
    return np.array(classificationsData['classifications'])

def read_training_data_file():
    trainingFile = open('training_data.json')
    trainingData = json.load(trainingFile)
    return np.array(trainingData['training_data'])
