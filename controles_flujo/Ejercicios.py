#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no 
# Solicitar la edad al usuario
```python
edad = int(input("Ingresa tu edad: "))

# Verificar si es mayor de edad o no
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")
    ```


#Escribir un programa que almacene la cedena de caracteres de contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincida con la guardada en la variable sin tener en cuenta mayusculas y minusculas.
```python
# Almacenar la contraseña en una variable
contraseña = "Contraseña123"

# Solicitar la contraseña al usuario
contraseña_usuario = input("Ingresa la contraseña: ")

# Comparar las contraseñas sin tener en cuenta mayúsculas y minúsculas
if contraseña.lower() == contraseña_usuario.lower():
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")
```

#Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atras desde ese numero hasta cero separados por comas.
```python
# Solicitar al usuario un número entero positivo
numero = int(input("Ingresa un número entero positivo: "))

# Verificar si el número es positivo
if numero > 0:
    # Inicializar la cadena de caracteres para la cuenta atrás
    cuenta_atras = str(numero)

    # Realizar la cuenta atrás desde el número ingresado hasta cero
    for i in range(numero - 1, -1, -1):
        cuenta_atras += ", " + str(i)

    # Mostrar la cuenta atrás por pantalla
    print(cuenta_atras)
else:
    print("El número ingresado no es válido")
```