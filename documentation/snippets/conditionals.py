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
