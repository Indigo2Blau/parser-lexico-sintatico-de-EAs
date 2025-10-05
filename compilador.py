import sys
import signal
# from os import system
# signal.signal(signal.SIGINT, lambda x, y:  (system('cls'),print('tchau :('),exit(0)))
# sys.tracebacklimit = 0

class num:
    v: float | int | None

    def __init__(self, v):
        self.v = v

    def __str__(self) -> str:
        return str(self.v) # 'N' 
    
    def __repr__(self) -> str:
        return 'N' 

    def __eq__(self, value):
        return type(self) == value



    


class op:
    v: str | None

    def __init__(self, v):
        self.v = v
    def __str__(self):
        return str(self.v)
    
    def __eq__(self, value):
        return self.v == value
    
    def __repr__(self):
        return '°'

    def _None_solver(self, other, other2, div=False):
        if None == other2.v: return True
        if None == other.v: return True

    def __call__(self, x:num, y:num):    
        if self._None_solver(x,y): return num(None)    
        a, b = x.v, y.v
        match self.v:
            case '*':
                return num(a*b)
            case '+':
                return num(a+b)
            case '/':
                if b==0: return num(None)
                return num(a/b)
            case '-':
                return num(a-b)
            case '^':
                if a<0 and b<1 and b>-1: return num(None) 
                return num(a**b)
            case '.':
                b =  str(b).replace('.', '')
                if isinstance(a, int): ponto= '.'
                else: ponto = ''
                return num(float(str(a)+ponto+b))
            case _:
                raise Exception('não implementado')

# =================== // =============== fim classes =================== // =================== #

def make_num(s):
    if s == '.': return num(0.0)
    return num(float(s))

# =================== // =============== fim wraper =================== // =================== #

def lecxsor(n):
    i =0
    j =0
    pal = []
    numero = ['1','2','3','4','5','6','7','8','9','0', '.']
    while i<len(n):
        if n[i] in numero: pass
        # elif n[i] == ',':
        #     if i>j: pal.append(make_num(n[j:i]))
        #     j=i+1
        else:
            if i>j: pal.append(make_num(n[j:i]))
            pal.append(op(n[i]))
            j=i+1
        i+=1
    if j!=i: pal.append(make_num(n[j:i]))
        
    return pal

# função que lida de resolver dep de operações binárias
def consome(n:list, f, _num, *op):
    if len(n)>0 and n[0].v in op:
            _temp = n.pop(0) #efeito!
            _bool, _num_2 = f(n)
            if not _bool: 
                n.insert(0, _temp) #backtrack!
                return True, _num
            return _bool, _temp(_num, _num_2)
    return True, _num

#term_n são a super estrutura de prioridade das operações, maior o n° maior a prioridade!
def Term0(n): 
    _bool, _num = Term1(n)
    if _bool:
        return consome(n, Term0, _num, '+', '-')
    return _bool, _num
    
def Term1(n):
    _bool, _num = Term2(n)
    if _bool: 
        return consome(n, Term1, _num, '*', '/')
    return _bool, _num

def Term2(n):
    _bool, _num = Term3(n)
    if _bool: 
        return consome(n, Term2, _num, '^')
    return _bool, _num

def Term3(n):
    _bool, _num = Factor(n)
    if _bool: 
        return consome(n, Term3, _num, '.')
    return _bool, _num

# A base sempre será um número ou outra recursão
def Factor(n):
    temp = 0
    if n: 
        prox = n[0]
        if isinstance(prox, num):
                return True, n.pop(0)  #fim do galho

        if prox.v == '(':
            temp = n.pop(0) #nova rec
            _bool, _num = Term0(n)
            if  _bool and n and n[0].v == ')':
                n.pop(0)
                return True, _num #nova rec acabou
    if isinstance(temp, op): n.insert(0, temp)
    return False, num(None)
    

# =================== // =============== fim rec =================== // =================== #

def evalut(s, debugg=False):
    n = lecxsor(s)
    if debugg:
        return Term0(n)[0], n
    a = Term0(n)
    print(a[0], a[1], n)
    return a[0], a[1], n
    
# =================== // =============== fim  corpo  =================== // =================== #
aa = '''
 # ============================================================================================================ #
||   _____     _______    ___     ____   _____     __    _         ______    ______       ______     _____      ||
||  |// __]   /       |  |   \   /   |  |  |_ \   |__|  | |       /  _   |  |  __  \    /     //|   / __  \     ||
||  |  |     |   / \  |  |    \ /    |  |  |_| |   __   | |      |  |_|  |  | |  \  \  |   / \  |  |  \/__/     ||
||  |  |__   |   \_/  |  |  |\___/|  |  |  |__/   |//|  | |___   |   __  |  | |__/  /  |// \_/  |  |  |\  \     ||
||  |_____|  |_______/   |__|     |__|  |__|      |__|  |_____|  |__| |__|  |______/   |_______/   |__| \__\    ||
 # ============================================================================================================ #
        
    -------> MAS APENAS com expressões numéricas de inteiros pelos operadores { + , * , / , - } 
                                                                ________________________________________________
                                                               |    op = +: NxN   -> N                          |   
                                                               |           (a,b) |-> a+b                        |   
                                                               |================================================|   
                                                               |____a(op)b -> lambda (op,a,b) -> op(a,b) -> a+b_|
  '''

bb =     '''
#  _____________________________________________________________________________________________________________
  |   _____     _______    ___     ____   _____     __    _           ____    ______       _______     _____    ||# type: ignore
  |  |   __]   /       |  |   \   /   |  |  |_ \   |__|  | |      __/___ |\   |  __  \    /       |   / __  \   ||# type: ignore
  |  |//|     |   / \  |  |//  \ /    |  |//|_| |   __   | |       | |_||| \  | |  \  \  |// / \  |  |  \/__/   ||# type: ignore
  |  |  |__   |   \_/  |  |  |\___/|  |  |  |__/   |  |  | |____   |  __ |_/  | |__/  /  |   \_/  |  |  |\  \   ||# type: ignore
  |  |_____|  |_______/   |__|     |__|  |__|      |__|  |______|  |_/ |_|    |______/   |_______/   |__| \__\  ||# type: ignore
  ##===========================================================================================================//# type: ignore
  -> amongus exclama todo programador usa Ctrl + C para sair
  '''

# =================== // =============== fim  artes =================== // =================== #


def main():
    system('cls')
    print(aa)
    print('bom dia, interprete sua expressão algebrica aqui!\n'+     'escreva abaixo:')
    while True:
        s=None

        s = evalut(input())
        if s[0] == False:
            print()
            print('deseja ver os testes?\nParece que sua Ea não é válida..\n...escreva: testar\n')
            a = input()
            if a == 'testar':
                from testes import testes_comp as rr
                rr()
            else: evalut(a)
        

if __name__ == '__main__':
    main()

# =================== // =============== fim  main =================== // =================== #
