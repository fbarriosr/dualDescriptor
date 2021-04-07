## DualDescriptor

Genera archivos .cub visualizables con el programa GaussView o cualquier otro capaz de leer archivos .cub provenientes de Gaussian. Corresponden a los campos escalares de las funciones de Fukui nucleofílica, Fukui electrofílica y al descriptor dual.  Por cada sistema molecular, requiere como alimentación de tres archivos .fchk correspondientes al sistema con N, N+p y N-q electrones. Utilizable solo en servidores con sistema operativo Linux y siempre tenga instalados y operativos
los programas Gaussian y sus complementarios cubegen y cubman.

## Requerimientos

Requiere servidor con los software cubegen y cubeman de Gaussian.

## Installation

Copia la carpeta DualDescriptor en tu cuenta del servidor. 
```
$ scp dualDescriptor.tar user@server:/home/user/
```
Descomprime el archivo
```
$ tar -xvf  dualDescriptor.tar
```
También puedes crear un alias en $ .bashrc. Utiliza un editor de texto 
```
$ vi ~.bashrc
```
Y agrega esta ultima linea: 
```
alias dd='python /home/user/dualDescriptor/dualDescriptor.py'
```

## Ejecución
Debes crear un archivo y tener los 3 archivos .fchk (proyecto Gaussian), luego ejecutar el programa mediante el comando python

Versión Gráfica:
```
$ python /home/user/dualDescriptor/dualDescriptor.py
```
Version Linea de Comandos:
```
$ python /home/user/dualDescriptor/dualDescriptor.py more
```
o simplemente usado el alias dd:

Versión Gráfica:
```
$ dd
```
![](https://webdesign.s3-us-west-2.amazonaws.com/dualdescriptor/dd_img1.png)
![](https://webdesign.s3-us-west-2.amazonaws.com/dualdescriptor/dd_img2.png)


Version Linea de Comandos:
```
$ dd more
```
![](https://webdesign.s3-us-west-2.amazonaws.com/dualdescriptor/dd_img3.png)
