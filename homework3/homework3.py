# 3.1 say goodbye
def say_goodbye(name):
    print('goodbye', name)

say_goodbye('test')
# 3.2 area of a circle
def area_C(radius):
    print(3.14*(radius**2))

area_C(4)
# 4.1 subtract, multiply, and divide
def subtract(a, b):
    return a-b
subtract(9,8)

def multiply(a, b):
    return a*b
multiply(5,7)

def divide(a, b):
    return a/b
divide(6,3)

# 5.1 wha should i wear?
readings = [1,2,3,4,5]
def minmaxtemp(readings):
    mins = min(readings)
    maxs = max(readings)
    return mins,maxs
minmaxtemp(readings)

# 5.2 check if its the weekend
def dayofweek(day):
    if day<= 6:
        return False
    else:
        return True
dayofweek(1)

# 5.3 fuel efficiency calculator
def effeciency(distance,gallons):
    return distance/gallons
effeciency(3,5)

# 5.4 secret code
def secret(inty):
    mm = inty % 10
    nn = inty //10
    dig = 10**len(str(nn))
    return mm*dig+nn
secret(3254)
#unfortunately had to consult ai to get more hints. 

# 6.1 oski stole my power?
def powa(a,b):
    starts = 1
    for i in range(b):
        starts *=a
    return starts
powa(7, 2)

# 6.2 min and max w loops
# can oski pls stop hacking my computer
# 6.2.1 for loops
rando = [1,4,3,6,2]
def minny(listy):
    small=listy[0]
    for num in listy:
        if num<small:
            small = num
    return small
print(minny(rando))

def maxy(listy):
    larg = listy [0]
    for num in listy:
        if num>larg:
            larg = num
    return larg
maxy(rando)


# 6.2.2 while loops
def whiiile(lista):
    ya = 1
    minis = lista[0]
    while ya < len(lista):
        if lista[ya] < minis:
            minis = lista[ya]
        ya += 1
    return minis
whiiile(rando)

def wheel(listr):
    oi = 1
    maxis = listr[0]
    while oi < len(listr):
        if listr[oi] > maxis:
            maxis = listr[oi]
        oi += 1
    return maxis
wheel(rando)

# 6.2.3
def splita(inty):
    nth = len(str(inty))
    toats = 0
    while nth>0:
        whatamidoing = inty//10**(nth-1)%10
        toats += whatamidoing
        nth -= 1
    return toats
print(splita(324))
print(f'print the sum (6.3.3) with number {324}')

909%10
909//10
10**len(str(9))
90*10+9
3254//10
3254%10
10**len(str(3254))*4