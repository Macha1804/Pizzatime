

def pizza_time(une_variable):
	for number in range(1,une_variable + 1):
		if number % 3 == 0 and number % 5 == 0:
			print("PizzaTime")
		elif number % 5 == 0:
			print("Time")
		elif number % 3 == 0:
			print("Pizza")
		else:
			print(number)

# Une fois le programme terminé, redemander le numéro


# print("Veuillez entrer un nombre")
# Transformer la variable saisie en nombre
# a = input()
# while a != "STOP":
	# pizza_time(int(a))
# else:
	# print("Veuillez entrer un nombre")
	# a = input()

a = 4
while a != "STOP":
	print("Veuillez entrer un nombre")
	a = input()
	if a != "STOP":
		pizza_time(int(a))




	
