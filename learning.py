import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
import json
from cil_utils import read_classifications_file, read_training_data_file, get_add_running_iteration

cls = read_classifications_file() # List of classification types
tdata = read_training_data_file() # Array of training data
tk = Tokenizer()

clsdict = {} # Create a mapping of the classification types for classification
for i in range(len(cls)):
    clsdict[cls[i]] = i

#--Initialized clsdict
print(clsdict)

xdata = [None] * len(tdata)
ydata = [None] * len(tdata)

for i in range(len(tdata)):
    xdata[i] = (tdata[i]['snippet'])
    ydata[i] = (clsdict[tdata[i]['classification']])

tk.fit_on_texts(xdata)
index_list = tk.texts_to_sequences(xdata)
x_train = pad_sequences(index_list, maxlen=128)

#--Initialized xdata and ydata
print(xdata)
print('---')
print(ydata)

model = Sequential()
model.add(Dense(64, activation='relu', input_dim=128))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))

adam = keras.optimizers.Adam(lr=0.001)

model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])

print("XDATA SHAPE: " + str(np.array(xdata).shape))
print("X_TRAIN SHAPE: " + str(np.array(x_train).shape))
print("YDATA SHAPE: " + str(np.array(ydata).shape))

ydata = to_categorical(ydata)
model.fit(x_train, ydata, epochs=100, batch_size=20)
model.save("learning-model-" + str(get_add_running_iteration()))
