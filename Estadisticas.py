flag = input("Hay algun animal a registrar? si/no: ")
r1 = 0
r2 = 0
r3 = 0
r4 = 0
total = 0
while flag.lower() == "si":
  age = int(input("Cusl es la edad del animal? "))
  if age < 2:
    r1 += 1
  elif age >= 2 and age < 5:
    r2 += 1
  elif age >= 5 and age < 10:
    r3 += 1
  else:
    r4 += 1
  flag = input("Hay algun animal a registrar? si/no: ")

total = r1 + r2 + r3 + r4
print("En total hay " + str(total) + " animales de los cuales ")  
print(str(r1) + " tienen menos de 2 anos lo cual representa el " + str((r1 / total) * 100) + "%")
print(str(r2) + " tienen de 2 a menos de 5 anos lo cual representa el " + str((r2 / total) * 100) + "%")
print(str(r3) + " tienen de 5 a menos de 10 anos lo cual representa el " + str((r3 / total) * 100) + "%")
print(str(r4) + " tienen 10 o mas anos lo cual representa el " + str((r4 / total) * 100) + "%")
