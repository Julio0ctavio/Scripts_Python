'''Escribir un programa que pregunte al usuario su edad y
muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).'''

user_age = int(input("¿Cuántos años tienes? "))
for age in range(0, user_age):
    if age == 0:
        print("Cumpliste {} año".format(age+1))
    else:
        print("Cumpliste {} años".format(age+1))
