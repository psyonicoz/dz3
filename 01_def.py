def divid(a, b):
    try:
        print(a // b)
    except Exception as e:
        print(e)
    return


a = int(input('first element '))
b = int(input('second element '))
divid(a, b)
