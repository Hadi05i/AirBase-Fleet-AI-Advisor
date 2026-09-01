import pandas as pd

from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv('python/AirBaseData.csv')


X=df[['Distance','Radar_Strength','Stealth_Required']]

y=df['Decision']

clf =RandomForestClassifier(n_estimators=100,random_state=42)
clf= clf.fit(X,y)

class AirCraft:
    def init(self,model,speed,missiles,fuel):
        self.model=model
        self.speed=speed
        self.missiles=missiles
        self.fuel=fuel
    def Details(self):
        print(f"\n-------{self.model} Status-------")    
        print(f"Speed:{self.speed/1225.0} Mach")
        print(f"Missiles:{self.missiles}")
        print(f"Fuel Level:{self.fuel}%")

fleet=[]

while True:
    print("\n1. Add New AirCraft")
    print("2. Display All Fleet")
    print("3. Exit")
    print("4. For AI Advice To Your Mission")
    
    try:
        choice=int(input("Enter Choice:"))
    except ValueError:
        print("Please enter a valid number.")
    if(choice==1):
        m=input("Model: ")
        s=float(input("Speed(km/h):"))
        msl=int(input("Missiles: "))
        f=int(input("Fuel: ")) 
        myplan=AirCraft(m,s,msl,f)
        fleet.append(myplan)
        print("Success! AirCraft Added To Fleet")
    elif (choice==2):
        if not fleet:
            print("Fleet is Empty,Please Add AirCrafts!")
        else:
            for plane in fleet:
                plane.Details()
    elif(choice==3):
        print("Exiting ....")
        break     
    elif (choice==4):
        if not fleet:
            print("The Fleet Is Empty")
        else:
            print("\n--- AI Mission Advisor ---")
            dis=float(input("Enter The Distance(1-1000 Km):"))
            radar=int(input("Enter Radar Level(1-10):"))
            stealth=int(input("Is Stealth Required? (1 for Yes , 0 for No):"))
            prediction=clf.predict([[dis,radar,stealth]])
            print(f"\n[AI Decision]:The most Suitable AirCraft for This Mission is:{prediction[0]}")
