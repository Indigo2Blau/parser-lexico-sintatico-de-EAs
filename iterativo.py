from compilador import *

def eval_iter(n):
    i =len(n)-1
    j =len(n)
    num = []
    while j>0:
        if n[i] == ',':
            num.append(n[i+1:j])
            j = i
        elif n[i] in ['*', '/', '+', '^']:  
            if i+1 !=j:
                num.append(n[i+1:j]) 
            num.append(oper(num, n[i]))
            if None in num: 
                return return_handle(n, num, i, j)
            j = i
        i-=1
    aux=''
    for x in range(len(num)-2, -1, -1):
        if num[x] !='.':
            aux += ',' + str(num[x])
    aux = aux.lstrip(',')
    if __name__ == '__main__':
        return True, num[-1], lecxsor(aux), aux 
    else:
        return True, lecxsor(aux)
    

def return_handle(n, num, i, j):
    aux = ''
    _bool = any(map(lambda x: isinstance(x, int), num))
    num = [x for x in num if x != None]
    for x in range(len(num)-2, -1, -1):
        if num[x] !='.':
            aux += ',' + str(num[x])
    aux = aux.lstrip(',')
    return _bool, lecxsor(n[:j]+aux)


def oper(num, op):
    try: a, b = int(num[-1]), int(num[-2])
    except ValueError: return None
    except IndexError: return None
    except Exception as e: raise e
    match op:
        case '*':
            ret = a * b
        case '/':
            if b == 0: return None
            ret = a // b
        case '+':
            ret = a + b
        case '^':
            ret = a**b
    # print('stack:',num, op, '->', ret) #depuração
    del num[-2:]
    return ret