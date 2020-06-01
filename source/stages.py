import subprocess
import sys
from source.myPrint import *
import os
import curses
from source.myCurses import *

class Stage1:
	status = False
	log= "No message"
	def __init__(self,inputFile,Y,X):
	    self.inputFile = inputFile
	    self.outputFile = self.inputFile.replace(".fchk", "_den.cub")
	    self.Y = str(Y)
	    self.X = str(X)
	    self.queryCMD = ["nohup", "cubegen" , self.X , "Density=SCF", self.inputFile , self.outputFile , "-" + self.Y, "h" ]
	    self.query = ' '.join(self.queryCMD) 

	def getOutputFile(self):
	    return self.outputFile
		
	def getStatus(self):
	    return self.status

	def view(self):
	    printElementName('Resume','-',40)
	    print('InputFile:',self.inputFile)
	    print('OutputFile:',self.outputFile)
	    print('Y:',self.Y)
	    print('X:',self.X)
	    print('Status:',self.status)
	    print('Log:',self.log)
	    printElement('-',40)
	    return 0
	    
	def viewQuery(self):
	    printElementName('Working','*',40)
	    print self.query
	    return 0
	    
	def viewQueryX(self,screen):
	    printCenter('Working ...',screen)
	    printFooter(self.query,screen)
	    screen.refresh()
	    return 0
		
	def viewX(self,screen):
	    printCenter(self.log,screen)
	    screen.refresh() 
	    return 0
	
	def cubegen(self):
	    try:
		res = subprocess.Popen(self.queryCMD,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		output,error = res.communicate()

		if output:								# funciona el programa
		    self.status = True
		    self.log = "Successful :)"
		    return 0
		if error:
		    self.outputFile = ""
		    self.status = False
		    self.log = error.strip()
		    return 1
	    except OSError as e:
		self.outputFile = ""
		self.status = False
		self.log = e.strerror
		return 2
	    except:
		self.outputFile = ""
		self.status = False
		self.log = sys.exc_info()[0]
		return 3

class Stage2:
	status = False
	log= "No message"
	def __init__(self,inputFile1,inputFile2,X):
	    self.inputFile1 = inputFile1
	    self.outputFile = self.inputFile1.replace(".fchk", "_den.cub")
	    self.inputFile2 = inputFile2
	    self.X = str(X)
	    self.queryCMD = ["nohup", "cubegen" , self.X , "Density=SCF", self.inputFile1 , self.outputFile , "-1", "h",  self.inputFile2 ]
	    self.query = ' '.join(self.queryCMD)

	def getOutputFile(self):
	    return self.outputFile
		
	def getStatus(self):
	    return self.status

	def view(self):
	    printElementName('Resume','-',40)
	    print('InputFile1:',self.inputFile1)
	    print('InputFile2:',self.inputFile2)
	    print('OutputFile:',self.outputFile)
	    print('X:',self.X)
	    print('Status:',self.status)
	    print('Log:',self.log)
	    printElement('-',40)
	    return 0
		
	def viewQuery(self):
	    printElementName('Working','*',40)
	    print self.query
	    return 0
    
	def viewQueryX(self,screen):
	    printCenter('Working ...',screen)
	    printFooter(self.query,screen)
	    screen.refresh()
	    return 0
	
	def viewX(self,screen):
	    printCenter(self.log,screen)
	    screen.refresh() 
	    return 0

	def cubegen(self):
	    try:
		res = subprocess.Popen(self.queryCMD,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		output,error = res.communicate()
		if output:
		    self.status = True
		    self.log = "Successful :)"
		    return 0
		if error:
		    self.outputFile = ""
		    self.status = False
		    self.log = error.strip()
		    return 1
	    except OSError as e:
		self.outputFile = ""
		self.status = False
		self.log = e.strerror
		return 2
	    except:
		self.outputFile = ""
		self.status = False
		self.log = sys.exc_info()[0]
		return 3

class Stage31:
	status = False
	log= "No message"
	def __init__(self,inputFile1,inputFile2,outputFile):
	    self.inputFile1 = inputFile1
	    self.inputFile2 = inputFile2
	    self.outputFile = outputFile
	    
	    # query 
	    self.cmd_suppression    = "cubman"
	    action                  = 'SU'
	    firstInput              =  self.inputFile1
	    isFormattedFirstInput   = "yes"
	    secondInput             =  self.inputFile2
	    isFormattedSecondInput  = "yes"
	    shouldItBeFormatted     = "yes"
	    
	    self.queryCMD       = '\n'.join([action, firstInput,isFormattedFirstInput,secondInput,isFormattedSecondInput,outputFile,shouldItBeFormatted ])
	    self.query    	= ' '.join([self.cmd_suppression ,action, firstInput,isFormattedFirstInput,secondInput,isFormattedSecondInput,outputFile,shouldItBeFormatted  ])

	def getOutputFile(self):
	    return self.outputFile
	
	def getStatus(self):
	    return self.status

	def view(self):
	    printElementName('Resume','-',40)
	    print('InputFile1:',self.inputFile1)
	    print('InputFile2:',self.inputFile2)
	    print('OutputFile:',self.outputFile)
	    print('Status:',self.status)
	    print('Log:',self.log)
	    printElement('-',40)
	    return 0
		
	def viewQuery(self):
	    printElementName('Working','*',40)
	    print self.query
	    return 0
	    
    
	def viewQueryX(self,screen):
	    printCenter('Working ...',screen)
	    printFooter(self.query,screen)
	    screen.refresh()
	    return 0

	def viewX(self,screen):
	    printCenter(self.log,screen)
	    screen.refresh() 
	    return 0
	
	def cubman(self):
	    try:
		res = subprocess.Popen(self.cmd_suppression ,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		output,error = res.communicate(self.queryCMD)
		if output:
		    self.status = True
		    self.log = "Successful :)"
		    return 0
		if error:
		    self.outputFile = ""
		    self.status = False
		    self.log = error.strip()
		    return 1
	    except OSError as e:
		self.outputFile = ""
		self.status = False
		self.log = e.strerror
		return 2
	    except:
		self.outputFile = ""
		self.status = False
		self.log = sys.exc_info()[0]
		return 3

class Stage32:
	status = False
	log= "No message"
	def __init__(self,inputFile,outputFile,factor):
	    self.inputFile  = inputFile
	    self.outputFile = outputFile
	    self.factor     = factor
	    
	    # query 
	    self.cmd_suppression    	= "cubman"
	    action 			= 'SC'
	    firstInput 			=  self.inputFile
	    isFormattedFirstInput	= "yes"
	    outputFile			= self.outputFile	
	    shouldItBeFormatted		= "yes"
	    scale 			= str( round( (float(1)/float(self.factor) ), 10))
	    
	    self.queryCMD       = '\n'.join([action, firstInput,isFormattedFirstInput,outputFile,shouldItBeFormatted,scale])
	    self.query    	= ' '.join([self.cmd_suppression ,action, firstInput,isFormattedFirstInput,outputFile,shouldItBeFormatted,scale ])

	def getOutputFile(self):
	    return self.outputFile
	
	def getStatus(self):
	    return self.status

	def view(self):
	    printElementName('Resume','-',40)
	    print('InputFile:',self.inputFile)
	    print('OutputFile:',self.outputFile)
	    print('Status:',self.status)
	    print('Log:',self.log)
	    printElement('-',40)
	    return 0
		
	def viewQuery(self):
	    printElementName('Scale','*',40)
	    print self.query
	    return 0
	    
    
	def viewQueryX(self,screen):
	    printCenter('Scale ...',screen)
	    printFooter(self.query,screen)
	    screen.refresh()
	    return 0

	def viewX(self,screen):
	    printCenter(self.log,screen)
	    screen.refresh() 
	    return 0
	
	def cubman(self):
	    try:
		res = subprocess.Popen(self.cmd_suppression ,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		output,error = res.communicate(self.queryCMD)
		if output:
		    self.status = True
		    self.log = "Successful :)"
		    return 0
		if error:
		    self.outputFile = ""
		    self.status = False
		    self.log = error.strip()
		    return 1
	    except OSError as e:
		self.outputFile = ""
		self.status = False
		self.log = e.strerror
		return 2
	    except:
		self.outputFile = ""
		self.status = False
		self.log = sys.exc_info()[0]
		return 3
