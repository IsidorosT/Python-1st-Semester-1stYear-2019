def Zero(*eq):
    if len(eq) == 0:
        index = 0
        return index
    else:
        index = eq[0][0]
        k = eq[0][1]
        if k == "+":
            res = index + 0
        elif k == "-":
            res = 0 - index
        elif k == "x":
            res = index * 0
        elif k == "/":
            res = 0 / index
        else:
            if index != 0:
                res = 0 // index
        if index == 0:
            error = "Division with zero is invalid"
            return error
        else:
            return res    
def One(*eq):
    if len(eq) == 0:
        index = 1
        return index
    else:
        index = eq[0][0]
        k = eq[0][1]
        if k == "+":
            res = index + 1
        elif k == "-":
            res = 1 - index
        elif k == "x":
            res = index * 1
        elif k == "/" and index != 0 :
            res = 1 / index
        else:
            if index != 0:
                res = 1 // index
        if index == 0:
            error = "Division with zero is invalid"
            return error
        else:
            return res    
def Two(*eq):
    if len(eq) == 0:
        index = 2
        return index
    else:
        index = eq[0][0]
        k = eq[0][1]
        if k == "+":
            res = index + 2
        elif k == "-":
            res = 2 - index
        elif k == "x":
            res = index * 2
        elif k == "/" and index != 0:
            res = 2 / index
        else:
            if index != 0:
                res = 2 // index
        if index == 0:
            error = "Division with zero is invalid"
            return error
        else:
            return res   
def Three(*eq):
    if len(eq) == 0:
        index = 3
        return index
    else:
        index = eq[0][0]
        k = eq[0][1]
        if k == "+":
            res = index + 3
        elif k == "-":
            res = 3 - index
        elif k =="x":
            res = index * 3
        elif k == "/" and index != 0:
            res = 3 / index
        else:
            if index != 0:
                res = 3 // index 
        if index == 0:
            error = "Division with zero is invalid"
            return error
        else:
            return res   
def Four(*eq):
    if len(eq) == 0:
        index = 4
        return index
    else:
        index = eq[0][0]
        k = eq[0][1]
        if k == "+":
            res = index + 4
        elif k == "-":
            res = 4 - index
        elif k == "x":
            res = index * 4
        elif k == "/" and index != 0:
            res = 4 / index
        else:
            if index != 0:
                res = 4 // index
        if index == 0:
            error = "Division with zero is invalid"
            return error
        else:
            return res  
def Five(*eq):
    if len(eq) == 0:
        index = 5
        return index
    else:
        index = eq[0][0]
        k = eq[0][1]
        if k == "+":
            res = index + 5
        elif k == "-":
            res = 5 - index
        elif k == "x":
            res = index * 5
        elif k == "/" and index != 0:
            res = 5 / index
        else:
            if index != 0:
                res = 5 // index
        if index == 0:
            error = "Division with zero is invalid"
            return error
        else:
            return res    
def Six(*eq):
    if len(eq) == 0:
        index = 6
        return index
    else:
        index = eq[0][0]
        k = eq[0][1]
        if k == "+":
            res = index + 6
        elif k == "-":
            res = 6 - index
        elif k == "x":
            res = index * 6
        elif k == "/" and index != 0:
            res = 6 / index
        else:
            if index != 0:
                res = 6 // index 
        if index == 0:
            error = "Division with zero is invalid"
            return error
        else:
            return res   
def Seven(*eq):
    if len(eq) == 0:
        index = 7
        return index
    else:
        index = eq[0][0]
        k = eq[0][1]
        if k == "+":
            res = index + 7
        elif k == "-":
            res = 7 - index
        elif k == "x":
            res = index * 7
        elif k == "/" and index != 0:
            res = 7 / index
        else:
            if index != 0:
                res = 7 // index
        if index == 0:
            error = "Division with zero is invalid"
            return error
        else:
            return res   
def Eight(*eq):
    if len(eq) == 0:
        index = 8
        return index
    else:
        index = eq[0][0]
        k = eq[0][1]
        if k == "+":
            res = index + 8
        elif k == "-":
            res = 8 - index
        elif k == "x":
            res = index * 8
        elif k == "/" and index != 0:
            res = 8 / index
        else:
            if index != 0:
                res = 8 // index
        if index == 0:
            error = "Division with zero is invalid"
            return error
        else:
            return res    
def Nine(*eq):
    if len(eq) == 0:
        index = 9
        return index
    else:
        index = eq[0][0]
        k = eq[0][1]
        if k == "+":
            res = index + 9
        elif k == "-":
            res = 9 - index
        elif k == "x":
            res = index * 9
        elif k == "/" and index != 0:
            res = 9 / index
        else:
            if index != 0:
                res = 9 // index
        if index == 0:
            error = "Division with zero is invalid"
            return error
        else:
            return res  
def Plus(num):
    k = '+'
    return (num, k)
def Minus(num):
    k = '-'
    return (num, k)
def Times(num):
    k = 'x'
    return (num, k)
def Divide(num):
    k = '/'
    return (num, k)
def CDivide(num):
    k = 'div'
    return (num, k)

