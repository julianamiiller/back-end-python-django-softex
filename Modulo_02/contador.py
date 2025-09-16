def contar_palavras(frase):
   
    return len(frase.split())

def contar_vogais(frase):
  
    vogais = "aeiou"
    contador = 0
    for letra in frase.lower():
        if letra in vogais:
            contador += 1
    return contador

def contar_consoantes(frase):

    vogais = "aeiou"
    contador = 0
    for letra in frase.lower():
        if letra.isalpha() and letra not in vogais:
            contador += 1
    return contador

def verificar_palindromo(frase):
 

    limpa = ""
    for letra in frase.lower():
        if letra.isalpha():
            limpa += letra
    return limpa == limpa[::-1]

frase = input("Digite uma frase para analisar: ")

palavras = contar_palavras(frase)
vogais = contar_vogais(frase)
consoantes = contar_consoantes(frase)
palindromo = verificar_palindromo(frase)

print("\n--- Resumo da Análise ---")
print(f"Palavras: {palavras}")
print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")
print(f"É um palíndromo? {'Sim' if palindromo else 'Não'}")
