import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/itsme/PyCharmMiscProject/.venv/MiniProject/indian_nutrition_tracking_dataset.csv')
# indata=pd.to_csv("Nutrition1.csv")

df = pd.DataFrame(data)
# print(df.head())
input_data =["Food","Amount","Calories","Protein","Carbs","Fat"]
df1 = pd.DataFrame(columns=input_data)
df1.to_csv("nutrition1.csv", mode='w+',columns=input_data,index=False)
while (True):
    food = input("Enter The Food :")


    def nutrition(food):
        amount = int(input("Enter The Amount :"))
        nutrition_item = df[df["Food"] == food]
        # print(nutrition_item)
        # print(f"Food :{food} Amount :{amount} Nutrition Item :{nutrition_item[["Calories","Protein","Carbs","Fat"]]*amount}")
        indata1 = np.array(
            [[food, amount, (nutrition_item.iloc[0]["Calories"] * amount), (nutrition_item.iloc[0]["Protein"] * amount),
              (nutrition_item.iloc[0]["Carbs"] * amount), (nutrition_item.iloc[0]["Fat"] * amount)]], dtype=object)
        # print(input_data)
        global df2
        df2 = pd.DataFrame(indata1)
        df2.to_csv("nutrition1.csv", mode='a', header=False, index=False)


    nutrition(food)
    exit = int(input("Enter The 1 To exit :"))
    if (exit == 1):
        break
data1=pd.read_csv("nutrition1.csv")
print(data1.head())
# print([data1['Calories'].sum(),data1['Protein'].sum(),data1['Carbs'].sum(),data1['Fat'].sum()])
print(f"Total Calories :{data1['Calories'].sum()},Total Protein :{data1['Protein'].sum()},Total Carbs:{data1['Carbs'].sum()},Total Fat :{data1['Fat'].sum()}")
# print(f"Remaining Calories :{calorie-data1['Calories'].sum()},Remaining Protein :{protein-data1['Protein'].sum()},Remaining Carbs:{carbs -data1['Carbs'].sum()},Remaining Fat :{fat -data1['Fat'].sum()}")
plt.bar(["calories","protein","fat","carbs"],[data1['Calories'].sum(),data1['Protein'].sum(),data1['Fat'].sum(),data1['Carbs'].sum()],color="red")
#,linestyle="--",marker="o"
# plt.show()