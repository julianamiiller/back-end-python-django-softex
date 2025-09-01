lado_a = float(input("Digite o lado A: "))
lado_b = float(input("Digite o lado B: "))
lado_c = float(input("Digite o lado C: "))

if lado_a <=0 or lado_b <=0 or lado_c <=0:
    print("Todos os lados precisam ser positivos. Tente novamente. ")

elif lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print("Triângulo formado. ")

else:
    print("Os lados não podem se transformar em um triângulo. ")