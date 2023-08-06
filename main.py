'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import sys, random

print("Добро пожаловать в генератор имен\n")
print("ваш результат:\n\n")

first = ('Akta','Anakis','Armara','Astaro','Aym','Azza','Beleth','Bryseis','Bune','Criella','Damaia', 'Decarabia','Ea',
'Gadreel','Gomory', 'Hecat', 'Ishte', 'Jezebeth','Kali', 'Kallista','Kasdeya',
'Lerissa','Lilith','Makaria','Manea','Markosian','Mastema','Naamah','Nemeia','Nija','Orianna','Osah','Phelaia',
'Prosperine','Purah','Pyra','Rieta','Ronobe','Ronwe','Seddit','Seere','Sekhmet','Semyaza','Shava','Shax','Sorath',
'Uzza','Vapula','Vepar','Verin')

last = ('','','','','','','','','','','','','','','','','','','','','','','','','','','','',
'','','','','','','','','','','','','','','','','','','','','','','','','','','','',
'','','','','','','','','','','','','','','','','','','','','','','','','','','','',
'Ambition','Art','Carrion','Chant','Creed','Death','Debauchery','Despair','Doom','Doubt','Dread',
'Ecstasy','Innui','Entropy','Excellence','Fear','Glory','Gluttony','Grief','Hate','Hope','Horror',
'Ideal','Ignominy','Laughter','Love','Lust','Mayhem','Mockery','Murder','Muse',
'Music','Mystery','Nowhere','Open','Pain','Passion','Poetry','Quest',
'Random','Reverence','Revulsion','Sorrow','Temerity','Torment','Tragedy','Vice','Virtue','Weary','Wit')
while True:
    FirstName = random.choice(first)
    LastName = random.choice(last) 
    print("\n\n{} {}\n\n".format(FirstName,LastName),file=sys.stderr)
    tryagain = input("\n\nОтправимся покорять драконов?(Enter дает еще бабу тифлинга, n на выход)\n")
    if tryagain.lower() == "n":
        break
input("\n Enter прочь от ДНД.")
    