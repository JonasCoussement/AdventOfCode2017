def initial_setup():
    row_init = open("Day1.txt").readlines()[0]
    return row_init

def check_next(inputlist):
    is_double =list()
    for i in range(0,len(inputlist)-1):
        if inputlist[i] == inputlist[i+1]:
            is_double.append(1)
        else:
            is_double.append(0)
    return is_double
    
def check_next2(inputlist):
    length = len(inputlist)
    doublelist = inputlist + inputlist
    is_double =list()
    for i in range(0,length):
        if doublelist[i] == doublelist[i+int(length/2)]:
            is_double.append(1)
        else:
            is_double.append(0)
    return is_double

def captcha(inputstring):
    add_last = list(inputstring)
    add_last.append(add_last[0])
    valid = check_next(add_last)
    return sum([int(a)*b for a,b in zip(add_last,valid)])

def captcha2(inputstring):
    valid = check_next2(list(inputstring))
    return sum([int(a)*b for a,b in zip(list(inputstring),valid)])

print(captcha(initial_setup()))
print(captcha2(initial_setup()))
