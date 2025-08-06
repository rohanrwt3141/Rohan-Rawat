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
                print(a," have taken Ladder from 3 to 22")
                c = 22
                print(a,"your current position is ",c)
            elif (c == 5):
                c = 8
                print(a, " have taken Ladder from 5 to 8")
                print(a, "your current position is ", c)
            elif (c == 11):
                c = 26
                print(a, " have taken Ladder from 11 to 26")
                print(a, "your current position is ", c)
            elif (c == 17):
                c = 4
                print(a, " have eaten by snake from 17 to 4")
                print(a, "your current position is ", c)
            elif (c == 19):
                c = 7
                print(a, " have eaten by snake from 19 to 7")
                print(a, "your current position is ", c)
            elif (c == 20):
                c = 29
                print(a, " have taken Ladder from 20 to 29")
                print(a, "your current position is ", c)
            elif (c == 21):
                c = 9
                print(a, " have eaten by snake from 21 to 9")
                print(a, "your current position is ", c)
            elif (c == 27):
                c = 1
                print(a, " have eaten by snake from 27 to 1")
                print(a, "your current position is ", c)
            elif (c > 30):
                c=c-e
                print(a, "your current position is ", c)
            elif (c == 30):
                print(a, "Win the game")
                break
            else:
                pass
                print(a, "your current position is ", c)
            n = n + 1

    else:
        die = int(input("Enter 1 to roll the die :"))
        if (die == 1):
            e = random.randint(1, 6)
            print(e)
            d = d + e
            if (d == 3):
                print(b, " have taken Ladder from 3 to 22")
                d = 22
                print(b, "your current position is ", d)
            elif (d == 5):
                d = 8
                print(b, " have taken Ladder from 5 to 8")
                print(b, "your current position is ", d)
            elif (d == 11):
                d = 26
                print(b, " have taken Ladder from 11 to 26")
                print(b, "your current position is ", d)
            elif (d == 17):
                d = 4
                print(b, " have eaten by snake from 17 to 4")
                print(b, "your current position is ", d)
            elif (d == 19):
                d = 7
                print(b, " have eaten by snake from 19 to 7")
                print(b, "your current position is ", d)
            elif (d == 20):
                d = 29
                print(b, " have taken Ladder from 20 to 29")
                print(b, "your current position is ", d)
            elif (d == 21):
                d = 9
                print(b, " have eaten by snake from 21 to 9")
                print(b, "your current position is ", d)

            elif (d == 27):
                d = 1
                print(b, " have eaten by snake from 27 to 1")
                print(b, "your current position is ", d)
            elif (d > 30):
                d=d-e
                print(b, "your current position is ", d)
            elif (d == 30):
                print(b, "Win the game")
                break
            else:
                pass
                print(b, "your current position is ", d)
            n = n + 1

