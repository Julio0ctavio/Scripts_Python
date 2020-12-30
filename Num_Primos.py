
print("Números primos del 1 al 100")

for x in range(2,100):
	for y in range(2,x):
		if(x % y == 0):
			#En caso de que deseemos ver los múltiplos de los otros núnmeros:
			#print(str(x) + ' es igual a' + str(y) + '*' + str(x/y) + "\n");
			break;
	else:
		print("\n\tNum. Primo: " + str(x));
