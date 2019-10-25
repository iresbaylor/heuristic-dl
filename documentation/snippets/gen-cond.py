for i in range(numCond):
    conditionalN = randint(1, 8) # Random number of conditionals
    conditionals = [None] * conditionalN
    out = ''
    bol = randint(0, 2)
    if bol > 0:
        out = out + 'else '
        out = out + 'if ('
        for i in range(conditionalN):
            conditionals[i] = generate_random_conditional()

        out = out + generate_predicate(conditionals)
        out = out + ')'
    else:
        bol = randint(0, 1)
        if bol == 1:
            out = out + '} '
        out = out + 'else'
    bol = randint(0, 1)
    if bol == 1:
        out = out + ' {'
    let = randint(0,24)
    data['training_data'].append({
    'snippet':out,
    'lang':'Java',
    'classification':'conditional'
    })
