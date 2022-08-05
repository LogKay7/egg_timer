# Exercice 2 : Timer pour la cuisson des oeufs

import time
import beepy

def show_menu():
	print("Quelle cuisson desirez-vous?")
	print("1. Oeuf à la coque")
	print("2. Oeuf mollet")
	print("3. Oeuf dur")
	print("4. Quitter")

print("Timer pour la cuisson des oeufs")
print("-------------------------------")
print()

usr_choice = -1
timer = 0
while usr_choice == -1:
	try:
		show_menu()
		usr_choice = int(input("-> "))
	except:
		print()
		input("Choix invalide...")
		print()
	else:
		if usr_choice > 4 or usr_choice < 1:
			print()
			input("Choix invalide...")
			print()
			usr_choice = -1
if usr_choice == 1:
	timer = 180
elif usr_choice == 2:
	timer = 360
elif usr_choice == 3:
	timer = 540
if timer != 0:
	for i in range(timer):
		time.sleep(1)
		print(".", end="", flush=True)
		if (i % 10 == 0 and i != 0):
			time_last = timer -i
			minutes = time_last // 60
			secondes = time_last - minutes * 60
			print()
			print (f"Temps restant : {minutes}:{secondes:02d}", end="", flush=True)
	beepy.beep(sound="ping")
