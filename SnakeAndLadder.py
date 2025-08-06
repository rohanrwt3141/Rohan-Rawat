import random
a=input("Enter Your Name :")
b=input("Enter Your Name :")
c=0
d=0
n=0
while(c!=30 or d!=30):
    if(n%2==0):
        die=int(input("Enter 1 to roll the die :"))
        if (die==1):
            e=random.randint(1,6)
            print(e)
            c = c + e
            if (c == 3):
                c = 22
            elif (c == 5):
                c = 8
            elif (c == 11):
                c = 26
            elif (c == 17):
                c = 4
            elif (c == 19):
                c = 7
            elif (c == 20):
                c = 29
            elif (c == 21):
                c = 9
            elif (c == 27):
                c = 1
            elif (c >= 30):
                print(a, "Win the game")
                break
            else:
                pass
            n = n + 1

    else:
        die = int(input("Enter 1 to roll the die :"))
        if (die == 1):
            e = random.randint(1, 6)
            print(e)
            d = d + e
            if (d == 3):
                d = 22
            elif (d == 5):
                d = 8
            elif (d == 11):
                d = 26
            elif (d == 17):
                d = 4
            elif (d == 19):
                d = 7
            elif (d == 20):
                d = 29
            elif (d == 21):
                d = 9
            elif (d == 27):
                d = 1
            elif (d >= 30):
                print(b, "Win the game")
                break
            else:
                pass
            n = n + 1

