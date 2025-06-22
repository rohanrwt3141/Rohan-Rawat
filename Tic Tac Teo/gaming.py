for i in range(5):
    print("""1:if you want to play with friend
2:if you want to play with computer""")
    a=int(input("enter the mode of game:"))
    if(a==1):
        import playwithfriend
        break
    elif(a==2):
        import computer
        break
    else:
        print("Invalid mode" )
