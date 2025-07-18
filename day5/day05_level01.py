import statistics
#Exercise 1 (Level 1) 
list = []
print(list)

#Exercise 2 (Level 1)

list = ['a','b','c','d','e','f']

#Exercise 3 (Level 1)
print('La longitud de la lista es de: ',len(list))

#Exercise 4 (Level 1)

print('El primer objeto es:',list[0])
middle_item = len(list) // 2
print('EL objeto de enmedio es:',middle_item)
print('El ultimo objeto es:',list[-1])

#Exercise 5 ( Level 1)

mixed_data_types = ['Anayeli Ezparza','19','1.58','soltera','Aguascalientes']

#Exercise 6 ( Level 1)

it_companies  =  ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#Exercise 7 ( Level 1)
print(mixed_data_types)
print(it_companies)

#Exercise 8 (Level 1)

print('El numero de compañias es: ',len(it_companies))

#Exercise 9 (Level 1)

print('El primer elemento de la lista es: ',it_companies[0])
middle_item_companie = len(it_companies)//2
print('El elemento de enmedio es:',middle_item_companie)
print('El ultimo valor de la lista es:',it_companies[-1])

#Exercise 10 (Level 1)

it_companies[1] = 'Tesla'
print('Cambio de empresa:',it_companies)

#Exercise 11 (Level 1)
it_companies.append('IT')
print(it_companies)

#Exercise 12 (Level 1)
middle= len(it_companies)//2
it_companies.insert(middle,'IT')
print(it_companies)

#Exercise 13 (Level 1)
it_companies[1] = it_companies[1].upper()
print(it_companies)

#Exercise 14 (Level 1)
print('#, '.join(it_companies))

#Exercise 15 (Level 1)
print('certain ¿esta en la lista?','certain' in it_companies )

#Exercise 16 (Level 1)
it_companies.sort()
print(it_companies)

#Exercise 17 (Level 1)
it_companies.reverse()
print(it_companies)

#Exercise 18 (Level 1)
it_companies1 = it_companies[0:3]
print(it_companies1)

#Exercise 19 (Level 1)
it_companies2 = it_companies[3:]
print(it_companies2)

#Exercise  20 (Level 1)

if ((len(it_companies)) %2!=0):

    print('Los elementos de enmedio en la lista son:',it_companies[middle])

else :
    print('El elemento de enmedio en la lista es:',it_companies[middle + 1: middle - 1])

#Exercise 21 (Level 1)

it_companies.pop(0)
print('Eliminado la primera empresa:',it_companies)

#Exercise 22 (Level 1)
it_companies = ['Amazon', 'Apple', 'Facebook', 'IBM', 'IT', 'Microsoft', 'Oracle', 'TESLA']

mitad_index = len(it_companies) // 2

if len(it_companies) % 2 != 0:
    del it_companies[mitad_index]
else:
    del it_companies[mitad_index - 1: mitad_index + 1]

print("Eliminando la compañia del medio:", it_companies)


#Exercise 23 (Level 1)

it_companies.pop()
print('Eliminando la ultima empresa',it_companies)

#Exercise 24 (Level 1)

it_companies.clear()
print('Eliminando todos los elementos de la lista:',it_companies)

#Exercise 25 (Level 1)
del it_companies

#Exercise 26 (Level 1)

front_end = ['HTML','CSS','JS','React','Redux']
back_end = ['Node','Express','MongoDB']

##front_end.extend(back_end)
##print(front_end)

#Exercise 27 (Level 1)
full_stack = front_end + back_end
Posicion_redux=full_stack.index('Redux')
full_stack.insert(Posicion_redux+1,'Python')
full_stack.insert(Posicion_redux+2,'SQL')

print(full_stack)
