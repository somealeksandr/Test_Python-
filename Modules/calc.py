if __name__ == "__main__":
    plus()
    minus()
    multi()
    division()

def plus(*params):
    res = 0
    for item in params:
        res += item
    return res

def minus(a, b):
    return a - b

def multi(*params):
    res = params[0]
    for item in params:
        res *= item
    return res

def division(a, b):
    if b == 0:
        return "Divide by zero!"
    else:
        return a / b
     