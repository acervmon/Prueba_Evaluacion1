#Ejercicio 5: Descomposición de Dirección IP
#Crea un script que tome una dirección IP como argumento y la descomponga en sus cuatro octetos, mostrándolos línea a línea.
import sys
import ipaddress

# Solicita al usuario que ingrese un IP
ip_input = input("Enter an IP address: ")

try:
    ip_addr = ipaddress.ip_address(ip_input)
    print("The IP address is valid.")
except ValueError as e:
    print(f"Error: {e}")
    print("The IP address is not valid.")

