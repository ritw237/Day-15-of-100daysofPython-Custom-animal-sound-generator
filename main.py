exit = "no"
while exit!="yes":
  animal = input("What animal do you want: Cow or Dog or Cat? ")
  if animal =="Cow":
    print("A cow goes Moo")
  elif animal == "Dog":
    print("Dog just keeps barking...quite annoying at times if you ask me")
  else:
    print("Cat purrs...meows too. I don't like cats")
  exit = input("Do you wanna exit?: ")