xdata = [None] * len(tdata)
ydata = [None] * len(tdata)

for i in range(len(tdata)):
    xdata[i] = (tdata[i]['snippet'])
    ydata[i] = (clsdict[tdata[i]['classification']])

tk.fit_on_texts(xdata)
index_list = tk.texts_to_sequences(xdata)
x_train = pad_sequences(index_list, maxlen=128)
