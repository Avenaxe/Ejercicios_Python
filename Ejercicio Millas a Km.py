#Laboratorio Python Tecnicas de Analisis Numerico Prop A23
###Convertidor de Longitudes o Distancias  
#Ejercicio 1

#Primero Declaramos nuestras variables a utilizar 

 
 

kilometros = 1 

millas = 1.61 

 
 

#Inicializamos un menu de opciones de convertidor 

 
 

print("Convertidor de Longitudes") 

print("Millas a Kilometros - Presiona 1") 

print("Kilometros a Millas - Presiona 2") 

 
 

#En esta sección se desarrollo un bucle ´while´ para poder tener un indicador si alguna eleccion del menu es invalida 

#Este pueda solicitar una eleccion verdadera o correcta 

 
 
 

while True: 

    opcion = input("Elija una opción: ") 

 
 

    if opcion == "1": 

        mak = float(input("Digita la cantidad a convertir en Millas")) 

        print("*****", mak, "millas es igual a:", (round(mak*millas, 4)), "Kilometros","*****") 

        break 

         

        #Utilizamos ´break´ para indicar que la instrucción ha terminado 

         

    elif opcion == "2": 

        kam = float(input("Digita la cantidad a convertir en Kilometros")) 

        print("*****",kam, "Kilometros es igual a:", (round(kam/millas, 4)), "Millas","*****") 

        break 

 
 

         #Else nos permitió tener solicitar nuevamente la seleccion en el menu si la elección del menu elegida no existe 

 
 

    else:  

        print("Elige una opcion valida")