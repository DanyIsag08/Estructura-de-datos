from Nodo import Nodo
print("Se crea la estructura:")
head = Nodo(100,Nodo(200,Nodo(300,Nodo(400,Nodo(600)))))
aux=head
while(aux):
	print(aux.get_dato())
	aux=aux.get_siguiente()
aux=head
print("Se cambia el valor de 300 a 333")

while(aux.get_dato()!=300):
	aux=aux.get_siguiente()
aux.set_dato(333)
aux=head
while(aux):
	print(aux.get_dato())
	aux=aux.get_siguiente()
aux=head
print("Agregar nuevo nodo (700)")
while(aux.get_siguiente() != None):
	aux=aux.get_siguiente()
aux.set_siguiente(Nodo(700))

aux=head
while(aux):
	print(aux.get_dato())
	aux=aux.get_siguiente()
aux=head
print("Valor al principio (50)")
nuevo_head=Nodo(50,head)
aux=nuevo_head
while(aux):
	print(aux.get_dato())
	aux=aux.get_siguiente()




