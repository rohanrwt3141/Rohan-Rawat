import random
name1=int(input("enter the name of player:"))
l1=[]
l2=[]
d=([1,2,3],[4,5,6,],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7])
X=[1,2,3,4,5,6,7,8,9]
g=8
print("""
             |    |    
          1  | 2  | 3  
         ----|----|----
          4  | 5  | 6  
         ----|----|----
          7  | 8  | 9  
             |    |

             """)
print(name1,"has 0")
print("computer has X")
print("""
             |    |    
             |    |    
         ----|----|----
             |    |    
         ----|----|----
             |    |    
             |    |
""")
a="""
             |     |    
          1  |  2  |  3
        -----|-----|-----
          4  |  5  |  6  
        -----|-----|----- 
          7  |  8  |  9  
             |     |    """
x="""
             |     |    
             |     |   
        -----|-----|-----
             |     |     
        -----|-----|----- 
             |     |     
             |     |    """
l=list(x)
for t in range(9):
    if(t%2==0):
     b=int(input("choose the number player:"))
     X.remove(b)
     g-=1
     for s in range(len(a)):
         if(b==1):
          if(a[s]=="1"):
              l[s]="O"
              l1.append(1)
              print("".join(l))
              if(sorted(l1) in d):
                  print(name1,"win")
          else:
              pass
         elif(b==2):
          if(a[s]=="2"):
              l1.append(2)
              l[s]="O"
              print("".join(l))
              if(sorted(l1) in d):
                  print(name1,"win")
          else:
              pass
         elif(b==3):
          if(a[s]=="3"):
             l[s]="O"
             print("".join(l))
             l1.append(3)
             if(sorted(l1) in d):
                 print(name1,"win")
          else:
              pass
         elif(b==4):
          if(a[s]=="4"):
              l1.append(4)
              l[s]="O"
              print("".join(l))
              if(sorted(l1) in d):
                  print(name1,"win")
          else:
              pass 
         elif(b==5):
          if(a[s]=="5"):
             l[s]="O"
             l1.append(5)
             print("".join(l))
             if(sorted(l1) in d):
                 print(name1,"win")
          else:
              pass
         elif(b==6):
             if(a[s]=="6"):
              l[s]="O"
              l1.append(6)
              print("".join(l))
              if(sorted(l1) in d):
                  print(name1,"win")
             else:
              pass
         elif(b==7):
             if(a[s]=="7"):
              l[s]="O"
              l1.append(7)
              print("".join(l))
              if(sorted(l1) in d):
                  print(name1,"win")
             else:
              pass
         elif(b==8):
             if(a[s]=="8"):
              l[s]="O"
              l1.append(8)
              print("".join(l))
              if(sorted(l1) in d):
                  print(name1,"win")
             else:
              pass 
         elif(b==9):
             if(a[s]=="9"):
              l[s]="O"
              l1.append(9)
              print("".join(l))
              if(sorted(l1) in d):
                  print(name1,"win")
             else:
              pass
         else:
             print("Invalid number is entered.")
             break
     
    else:
     print("Computer turn")   
     c=X[random.randint(0,g)]
     print("Computer has choosen",c)
     g-=1
     X.remove(c)
     for s in range(len(a)):
            if(c==1):
             if(a[s]=="1"):
              l[s]="X"
              l2.append(1)
              print("".join(l))
              if(sorted(l2) in d):
                  print(name2,"win")
             else:
              pass
            elif(c==2):
             if(a[s]=="1"):
              l[s]="X"
              l2.append(2)
              print("".join(l))
              if(sorted(l2) in d):
                  print(name2,"win")
             else:
              pass
            elif(c==3):
             if(a[s]=="3"):
              l[s]="X"
              l2.append(3)
              print("".join(l))
              if(sorted(l2) in d):
                  print(name2,"win")
             else:
              pass
            elif(c==4):
             if(a[s]=="4"):
              l[s]="X"
              l2.append(4)
              print("".join(l))
              if(sorted(l2) in d):
                  print(name2,"win")
             else:
              pass 
            elif(c==5):
             if(a[s]=="5"):
              l[s]="X"
              l2.append(5)
              print("".join(l))
              if(sorted(l2) in d):
                  print(name2,"win")
             else:
              pass
            elif(c==6):
             if(a[s]=="6"):
              l[s]="X"
              l2.append(6)
              print("".join(l))
              if(sorted(l2) in d):
                  print(name2,"win")
             else:
              pass
            elif(c==7):
             if(a[s]=="7"):
              l[s]="X"
              l2.append(7)
              print("".join(l))
              if(sorted(l2) in d):
                  print(name2,"win")
             else:
              pass
            elif(c==8):
             if(a[s]=="8"):
              l[s]="X"
              l2.append(8)
              print("".join(l))
              if(sorted(l2) in d):
                  print(name2,"win")
             else:
              pass 
            elif(c==9):
             if(a[s]=="9"):
              l[s]="X"
              l2.append(9)
              print("".join(l))
              if(sorted(l2) in d):
                  print(name2,"win")
             else:
              pass
            else:
             print("Invalid number is entered.")
             break

