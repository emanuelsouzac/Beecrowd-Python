def mdc(a, b):
    while 1:
        resto = a % b
        if resto == 0:
            break
        a = b
        b = resto
    print(b)

n = int(input())

for i in range(0, n):
    qtd = input()
    qtd = qtd.split()
    fig1 = int(qtd[0])
    fig2 = int(qtd[1])
    mdc(fig1, fig2)
