import json
from random import randint



numLoop = 1000
numCond = 1000

ralph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Ralph = list(map(lambda x: x.upper(), ralph))


def generate_random_conditional():
    condLength = randint(1,12)
    out = ''
    for i in range(condLength):
        bol = 0
        if i > 1:
            bol = randint(0,2)
        if bol == 0:
            out = out + ralph[randint(0,24)]
        elif bol == 1:
            out = out + Ralph[randint(0,24)]
        elif bol == 2:
            out = out + str(randint(0,9))
    return out

# Can make this better
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

def main():
    data = {}
    data['training_data'] = []

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

    for i in range(numLoop):
        conditionalN = randint(1, 8) # Random number of conditionals
        conditionals = [None] * conditionalN
        out = ''
        bol = randint(0, 3)
        if bol > 0:
            if bol == 1:
                out = out + 'while ('
                for i in range(conditionalN):
                    conditionals[i] = generate_random_conditional()

                out = out + generate_predicate(conditionals)
                out = out + ')'
            if bol == 2:
                randVar = generate_random_conditional()
                out = out + 'for (int ' + randVar + ' = 0; ' + randVar + ' < '+ str(randint(0,256)) + '; ' + randVar + '++)' #placeholder
            if bol == 3:
                randVar = generate_random_conditional()
                randVar2 = generate_random_conditional()
                out = out + 'for (RandObj ' + randVar + ' : ' + randVar2 + ')'
        else:
            out = 'do'
        bol = randint(0, 1)
        if bol == 1:
            out = out + ' {'
        let = randint(0,24)
        data['training_data'].append({
        'snippet':out,
        'lang':'Java',
        'classification':'loop'
        })

    print('DUMPING')
    with open('random_training_data.json', 'r+') as out:
        out.seek(0)
        json.dump(data, out)

if __name__ == "__main__":
    main()












    # eoa
