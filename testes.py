from compilador import *
from iterativo import *
from functools import partial
# import sys
# import signal
# from os import system
# sys.tracebacklimit = 10

def test_rap():
    print('testes de wraper:')
    a = num(1)
    b = num(2)
    c = num(None)
    d = num(0)
    testes = [
        (op('+')(a,b),  '3',    "op('+')(a,b)"),
        (op('+')(b,a),  '3',    "op('+')(b,a)"),
        (op('+')(a,c),  'None', "op('+')(a,c)"),
        (op('+')(c,a),  'None', "op('+')(c,a)"),
        ]
    print('testes de soma')
    for n in testes:printa(n, lambda x: x, True)
    testes = [
        (op('*')(a,b),  '2',    "op('*')(a,b)"),
        (op('*')(b,a),  '2',    "op('*')(b,a)"),
        (op('*')(a,c),  'None', "op('*')(a,c)"),
        (op('*')(c,a),  'None', "op('*')(c,a)"),
    ]
    print('testes de mult')
    for n in testes:printa(n, lambda x: x, True)
    testes = [
        (op('/')(a,b),  '0.5',  "op('/')(a,b)"),
        (op('/')(d,b),  '0.0',  "op('/')(d,b)"),
        (op('/')(b,a),  '2.0',  "op('/')(b,a)"),
        (op('/')(a,c),  'None', "op('/')(a,c)"),
        (op('/')(c,a),  'None', "op('/')(c,a)"),
        (op('/')(a,d),  'None', "op('/')(a,d)"),
    ]
    print('testes de div')
    for n in testes:printa(n, lambda x: x, True)
    testes = [
        (op('-')(a,b),  '-1'  , "op('-')(a,b)"),
        (op('-')(b,a),  '1'   , "op('-')(b,a)"),
        (op('-')(a,c),  'None', "op('-')(a,c)"),
        (op('-')(c,a),  'None', "op('-')(c,a)"),
    ]
    print('testes de menos')
    for n in testes:printa(n, lambda x: x, True)
    a = num(2)
    b = num(3)
    c = num(None)
    d = num(0)
    testes = [
        (op('^')(a,b),  '8',    "op('^')(a,b)"),
        (op('^')(d,b),  '0',    "op('^')(d,b)"),
        (op('^')(b,a),  '9',    "op('^')(b,a)"),
        (op('^')(a,c),  'None', "op('^')(a,c)"),
        (op('^')(c,a),  'None', "op('^')(c,a)"),
        (op('^')(a,d),  '1',    "op('^')(a,d)"),
    ]
    print('testes de exp')
    for n in testes:printa(n, lambda x: x, True)
    testes = [
        (op('.')(a,b),              '2.3' ,       ".(a,b)"),
        (op('.')(d,b),              '0.3' ,       ".(d,b)"),
        (op('.')(b,a),              '3.2' ,       ".(b,a)"),
        (op('.')(a,c),              'None',       ".(a,c)"),
        (op('.')(c,a),              'None',       ".(c,a)"),
        (op('.')(a,d),              '2.0' ,       ".(a,d)"),
        (op('.')(op('.')(a,b), a),  '2.32',  ".(.(a,b),a)"),
        (op('.')(op('.')(d,b), a),  '0.32',  ".(.(d,b),a)"),
        (op('.')(op('.')(b,a), a),  '3.22',  ".(.(b,a),a)"),
        (op('.')(op('.')(a,c), a),  'None',  ".(.(a,c),a)"),
        (op('.')(op('.')(c,a), a),  'None',  ".(.(c,a),a)"),
        (op('.')(op('.')(a,d), a),  '2.02',  ".(.(a,d),a)"),
    ]
    print('testes de float')
    for n in testes:printa(n, lambda x: x, True)

def test_de_eval():
    print('testes de eval:')
    testes = [
        ('/3,2',  '(True, [])'),
        ('+1,1',  '(True, [])'),
        ('+'   , '(False, [°])'),
        ('1' ,    '(True, [])'),
        ('.0',    '(True, [])'),
        ('.',    '(False, [°])'),
        (',',    '(False, [°])'),
        ('-1',    '(True, [])'),
        ('+++1,0',    '(True, [°, °])'),
        ('n1+1,1,0',    '(True, [N, N])'),
        ('+2,2,1,0',    '(True, [N, N])'),
        ('+1,0+',    '(False, [°, N, N, °])'),
    ]
    print('testes iter:')
    evalut_debb = partial(evalut, debugg=True)
    for n in testes:printa(n, evalut_debb)

    print('testes recur:')
    testes = [
        ('1+1',  '(True, [])'),
        ('1+2*3',  '(True, [])'),
        ('+' ,    '(False, [°])'),
        ('*',    '(False, [°])'),
        ('1',    '(True, [])'),
        ('1+1(+)',    '(True, [°, °, °])'),
        ('__',    '(False, [°, °])'),
        ('1+2/2*(10)',    '(True, [])'),
        ('12/1',    '(True, [])'),
        ('1+1_/2',    '(True, [°, °, N])'),
        ('()'   , '(False, [°, °])'),
        ('1(',    '(True, [°])'),
        ('1+',    '(True, [°])'),
        ('1*',    '(True, [°])'),
        ('1/',    '(True, [°])'),
        ('1-',    '(True, [°])'),
        ('1)',    '(True, [°])'),
        ('1(2)',    '(True, [°, N, °])'),
        
    ]

    for n in testes: printa(n, evalut_debb)


def printa(n, f, arg=False):

    a = str(f(n[0]))
    b = str(n[1])
    d = str(n[0])
    if arg: d = n[2]
    c= len("(False, [°, N, °, N, °]);")
    print(f"{a==b} |".rjust(7), end='')
    print(f"in:".ljust(3), end='')
    print(f"{d};".rjust(12), end='')
    print(f" e:".ljust(len(" e: ")), end='')
    print(f"{b};".rjust(c), end='')
    print(f" resposta:".ljust(len(" resposta: ")), end='')
    print(f"{a};".rjust(c))

# =================== // =============== fim  corp0  =================== // =================== #

def testes_comp():
    from os import system
    system('cls')
    if __name__ != '__main__':
        print(bb)
    print()
    print('Bom dia, teste a implementação do compilador aqui!\nEscreva abaixo:\n   >1 para testes de eval\n   >2 para testes das classes\n   >3 para você mesmo testar!')
    while True:
        s = input()
        match s:
            case '1':
                test_de_eval()
            case '2':
                test_rap()
            case '3':
                from compilador import main as tt
                tt()
        print('opções: 1,2,3')

if __name__ == '__main__':
    testes_comp()

# =================== // =============== fim  main =================== // =================== #