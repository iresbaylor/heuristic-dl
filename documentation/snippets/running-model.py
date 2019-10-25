model = Sequential()
model.add(Dense(128, activation='relu', input_dim=128))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))

adam = keras.optimizers.Adam(lr=0.001)

model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
