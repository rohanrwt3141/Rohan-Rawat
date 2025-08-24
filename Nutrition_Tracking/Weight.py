import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
weight =int(input("Enter your weight in Kg:"))
height=int(input("Enter your height in cm:"))
BMI=weight//(((height)*0.01)**2)
if(BMI<18.5):
    cond="Under Weight"
    print("Under weight")
elif(18.5<=BMI<24.9):
    cond = "Normal"
    print("Normal")
elif(24.9<=BMI<30):
    cond = "Overweight"
    print("Overweight")
else:
    cond = "Obese"
    print("Obese")
def nutri(cond):
    age=int(input("Enter your age:"))
    gender=input("Enter Your Gender :: Male Or Female:")
    if(gender=="Male"):
        BMR=(10*weight) + (6.25*height)-(5*age) +5
    else:
        BMR=(10*weight) + (6.25*height)-(5*age) -161

    active=input("Enter Your Activity :: Senentar(no exercise)\n Light exercise \nModerate exercise \nHeavy exercise \nVery intense exercise:")
    if(active=="Senentar"):
        TDEE=BMR*1.2
    elif(active=="Heavy exercise"):
        TDEE=BMR*1.725
    elif(active=="Very intense exercise"):
        TDEE=BMR*1.9
    elif(active=="Moderate exercise"):
        TDEE=BMR*1.55
    elif(active=="Light exercise"):
        TDEE=BMR*1.375
    else:
        print("Invalid input")
    if(cond=="Under Weight"):
        calorie=TDEE+500
        protein = (0.25 * TDEE)/4
        fat = (0.3 * TDEE)/9
        carbs = (0.55 * TDEE)/4
        print(f"Your Goal :: Calories : {calorie} Cal \n Protein :{protein} \n Fat : {fat} \n Carbs : {carbs}")
    elif(cond=="Over weight"):
        calorie = TDEE - 300
        protein = (0.35 * TDEE)/4
        fat = (0.3) * TDEE/9
        carbs = (0.5 * TDEE)/4
        print(f"Your Goal :: Calories : {calorie} Cal \n Protein :{protein} \n Fat : {fat} \n Carbs : {carbs}")
    elif(cond=="Normal"):
        calorie=TDEE
        protein = (0.2 * TDEE)/4
        fat = (0.3 * TDEE)/9
        carbs = (0.55 * TDEE)/4
        print(f"Your Goal :: Calories : {calorie} Cal \n Protein :{protein} \n Fat : {fat} \n Carbs : {carbs}")
    elif(cond=="Obese"):
        calorie=TDEE-900
        protein =(0.35*TDEE)/4
        fat=(0.3*TDEE)/9
        carbs=(0.5*TDEE)/4
        print(f"Your Goal :: Calories : {calorie} Cal \n Protein :{protein} \n Fat : {fat} \n Carbs : {carbs}")
    print("-------------------NOTE :You have to track your calories every day.-----------------------")
    choice=input("Enter Yes :: To open Nutrition Tracker \n No :: To close The app")
    plt.bar(["calories", "protein", "fat", "carbs"], [calorie, protein, fat, carbs], color="Black")
    #, linestyle="--",marker="o"

    if(choice=="No"):
        pass
    else:
        import Nutrition_Tracking
        plt.show()

nutri(cond)
