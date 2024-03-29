import numpy as np
import json

def read_classifications_file(file):
    classificationsFile = open(file)
    classificationsData = json.load(classificationsFile)
    return np.array(classificationsData['classifications'])

def read_training_data_file(file):
    trainingFile = open(file)
    trainingData = json.load(trainingFile)
    return np.array(trainingData['training_data'])

def get_add_running_iteration():
    runtimes = open('runtimes.json', 'r+')
    rd = json.load(runtimes)
    t = rd['run']
    rd['run'] = rd['run'] + 1
    runtimes.seek(0)
    json.dump(rd, runtimes)
    return t

def get_running_iteration():
    runtimes = open('runtimes.json', 'r+')
    rd = json.load(runtimes)
    return rd['run']
