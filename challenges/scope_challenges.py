def challenge_01():
    # 1 local
    outer_value = 42

    print(f"The value from outside is: {outer_value}")

def challenge_02():
    # 2 global 
    print(f"The value from outside is: {outer_value}")

# def challenge_03():
    # 3 Throws error: UnboundLocalError: cannot access local variable 
    # 'inner_value' where it is not associated with a value
    # print(f"The value from outside is: {inner_value}")

    # inner_value = 42

def challenge_04():
    # 4
    # prints global value of outer_value
    print(f"The value from outside is: {outer_value}")

    outer_value = 42

outer_value = 1729