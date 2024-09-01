import csv
with open('documento.csv', mode='r', encoding='ISO-8859-1') as file:
    reader = csv.reader(file)
    rows = list(reader) 
    enerof = int(rows[8][3])
    juniof = int(rows[8][8])
    print("Diferencia entre enero y junio es:",juniof - enerof)

enerov = int(rows[16][3])
febrerov = int(rows[16][4])
marzov = int(rows[16][5])
abrilv= int(rows[16][6])
mayov = int(rows[16][7])
juniov = int(rows[16][8])

def dif(a,b):
    print (a - b)
   
A, B = input().split()

minus1 = A.lower()
minus2 = B.lower()


meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]

if minus1 == meses[0]:
    x = enerov
elif minus1 == meses[1]:
    x = febrerov
elif minus1 == meses[2]:
    x = marzov
elif minus1 == meses[3]:
    x = abrilv
elif minus1 == meses[4]:
    x = mayov
elif minus1 == meses[5]:
    x = juniov
    
if minus2 == meses[0]:
    y = enerov
elif minus2 == meses[1]:
    y = febrerov
elif minus2 == meses[2]:
    y = marzov
elif minus2 == meses[3]:
    y = abrilv
elif minus2 == meses[4]:
    y = mayov
elif minus2 == meses[5]:
    y = juniov

dif(y, x)

eneroc = int(rows[2][3])
febreroc = int(rows[2][4])
marzoc = int(rows[2][5])
abrilc = int(rows[2][6])
mayoc = int(rows[2][7])
junioc = int(rows[2][8])

def suma(a,b,c,d,e,f):
    return a+b+c+d+e+f

total=suma(eneroc,febreroc,marzoc,abrilc,mayoc,junioc)
print("Promedio de facebook (Crecimiento): ",total / 6)

enerot = int(rows[9][3])
febrerot = int(rows[9][4])
marzot = int(rows[9][5])
abrilt = int(rows[9][6])
mayot = int(rows[9][7])
juniot = int(rows[9][8])

totalt = suma(enerot,febrerot,marzot,abrilt,mayot,juniot)
print("Promedio de twitter (Crecimiento): ",totalt / 6)

megustef = int(rows[5][3])
megustff = int(rows[5][4])
megustmarf = int(rows[5][5])
megustaf = int(rows[5][6])
megustmayf = int(rows[5][7])
megustjf = int(rows[5][8])
megustet = int(rows[13][3])
megustft = int(rows[13][4])
megustmart = int(rows[13][5])
megustat = int(rows[13][6])
megustmayt = int(rows[13][7])
megustjt = int(rows[13][8])
megustey = int(rows[18][3])
megustfy = int(rows[18][4])
megustmary = int(rows[18][5])
megustay = int(rows[18][6])
megustmayy = int(rows[18][7])
megustjy = int(rows[18][8])

me_gustas_face = suma(megustef, megustff, megustmarf, megustaf, megustmayf, megustjf)
me_gustas_twitter = suma(megustet, megustft, megustmart, megustat, megustmayt, megustjt)
me_gustas_youtube = suma(megustey, megustfy, megustmary, megustay, megustmayy, megustjy)

def suma_me_gustas(a,b,c):
    return a+b+c

total_de_me_gustas = suma_me_gustas(me_gustas_face, me_gustas_youtube, me_gustas_twitter)

print("Promedio total de me gustas de facebook, twitter y youtube: " , total_de_me_gustas/18)

