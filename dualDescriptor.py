import curses
from source.myCurses import *

import os

from source.filesFunc import *
from source.stages import *
from source.myPrint import *
import sys


if (len(sys.argv)-1 ==0 ):
    vision = True
else:
    if (sys.argv[1] == 'more'):
	vision = False
    else:
	vision = True
myCmd = os.popen('ls | grep "\.fchk$"').read()
allFilesNames = myCmd.split()

nameProgram = 'Dual Descriptor'


if vision:

    screen = curses.initscr() # set the style

    curses.wrapper(do_it)    # pantalla de Inicio


    printCenter("WELLCOME TO "+nameProgram.upper(),screen)
    printFooterLeft("Version: 1.1",screen)
    printFooterRight("2020 ",screen)
    screen.refresh()

    curses.napms(3000)
    
    if len(allFilesNames) == 0:
	screen.clear()
        printCenter("No Files *.fchk :(",screen)
        screen.refresh()
        curses.napms(3000)
        curses.endwin()
        sys.exit(0)   # salir sin errores

else:
    printElement('-',40)
    printElementName(nameProgram.upper(),'-',40)
    printElement('-',40)
    if len(allFilesNames) == 0:
	printElementName('No Files *.fchk','=',40)
	sys.exit(0)   # salir sin errores


# List for the project

allProjectName =[]                  # Project List Name
allBadFilesName = []                # Bad Project List Name

listProjectGauss = []               # List Project Gauss 
listProjectGaussIncomplete = []     # List Incomple Project Gauss 


filesTempList = []                  # FilesTemp List Project Gaussian in working
filesOutList = []                   # FilesOutput  List Project Gaussian in working

# Load List All  Project & All Bad 

for i in range (len(allFilesNames)):
    name = allFilesNames[i]
    name = name[::-1]
    t1 = name.find('_')  # encontrar '_' right to left
    if t1 != -1:
	t1 = len(name)-1 - t1      # arreglo el puntero 
	aux = allFilesNames[i][0:t1+2]
	if not(aux in allProjectName):
	    allProjectName.append(aux)
    else:
	allBadFilesName.append(allFilesNames[i])

# load the project names

for i in range (len(allProjectName)):
    a = ProjectGaussian(allProjectName[i])
    a.loadingFiles(allFilesNames)
    a.checkUnique()
    if a.status == True :
	listProjectGauss.append(a)
    else:
	listProjectGaussIncomplete.append(a) 


# View List of Projects

if len(listProjectGauss)!= 0:
    if vision:
	screen.clear()
	printTop("Project List",screen)
	aux = ""
	for i in range (len(listProjectGauss)):
	    aux=str(i)+': '+listProjectGauss[i].getName()
	    printCenterPlus(aux,screen,i)
	screen.refresh()
    else:
	printElementName('Project List',' ',40)
	for i in range (len(listProjectGauss)):
	    print(i,listProjectGauss[i].getName())
	    #print('P',listProjectGauss[i].getP())
	    #print('Q',listProjectGauss[i].getQ())
	    #printElement('*',40)
	printElement('-',40)
	#print('AllFilesNames')
	#print(allFilesNames)
	#print('AllBadFilesNames')
	#print(allBadFilesName)           # Bad Project List Name
	
	#print('listoProjectGaussIncomplete')
	#for i in range (0,len(listProjectGaussIncomplete)):
	    #print(i,listProjectGaussIncomplete[i].getName())
else:
    if vision:
	screen.clear()
	printCenter("No Project Gaussian :(",screen)
	screen.refresh()
	curses.napms(2000)
	curses.endwin()
    else:
	printElementName('No Project Gaussian :(','=',40)
    sys.exit(0)   # salir sin errores


# Choose the project for work

inputFile = 0 
flag = False

while True:
    if vision:
	answer = my_int_input('Choose Project',screen,flag)
    else:
	answer = checker('Choose Project')

    if ( answer< 0) or (answer > len(listProjectGauss)-1):
	if vision:
	    flag = True
	else:
	    print('Action not valid: ', answer)
    else:
	inputFile = listProjectGauss[answer].getNamePosFile()
	break

nproject = answer

# Choose the cores

X = 0 
flag = False

if vision:
    screen.clear()
    
    printTop("Number Cores (Recomended 4)",screen)
    printCenter('Options: 1,2,3 or 4 Cores',screen)
    
else:
    printElementName('Number Cores X','-',40)
    print('Recommended 4, but you can choose 1, 2 or 3.')


while True:
    if vision:
	answer = my_int_input('Insert Cores',screen,flag)
    else:
	answer = checker('Insert Cores')

    if ( answer< 1) or (answer > 4):
	if vision:
	    flag = True
	else:
	    print('Action not valid: ', answer)
    else:
	X = answer
	break
	
# Choose Resolution

Y = 0 
flag = False

if vision:
    screen.clear()
    
    printTop("Resolution (Recomended 3)",screen)
    printCenter('Options: low = 2, Med = 3, High = 4',screen)
    
else:
    printElementName('Resolution Y','-',40)
    print('Recommended 3, but you can choose:')
    print ('Low    : 2')
    print ('Medium : 3')
    print ('High   : 4')


while True:
    if vision:
	answer = my_int_input('Insert Resolution ',screen,flag)
    else:
	answer = checker('Insert Resolution ')

    if ( answer< 2) or (answer > 4):
	if vision:
	    flag = True
	else:
	    print('Action not valid: ', answer)
    else:
	Y = answer
	break



# Start to working

# Step 1

large = '6'

if vision:
    screen.clear()
    printTop('Step 1/'+large, screen)
    screen.refresh()
else:
    printElementName('Step 1/'+large,'=',40)

step1 = Stage1(inputFile,Y,X)

if vision:
    step1.viewQueryX(screen)
else:
    step1.viewQuery()
    
step1.cubegen()

if vision:
    step1.viewX(screen)
else:
    step1.view()

if step1.getStatus() == False:
    if vision:
	printCenter('Error No OutputFile',screen)
	curses.napms(3000)
	curses.endwin()
    else:
	printElementName('Error No OutputFile','=',40)
    sys.exit(0)   # salir sin errores


filesTempList.append(step1.getOutputFile())



# Step 2

if vision:
    curses.napms(2000)
    screen.clear()
    printTop('Step 2/'+large,screen)
    screen.refresh()
else:
    printElementName('Step 2/'+large,'=',40)

inputFile1 = listProjectGauss[nproject].getNameMainFile()
inputFile2 = step1.getOutputFile()

step2 = Stage2(inputFile1,inputFile2,X)

if vision:
    step2.viewQueryX(screen)
else:
    step2.viewQuery()
    
step2.cubegen()

if vision:
    step2.viewX(screen)
else:
    step2.view()

if step2.getStatus() == False:
    if vision:
	printCenter('Error No OutputFile',screen)
	curses.napms(3000)
	curses.endwin()
    else:
	printElementName('Error No OutputFile','=',40)
    sys.exit(0)   # salir sin errores

filesTempList.append(step2.getOutputFile())

# Step3

if vision:
    curses.napms(2000)
    screen.clear()
    printTop('Step 3/'+large, screen)
    screen.refresh()
else:
    printElementName('Step 3/'+large, '=',40)

inputFile1 = listProjectGauss[nproject].getNameNegFile()
inputFile2 = step1.getOutputFile()

step3 = Stage2(inputFile1,inputFile2,X)

if vision:
    step3.viewQueryX(screen)
else:
    step3.viewQuery()
    
step3.cubegen()

if vision:
    step3.viewX(screen)
else:
    step3.view()

if step3.getStatus() == False:
    if vision:
	printCenter('Error No OutputFile',screen)
	curses.napms(3000)
	curses.endwin()
    else:
	printElementName('Error No OutputFile','=',40)
    sys.exit(0)   # salir sin errores

filesTempList.append(step3.getOutputFile())



# Step4

if vision:
    curses.napms(2000)
    screen.clear()
    printTop('Step 4/'+large,screen)
    screen.refresh()
else:
    printElementName('Step 4/'+large,'=',40)

inputFile1 = step1.getOutputFile()
inputFile2 = step2.getOutputFile()

factor = int(listProjectGauss[nproject].getP())

t1 = inputFile1.find('_')

if (factor == 1):
    outputFile = inputFile1[0:t1]+"_F+F_FDA.cub"
else:
    outputFile = inputFile1[0:t1]+"_pro_F+F_FDA.cub"

step4 = Stage31(inputFile1,inputFile2,outputFile)

if vision:
    step4.viewQueryX(screen)
else:
    step4.viewQuery()
    
step4.cubman()

if vision:
    step4.viewX(screen)
else:
    step4.view()

if step4.getStatus() == False:
    if vision:
	printCenter('Error No OutputFile',screen)
	curses.napms(3000)
	curses.endwin()
    else:
	printElementName('Error No OutputFile','=',40)
    sys.exit(0)   # salir sin errores

if factor == 1:
    filesOutList.append(step4.getOutputFile())
else:
    filesTempList.append(step4.getOutputFile())
    
    

    
if factor > 1:


    inputFile  = step4.getOutputFile()
    outputFile = inputFile1[0:t1]+"_F+F_FDA.cub"

    step42 = Stage32(inputFile,outputFile,factor)

    if vision:
	curses.napms(2000)
	screen.clear()
	printTop('Step 4/'+large,screen)
	screen.refresh()
	step42.viewQueryX(screen)
    else:
	step42.viewQuery()
    
    step42.cubman()

    if vision:
	curses.napms(2000)
	step42.viewX(screen)
    else:
	step42.view()

    if step42.getStatus() == False:
	if vision:
	    printCenter('Error No OutputFile',screen)
	    curses.napms(3000)
	    curses.endwin()
	else:
	    printElementName('Error No OutputFile','=',40)
	sys.exit(0)   # salir sin errores

    filesOutList.append(step42.getOutputFile())




# Step5

if vision:
    curses.napms(2000)
    screen.clear()
    printTop('Step 5/'+large,screen)
    screen.refresh()
else:
    printElementName('Step 5/'+large,'=',40)

inputFile1 = step2.getOutputFile()
inputFile2 = step3.getOutputFile()

factor = int(listProjectGauss[nproject].getQ())

t1 = inputFile1.find('_')

if (factor == 1):
    outputFile = inputFile1[0:t1]+"_F-F_FDA.cub"
else:
    outputFile = inputFile1[0:t1]+"_pro_F-F_FDA.cub"

step5 = Stage31(inputFile1,inputFile2,outputFile)

if vision:
    step5.viewQueryX(screen)
else:
    step5.viewQuery()
    
step5.cubman()

if vision:
    step5.viewX(screen)
else:
    step5.view()

if step5.getStatus() == False:
    if vision:
	printCenter('Error No OutputFile',screen)
	curses.napms(3000)
	curses.endwin()
    else:
	printElementName('Error No OutputFile','=',40)
    sys.exit(0)   # salir sin errores

if factor == 1:
    filesOutList.append(step5.getOutputFile())
else:
    filesTempList.append(step5.getOutputFile())
    
    

    
if factor > 1:


    inputFile  = step5.getOutputFile()
    outputFile = inputFile1[0:t1]+"_F-F_FDA.cub"

    step52 = Stage32(inputFile,outputFile,factor)

    if vision:
	curses.napms(2000)
	screen.clear()
	printTop('Step 5/'+large,screen)
	screen.refresh()
	step52.viewQueryX(screen)
    else:
	step52.viewQuery()
    
    step52.cubman()

    if vision:
	curses.napms(2000)
	step52.viewX(screen)
    else:
	step52.view()

    if step52.getStatus() == False:
	if vision:
	    printCenter('Error No OutputFile',screen)
	    curses.napms(3000)
	    curses.endwin()
	else:
	    printElementName('Error No OutputFile','=',40)
	sys.exit(0)   # salir sin errores

    filesOutList.append(step52.getOutputFile())


# Step6

if vision:
    curses.napms(2000)
    screen.clear()
    printTop('Step 6/'+large,screen)
    screen.refresh()
else:
    printElementName('Step 6/'+large,'=',40)



inputFile1 = filesOutList[0]
inputFile2 = filesOutList[1]

outputFile = inputFile1.replace("_F+F_FDA.cub", "_DD_FDA.cub")

step6 = Stage31(inputFile1,inputFile2,outputFile)

if vision:
    step6.viewQueryX(screen)
else:
    step6.viewQuery()
    
step6.cubman()

if vision:
    step6.viewX(screen)
else:
    step6.view()

if step6.getStatus() == False:
    if vision:
	printCenter('Error No OutputFile',screen)
	curses.napms(3000)
	curses.endwin()
    else:
	printElementName('Error No OutputFile','=',40)
    sys.exit(0)   # salir sin errores


filesOutList.append(step6.getOutputFile())


#Edit Output Files

line2_S31 = 'Nucleophilic Fukui function FDA' 
line2_S32 = 'Electrophilic Fukui function FDA'
line2_S4 = 'Dual descriptor or second order Fukui function FDA'

edit(filesOutList[0],filesOutList[0],line2_S31)
edit(filesOutList[1],filesOutList[1],line2_S32)
edit(filesOutList[2],filesOutList[2],line2_S4)

# Delete Temp Files

if vision:
    curses.napms(2000)
    screen.clear()
    
    printCenter("Temporal Files",screen)
    
    
else:
    printElementName('Temporal Files','-',40)

while True:
    if vision:
	answer = str(my_raw_input("Delete y/n ? " ,screen))
	
    else:
	answer = str(raw_input("Delete y/n: ?\n"))

    if answer == 'y':
	removeFiles(filesTempList)
	filesTempList = []
	break
    elif answer == 'n':
	break
    else:
	if vision:
	    printFooter('Action not valid: ' +  answer ,screen)
	else:
	    print('Action not valid: ', answer)


# print Results 



if vision:

    curses.napms(2000)
    screen.clear()
    
    printTop("Final Files",screen)
    printCenter(' '.join(filesOutList),screen)
    
    if (len(filesTempList) != 0):
	printBottom('Temporal Files',screen)
	printFooter(' '.join(filesTempList),screen)

    screen.getch()
    curses.endwin()
    
else:
    printElementName('Final Files','=',40)
    print(filesOutList)
    if (len(filesTempList) != 0):
	printElementName('Temporal Files','=',40)
    	print(filesTempList)



    
