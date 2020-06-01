from source.myPrint import *
import subprocess
import os

class ProjectGaussian:
	name = ""
	N = ""
	p = 0
	q = 0
	files = []
	status = False
	errorMsg = "No message"

	def __init__(self, name):
		self.name = name
		aux = name[::-1]
		t1 = aux.find('_')   # right to left
		t1 = len(aux) -1 - t1  # arreglando el puntero 
		self.shortname =  name[0:t1]
		self.N = name[t1+1]

	def getNamePosFile(self):
		aux = self.name+'+'+self.p+'.fchk'
		if aux in self.files:
			return aux
		else:
			return "False"

	def getNameNegFile(self):
		aux = self.name+'-'+self.q+'.fchk'
		if aux in self.files:
			return aux
		else:
			return "False"

	def getNameMainFile(self):
		aux = self.name+'.fchk'
		if aux in self.files:
			return aux
		else:
			return "False"

	def getP(self):
		return self.p

	def getQ(self):
		return self.q
	def getN(self):
		return self.N

	def getName(self):
		return self.name
		
	def viewName(self):
		print('Name:',self.name)

	def view(self):

		printElement('-',40)
		print('Name:',self.name)
		print('shortname:',self.shortname)
		print('N:',self.N)
		print('p:',self.p)
		print('q:',self.q)
		print('files:',self.files)
		print('status:',self.status)
		print('error:',self.errorMsg)
		printElement('-',40)
		return

	def set_P(self,name):
		aux = name[::-1]
		t1 = aux.find('+')
		t1 = len(aux)-1 - t1   # arreglo el puntero
		t2 = name.find('.')
		self.p = name[t1+1:t2]
		return

	def set_Q(self,name):
		aux = name[::-1]
		t1 = aux.find('-')
		t1 = len(aux)-1 -t1    #arreglo el puntero
		t2 = name.find('.')
		self.q = name[t1+1:t2]
		return

	def loadingFiles(self, allFilesNames):
		self.files =[]
		for i in range (len(allFilesNames)):
			if self.name in allFilesNames[i][0:len(self.name)]: 
				self.files.append(allFilesNames[i])
		#print('files:',self.files)
		return
	def checkUnique(self):
		countP= 0
		countQ= 0
		posP = 0
		posQ = 0

		for i in range (len(self.files)):
			aux = self.files[i].replace(self.name,'')
			if '+' in aux: 
				countP=countP+1
				posP = i 
			elif '-' in aux: 
				countQ=countQ+1
				posQ = i 
		#print('file:',self.files)
		#print('countP:',countP, 'countQ:',countQ)


		if (countP == 1) and (countQ == 1) and (len(self.files)== 3):
			self.status = True
			self.set_P(self.files[posP])
			self.set_Q(self.files[posQ])
			self.errorMsg = "No hay errores en los nombres de los archivos"
		elif (countP == 2) and (countQ == 0) and (len(self.files)== 3):
			self.status = False
			archivo = self.name + "-Q"
			self.errorMsg = "Hay errores, tienes 2 archivos +P (solo debes tener 1). Te falta el archivo: "+ archivo
		elif (countP == 0) and (countQ == 2) and (len(self.files)== 3):
			self.status = False
			archivo = self.name + "+P"
			self.errorMsg = "Hay errores, tienes 2 archivos -Q (solo debes tener 1). Te falta el archivo: "+ archivo
		elif (countP == 0) and (countQ == 3) and (len(self.files)== 3):
			self.status = False
			archivo1 = self.name 
			archivo2 = self.name + "+P"
			self.errorMsg = "Hay errores, tienes 3 archivos -Q (solo debes tener 1). Te faltan los archivos: "+ archivo1+' y ' + archivo2
		elif (countP == 3) and (countQ == 0) and (len(self.files)== 3):
			self.status = False
			archivo1 = self.name 
			archivo2 = self.name + "-Q"
			self.errorMsg = "Hay errores, tienes 3 archivos +P (solo debes tener 1). Te faltan los archivos: "+ archivo1+' y ' + archivo2
		elif len(self.files) == 1:
			self.status = False
			if (countP == 0) and (countQ == 0):
				archivo1 = self.name + "+P"
				archivo2 = self.name + "-Q"
				self.errorMsg = "Hay error, solo se encontro un archivo, faltan los archivos: "+ archivo1 + " y " +archivo2
			elif (countP == 0) and (countQ == 1):
				archivo1 = self.name 
				archivo2 = self.name + "+P"
				self.errorMsg = "Hay error, solo se encontro un archivo, faltan los archivos: "+ archivo1 + " y " +archivo2
			elif (countP == 1) and (countQ == 0):
				archivo1 = self.name 
				archivo2 = self.name + "+Q"
				self.errorMsg = "Hay error, solo se encontro un archivo, faltan los archivos: "+ archivo1 + " y " +archivo2

		elif len(self.files) == 2:
			self.status = False
			if (countP == 0) and (countQ == 1):
				archivo = self.name  + "+P"
				self.errorMsg = "Hay error, faltan el archivo: "+ archivo 
			elif (countP == 1) and (countQ == 0):
				archivo = self.name  + "-Q"
				self.errorMsg = "Hay error, faltan el archivo: "+ archivo 
			elif (countP == 1) and (countQ == 1):
				archivo = self.name 
				self.errorMsg = "Hay error, faltan el archivo: "+ archivo 
			elif (countP == 2) and (countQ == 0):
				archivo1 = self.name 
				archivo2 = self.name + "-Q"
				self.errorMsg = "Hay error, tienes 2 archivos +P (solo debes tener 1). Te faltan los archivos: "+ archivo1 + " y " +archivo2
			elif (countP == 0) and (countQ == 2):
				archivo1 = self.name 
				archivo2 = self.name + "+P"
				self.errorMsg = "Hay error, tienes 2 archivos -Q (solo debes tener 1). Te faltan los archivos: "+ archivo1 + " y " +archivo2
		elif len(self.files) > 3:
			self.status = False
			archivo1 = self.name 
			archivo2 = self.name + "+P"
			archivo3 = self.name + "-Q"
			self.errorMsg = "Hay errores, se encontraron multiples archivos, solo debes tener 3:"+archivo1+', '+archivo2 +' y '+archivo3
		
		return

def removeFiles(filesList):
    filesList.insert(0,'rm')
    #printElementName('Delete','*',40)
    query = ' '.join(filesList)
    #print query
    try:
	res = subprocess.Popen(filesList,stdout=subprocess.PIPE,stderr=subprocess.PIPE);
	output,error = res.communicate()
	if output:
	    print "Output Code:",res.returncode
	    print "Succefull:",output
	    printElement('*',40)
	    return 0
	if error:
	    print "Output Code:",res.returncode
	    print "Error: ",error.strip()
	    printElement('*',40)
	    return 1
    except OSError as e:
	print "Output Code: ",e.errno
	print "Error:",e.strerror
	print "ErrorFile: ",e.filename
	printElement('*',40)
	return 2
    except:
	print "Error:", sys.exc_info()[0]
	printElement('*',40)
	return 3
    #printElement('*',40)
    
    

    
def checker(message):
    if message == "":
	inputt = raw_input()
    else:
	inputt = raw_input(message+'\n')
    try:
	return int(inputt)
    except ValueError:
	print "Error!, Enter a number!"
	return checker("")


def edit(fileName, line1, line2):
    with open(fileName) as f:
	lines = f.readlines() #read
	f.close()

    lines[0] = line1 +'\n'
    lines[1] = line2 +'\n'
				
    with open(fileName, "w") as f:
	f.writelines(lines) #write back
    return 0

