vitoria_lv1 = 0 
vitoria_lv2 = 0
for i in range(2):
    if i  == 0:
        print("Perguntas de adição: ")
        for j in range(1):
            resposta = int(input("1) quanto é 2+2 =  "))
            if resposta == 4:
                vitoria_lv1 += 1
        for k in range(1):
            resposta = int(input("2) quanto é 3+3 =  "))
            if resposta == 6:
                vitoria_lv1 += 1
        for l in range(1):
            resposta = int(input("3) quanto é 7 + 12 =  "))
            if resposta == 19:
                vitoria_lv1 += 1
    if i == 1:
        print("Perguntas de subtração: ")
        for m in range (1):
            resposta = int(input("1) quanto é 8-5 =  "))
            if resposta == 3:
                vitoria_lv1 += 1
        for n in range(1):
            resposta = int(input("2) quanto é 24-7 =  "))
            if resposta == 17:
                vitoria_lv1 += 1
        for o in range(1):
            resposta = int(input("3) quanto é 12-4 =  "))
            if resposta == 8:
                vitoria_lv1 += 1

if 4 < vitoria_lv1 <= 6:
    print("Você passou para o proximo nivel")

    print("Bem vindo ao nivel 02")
    
    for i in range(2):
        if i  == 0:
            print("Perguntas de multiplicação: ")
            for j in range(1):
                resposta = int(input("1) quanto é 2 x 7 =  "))
                if resposta == 14:
                    vitoria_lv2 += 1
            for k in range(1):
                resposta = int(input("2) quanto é 3 X 3 =  "))
                if resposta == 9:
                    vitoria_lv2 += 1
            for l in range(1):
                resposta = int(input("3) quanto é 7 X 12 =  "))
                if resposta == 84:
                    vitoria_lv2 += 1
        if i == 1:
            print("Perguntas de divisão: ")
            for m in range (1):
                resposta = int(input("1) quanto é 8 / 4 =  "))
                if resposta == 2:
                    vitoria_lv2 += 1
            for n in range(1):
                resposta = int(input("2) quanto é 27 / 3 =  "))
                if resposta == 9:
                    vitoria_lv2 += 1
            for o in range(1):
                resposta = int(input("3) quanto é 64 / 8 =  "))
                if resposta == 8:
                    vitoria_lv2 += 1
                    
if 4 < vitoria_lv2 <= 6:
    print("Você é o campeão")
else:
    print("Game over ")    

