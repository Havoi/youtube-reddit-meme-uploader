import os
import tkinter
from tkinter import filedialog
from tkinter.simpledialog import askstring

def multi_filename_change():
	files = './Images'
	
	
	i = 1
	for file in os.listdir(files):
		if not file.startswith('.'):
			src = os.path.join(files, file)
			# if "thumb" in file:
			# 	os.remove(src)
				
			# else:
			dst = files + "/" + str(i) + ".png"
			os.rename(src, dst)
			print(i)
			i += 1

