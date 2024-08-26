#Phytom velocidade media
# 
#  = int(input("Digite o numero de rotas: "))
ro = int(input("Quantas rotas: "))
n = 1
l = list (range(n,ro +1))

for qr in l: 
    o = "Rota"
   

    rg = [f"{o} {i}" for i in range(1, ro + 1)]
    t = float(input("Quantos trechos: "))
    c = float(input("Qual a distancia: "))
    vm = float(input("Qual a velocidade media: "))
    print(str(rg))