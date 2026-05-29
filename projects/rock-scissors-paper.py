import random;
print("1=rock 2=scissors 3=paper.");
userchoice=int(input("Choose one of rock, scissors, paper."));
computerchoice=random.randint(1,3);
if userchoice==computerchoice:
    print("It's a tie.")
elif(userchoice==1 and computerchoice==2) or (userchoice==2 and computerchoice==1) or (userchoice==3 and computerchoice==2):
    print("Computer won.")
else:
    print("User won.");
