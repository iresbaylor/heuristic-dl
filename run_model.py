import tensorflow as tf
import keras
from keras.models import load_model
from keras.layers import Dense, Dropout
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
import json
from cil_utils import read_classifications_file, read_training_data_file, get_running_iteration

model = load_model('learning-model-' + str(get_running_iteration() - 1))

example = ['while (yv88Mum7wy > tk3 != nz1XW79xEuk > hqx139s > vzk7Dg9Z40)', 'else if (avD6TkGf920 == yv25zKYB8 > rnn41v2vgH)', 'else if (x > 0 && p) {']

tk = Tokenizer()
tk.fit_on_texts(example)
index_list = tk.texts_to_sequences(example)
x_train = pad_sequences(index_list, maxlen=128)

score = model.predict(x_train)
print("Prediction: " + str(score))
