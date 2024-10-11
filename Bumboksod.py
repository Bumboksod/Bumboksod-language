#Bumboksod
print("Czy chcesz zacząć samouczek po Bumboksod")

Tutorialnie = False

def drukuj():
	print("Wybierz słowo które ma się pojawić w konsoli")
	printt = input()
	print(printt)

def kalkulator():
	print("Podaj pełne działanie które kalkulator ma wykonać")
	x = input()
	print(eval(x))

def tutorial():
	print("Oto nowy język programowania na początku wpisz komendę drukuj")
	codetut = input()
	if codetut == "drukuj":
		drukuj()
	print("Bumboksod ma niektóre funkcje wbudowane w sobie takie jak kalkulator wpisz kalkulator")
	codetut = input()
	if codetut == "kalkulator":
		kalkulator()

Tutorialstart = input()
if Tutorialstart == "tak":
	tutorial()
else:
	Tutorialnie = True
	
while Tutorialnie:
	code = input()
	if code == "drukuj":
		drukuj()
	elif code == "kalkulator":
		kalkulator()
	else:
		print("nie ma takiej komendy zgłoś się na Youtube MoledGrid1 a postaram się ją dodać")