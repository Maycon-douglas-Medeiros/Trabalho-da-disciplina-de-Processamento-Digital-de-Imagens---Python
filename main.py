import imageio as img
import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------------------------------------------------
#Função que abre o aquivo texto_entrada.txt e pega o Ascii de cada caractere e tranforma em seu respectivo binário(Bin)
#----------------------------------------------------------------------------------------------------------------------

def pegaFrase():
	bitsP = 0
	global Bin
	Bin = list()
	Ascii = list()
	frase = ""

	texto_entrada = open("texto_entrada.txt", "r")

	letras = texto_entrada.readlines()

	for x in letras:
		frase = x

	for x in range(len(frase)):
		Ascii.append(ord(frase[x]))
		Bin.append(format(Ascii[x], 'b'))
		bitsP += len(Bin[x])

	texto_entrada.close()
	return Bin, bitsP
#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------
#Pega os valores RGB dos pixel da imagem e converte para seu respectivo binário(rgb), após isso calcula e modifica os
#pixels da imagem e salva a mesma como 'imagem_saida.png'
#----------------------------------------------------------------------------------------------------------------------
def codificar():
	global BitsP
	sizeIm = 0
	BitsP = 0

	rgb = list()
	RGB = list()
	Bin = list()

	Bin, BitsP = pegaFrase()

	f = img.imread('imagem_entrada.png')

	sizeIm = (f.shape[1]) * 3

	if(sizeIm < BitsP):
		print("Mensagem muito grande para a Imagem!")
		return 0

	print("Bin:", Bin)
	x = 0
	
	while(len(rgb) < BitsP):
		rgb.append(format(f[0, x, 0], 'b'))
		if(len(rgb) < BitsP):
			rgb.append(format(f[0, x, 1], 'b'))
			rgb.append(format(f[0, x, 2], 'b'))

		x += 1
	print("----------------------------------------------------------------------------------------------------------------------")
	print("RGB: ",rgb)
	print("----------------------------------------------------------------------------------------------------------------------")
	k = l = 0
	for i in range(0, len(rgb)):
		rgb2 = ""
		for j in range(0, len(rgb[i])-1):
			rgb2 += rgb[i][j]
		
		if(l >= len(Bin[k])):
			l = 0
			k += 1
		if(k < len(Bin)):
			rgb2 += Bin[k][l]
			l += 1

		rgb[i] = rgb2

	print("----------------------------------------------------------------------------------------------------------------------")
	print("RGB Altearado: ",rgb)
	print("----------------------------------------------------------------------------------------------------------------------")

	for x in range(0, len(rgb)):
		RGB.append(int(rgb[x], 2))
	
	j = 0
	i = 1
	
	if((len(RGB)%3) == 0):
		for x in range(0, len(RGB), 3):
			f[0:1 , j:i, [0, 1, 2]] = RGB[x], RGB[x+1], RGB[x+2]
			print(RGB[x], RGB[x+1], RGB[x+2])
			j += 1
			i += 1
	else:
		for x in range(0, len(RGB), 3):
			if(x+2 < len(RGB)):
				f[0:1 , j:i, [0, 1, 2]] = RGB[x], RGB[x+1], RGB[x+2]
				print(RGB[x], RGB[x+1], RGB[x+2])
			else:
				f[0:1 , j:i, [0]] = RGB[x]
				print(RGB[x])
			j += 1
			i += 1

	img.imwrite('imagem_saida.png', f)
#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------
#Decodificar
#----------------------------------------------------------------------------------------------------------------------
def decodificar():
	fraseB = list()
	f2 = img.imread('imagem_saida.png')

	x = 0
	while(len(fraseB) < BitsP):
		fraseB.append(format(f2[0, x, 0], 'b'))
		if(len(fraseB) < BitsP):
			fraseB.append(format(f2[0, x, 1], 'b'))
			fraseB.append(format(f2[0, x, 2], 'b'))

		x += 1

	frases = list()
	frase = ""
	aux = 0
	aux2 = len(Bin[aux])-1

	for i in range(0, len(fraseB)):
		if(aux2 < i):
			print(frase)
			frases.append(frase)
			frase = ""
			aux += 1
			
			if(aux < len(Bin)):
				aux2 = aux2 + len(Bin[aux])
				
			
		for j in range(0, len(fraseB[i])):
			if(j == len(fraseB[i])-1):
				frase += fraseB[i][j]
	
	if(len(frase) > 1):
		frases.append(frase)
	
	frase = ""

	print(Bin)
	print(len(Bin))
	print(frases)
	print(len(frases))

	for x in range(0, len(frases)):
		frases[x] = int(frases[x], 2)
		frase += chr(frases[x])
	
	print(frases)
	arquivo = open('texto_saida.txt', 'w')
	arquivo.write(frase)
	arquivo.close()

	plt.imshow(f2)
	plt.show()
#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------
codificar()
decodificar()
#----------------------------------------------------------------------------------------------------------------------