frase = 'eu amo programar'
frase_maiuscula = frase.upper() #coloca em maiuscula (.upper)
print(frase_maiuscula)

frase2 = 'Eu Adoro Programar'
frase_minuscula = frase.lower() #coloca em minuscula (.lower)
print(frase_minuscula)

titulo = 'a programação é divertida'
titulo_formatado = titulo.capitalize() #coloca a primeira letra em maiuscula (.capitalize)
print(titulo_formatado)

'''Às vezes, você precisa encontrar ou trocar algo em um texto. Esses métodos são como um 
"localizar e substituir" super inteligente para a sua programação. '''

frase_original = 'Eu gosto de maça, mais prefiro maça verde. '
frase_modificada = frase_original.replace('maça', 'banana') # aqui vc muda a palavra selecionada, pela a outra que vc selecionou, no caso maça e banana (.replace)
print(frase_modificada)

texto = 'aprendendo a programar em python'
palavras = texto.split() #trasforma em uma lista de string e divide a frase sempre que encontra um espaço (.split)
print(palavras)

texto1 = 'eu', 'amo', 'programaçao'
texto1_modificado = ''.join(texto1) #coloca  tudo junto (.join)
print(texto1_modificado)

