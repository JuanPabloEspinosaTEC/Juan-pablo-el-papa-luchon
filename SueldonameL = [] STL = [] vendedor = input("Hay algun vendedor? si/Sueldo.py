nameL = []
STL = []
vendedor = input("Hay algun vendedor? si/no: ")
while vendedor.lower() == "si":
  name = input("Cual es el nombre del vendedor? ")
  SB = float(input("Cual es su salario base? "))
  TV = float(input("Cual es su total de ventas? "))
  nameL.append(name)
  com = 0
  if TV < 3500:
    com = 0.07
  elif TV >= 3500 and TV <= 7000:
    com = 0.1
  else:
    com = 0.15
  STL.append(SB + (SB * com))
  vendedor = input("Hay algun vendedor? si/no: ")
count = 0
for x in nameL:
  print("El vendedor " + x + " tiene un sueldo total de " + str(STL[count]))
  count += 1
