## DualDescriptor

Es un proyecto "UNIX" para automatizar las rutinas del software Gaussian. Debido a que este presenta una sintaxis compleja para los usuarios no habituados a la programación, lo cual lleva a errores y a perdida de tiempo en entender cómo utilizar el programa.

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
