def generate_predicate(conditionals):
    out = ''
    for i in range(len(conditionals)-1):
        out = out + conditionals[i]
        out = out + ' '
        bol = randint(0,6)
        if bol == 0:
            out = out + '&&'
        elif bol == 1:
            out = out + '||'
        elif bol == 2:
            out = out + '=='
        elif bol == 3:
            out = out + '>'
        elif bol == 3:
            out = out + '<'
        elif bol == 4:
            out = out + '>='
        elif bol == 5:
            out = out + '<='
        elif bol == 6:
            out = out + '!='
        out = out + ' '
    out = out + conditionals[len(conditionals) - 1]
    return out
