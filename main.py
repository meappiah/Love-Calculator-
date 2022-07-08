print("Welcome to the Love Calculator!") #welcome message 
name1 = input("What is your name? \n") #defining first name variable 
name2 = input("What is their name? \n")#defining second name variable 
combined_names = name1 + name2 #combining the string (names)
lowercase_names = combined_names.lower()  #Changing all letters into lower case 

#counting the letters of true in the combined names 
t = lowercase_names.count("t")
r =lowercase_names.count("r")
u = lowercase_names.count("u")
e = lowercase_names.count("e")

#counting the letters of LOVE in the combined names 

l = lowercase_names.count("l")
o = lowercase_names.count("o")
v = lowercase_names.count("v")
e = lowercase_names.count("e")

true = t +r + u + e #adding the counted strings in TRUE 
love = l +o +v+ e   #adding the counted strings in LOVE 

love_score = int (str(true) + str(love)) #combining the counts to get the love score.

#Defining the conditions 
if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos. ")

elif love_score >= 40 and love <= 50:
  print(f"Yor score is {love_score}, you are alright together.")
else: 
  print (f"Your score is {love_score}.")







