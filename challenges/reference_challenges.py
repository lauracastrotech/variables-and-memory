def challenge_01():
    apples = 1729
    oranges = 42
    papaya = apples
    print('apples',apples,'papaya', papaya)
    # 1 1729
    apples = apples + oranges
    print('apples',apples,'papaya', papaya)
    print('oranges',oranges)
    # 2 1729 + 42 =

def challenge_02():
    apples = 1729
    print(id(apples))
    oranges = 42
    print(id(oranges))
    bananas = [apples, oranges]
    # 3 [1729,42]
    print(id(bananas))

def challenge_03():
    apples = 1729
    oranges = 42
    bananas = [apples, oranges]
    print(f'This is apples id: {id(apples)}\nThis is oranges id: {id(oranges)}\nThis is bananas id: {id(bananas)}')
    challenge_03_helper(bananas)

def challenge_03_helper(kiwis):
    mangos = 315
    kiwis.append(mangos)
    # 4
    print(f'This is mango id: {id(mangos)}\nThis is kiwis id: {id(kiwis)}')
# challenge_01()
# challenge_02()
challenge_03()