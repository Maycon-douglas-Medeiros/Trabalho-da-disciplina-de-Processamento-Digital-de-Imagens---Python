import imageio as img
import numpy as np
import matplotlib.pyplot as plt

Bin = list()
rgb = list()

def pegaFrase():
	
	texto_entrada = open("texto_entrada.txt", "r")

	Ascii = list()
	frase = ""

	letras = texto_entrada.readlines()

	for x in letras:
		frase = x

	for x in range(len(frase)):
		Ascii.append(ord(frase[x]))
		Bin.append(format(Ascii[x], 'b'))

	texto_entrada.close()

	return Bin

def codificar():

	f = img.imread('imagem_entrada.png')
	#print(f.shape[0])

	rgb.append(bin(f[0, 0, 0]))
	rgb.append(bin(f[20, 30, 1]))
	rgb.append(bin(f[40, 50, 2]))

	print(rgb)

	# y   x   r g b
	

	print(f[0, 0, 0])
	print(f[20, 30, 1])
	print(f[40, 50, 2])
	
	#img.imwrite('imagem_saida.png', f[0:1 , 0:1])
	plt.imshow(f)
	plt.show()

codificar()
