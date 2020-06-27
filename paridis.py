print("Scrivi un numero è ti dico se è pari o dispari")
num = input("Numero: ")
num = int(num)

pari = num % 2

if pari == 0:
   print(num ,"è un numero pari")

else:
   print(num ,"è un numero dispari")
