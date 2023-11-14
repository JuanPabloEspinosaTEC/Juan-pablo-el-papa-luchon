pasword = ""
flag = 0
validCh = "1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
print("Create a password just with numbers and letters")
for x in range(8):
  character = input("Enter " + str(x + 1) + " caracter of the password: ")
  while len(character) != 1:
    character = input("Enter a valid " + str(x + 1) + " caracter of the pasword: ")
  for y in validCh:
    if character == y:
      flag += 1
  pasword += character
print("The pasword is " + str(pasword))
if flag == 8:
  print("The password is valid")
else:
  print("The password its unvalid, you can just use letters and numbers ofthe eanglish keyboard")
