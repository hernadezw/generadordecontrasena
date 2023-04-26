import random # generar numeros, textos, caracteres aleatorios 

class Generador:

def generador_contra(): # metodo y una funcion,  una funcion devuelve un valor y un metodo realiza una tarea en epecífica sin necesidad de devolver un valor
    mayuscula=['A','B','C','D','E','F','G','H','I'] #diccionario 
    minuscula=['a','b','c','d','e','f','g','h'] #diccionario
    simbolo=['!','#','%','$','/']
    numero=['1','2','3','4','5','6','7','8','9']
    
    caracteres=mayuscula+minuscula+simbolo+numero 
    
    contrasena=[]    
    for i in range(15):
        caracter_random=random.choice(caracteres) 
        contrasena.append(caracter_random)        #.append sirve para agregar un elemento en la lista
    
    contrasena="".join(contrasena)               #. join sive para unir los elementos en la lista osea lo convierte en un texto 
    return contrasena # devolver un valor 


cantidad=int(input("Ingrese cantidad: "))

a=654
b=632
c=152









while (cantidad>=8):
    valor_devuelto=generador_contra()
    print("Su nueva contraseña es: " + valor_devuelto)




# 
 #cantidad minima debe ser de 8

# Ingrese la cantidad de caracteres para su contraseña: 5
# la cantidad de caracteres es muy bajo

# Ingrese la cantidad de caracteres para su contraseña
# su nueva contaseña es: lkiedsdsds8uekk3483434343dsdsdsds
