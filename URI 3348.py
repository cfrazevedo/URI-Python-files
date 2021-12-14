"""
URI (BEE) 3348 - NÃO RESOLVIDO - TIME LIMIT ERROR

Não sei como resolve este exercício sem analisar todos os números de Merlin até K.
O código abaixo chega nos resultados esperados, entretanto gasta muito tempo e
memória (Time Limit Error). Realmente ja demora muito tempo quando K = 12, e esse tempo
aumenta com o valor de K.Este tempo já está otimizado, pois o código não analiza números
que inicialmente caem nas aranhas Nesticodes (linhas 23-24).

Você pode resolver este problema associando diretamente o número de N com o número de K,
sem analisar cada valor até K, ou seja, não resolve o problema. Deixarei este código
abaixo marcados com cerquilha (#), sem codificar (linhas 41-80). Como o número máximo
de N é 19, fica fácil receber o aceite do julgamento apenas com a associação entre os
números N e K.'
"""

n = int(input())
s = n * 'N'
s += n * 'L'
num = len(s) // 2 + 1
resp = False
while not resp:
    while num % len(s) != 0 and num % len(s) <= len(s) / 2:
        num += 1
    s1 = s
    np = num
    while 'L' in s1:
        cr = s1[(np % len(s1)) - 1]
        if cr == 'L':
            if np % len(s1) == 0:
                np = num
            else:
                np = num - (len(s1) - (np % len(s1)))
            s1 = s1[:-1]
        elif cr == 'N':
            num += 1
            break
        if not 'L' in s1:
            print(num)
            resp = True

# n = int(input())
# if n == 1:
#     print(2)
# elif n == 2:
#     print(7)
# elif n == 3:
#     print(5)
# elif n == 4:
#     print(30)
# elif n == 5:
#     print(169)
# elif n == 6:
#     print(441)
# elif n == 7:
#     print(1872)
# elif n == 8:
#     print(7632)
# elif n == 9:
#     print(1740)
# elif n == 10:
#     print(93313)
# elif n == 11:
#     print(459901)
# elif n == 12:
#     print(1358657)
# elif n == 13:
#     print(2504881)
# elif n == 14:
#     print(13482720)
# elif n == 15:
#     print(25779600)
# elif n == 16:
#     print(68468401)
# elif n == 17:
#     print(610346880)
# elif n == 18:
#     print(1271932200)
# elif n == 19:
#     print(327280800)