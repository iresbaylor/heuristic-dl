cls = read_classifications_file(classifications) # List of classification types
tdata = read_training_data_file(training) # Array of training data
tk = Tokenizer()

clsdict = {} # Create a mapping of the classification types for classification
for i in range(len(cls)):
    clsdict[cls[i]] = i
