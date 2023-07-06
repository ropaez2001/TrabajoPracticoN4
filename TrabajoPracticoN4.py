"""Escriba una función que muestre todos los números primos entre 1 y un número n que
 es ingresado por parámetro.
 
Primos(numero ):
   
def NumeroPrimo():    
  numero =int(input( "Ingresar un numero:  "))
  if numero >1:
    cont=0
    for i in range (2,numero): 
        
       resto= numero % i 
       print( resto)
       
       if resto==0:
        cont+=1
        
    
    if cont==0:
           print("numero  es primo: ",numero)
    else:
        print(numero ,"no es un numero primo")
        
  else:      
         print("el numero es menor que 2 ")
       
NumeroPrimo()      """
#-------------------------------------------------------------------------------

"""2) Escriba una función que le pida al usuario ingresar condimentos para un sándwich, 
hasta que el usuario ingrese ‘salir’. 
Cada vez que se ingrese un condimento, 
muestre un mensaje avisando que ya se agregó el condimento al sándwich.
Escriba versiones diferentes del programa de acuerdo a estos criterios:
       
• Use un test condicional en el ciclo while para detener la ejecución.
• Use un test condicional dentro del ciclo para decidir si continuar la ejecución."""
    
"""def Sandwich():
       aderezos=[] 
       
       condimentos=input(" Ingresar condimentos : ")
       
       while condimentos!="salir":
              aderezos.append(condimentos)
              print("ya se agregó el", aderezos, "al sándwich: ")
              condimentos = input("Ingresar otro condimento (o 'salir' para terminar): ")
       print(" los condimentos agregados al sandwich son: ", aderezos)       
Sandwich()"""


# la otra version---------------------------------------------------------
"""def Sandwich():
       aderezos=[] 
       
       condimentos=input(" Ingresar condimentos : ")
       
       while True:
              
              if condimentos=="salir":
               break
               
              if condimentos not in aderezos:
                      aderezos.append(condimentos)
                      print("ya se agregó el", aderezos, "al sándwich: ")
               
                      condimentos = input("Ingresar otro condimento,(o 'salir' para terminar): ")
                      
              elif condimentos  in aderezos:
                 print(" Ingresar otro condimento, esta repetido")
                 condimentos=input(" Ingresar otro  condimento , (o 'salir' para terminar): ") : ")
              
       print(" los condimentos agregados al sandwich son: ", aderezos)
                            
Sandwich()"""
              
       
            

                  
                  
     
      
  

         
     

    