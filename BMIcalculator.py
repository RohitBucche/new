# BMI = weight / height**2
import pyttsx3
engine = pyttsx3.init()


engine.say("Enter your Weight in Kilograms")
engine.runAndWait() 
x = int(input("Enter your Weight in Kg: "))

engine.say("Enter your Height in Centimeters")
engine.runAndWait() 
y = int(input("Enter your Height in CM: "))

# to convert height CM to meters
z = (y/100)

if x==0 or y==0:
    print("Enter Valid Numbers")
    engine.say("Enter Valid Numbers.")
else:

    bmi = x/(z**2)
    print(f"Your BMI is: {bmi:.2f}")
    engine.say(f"Your BMI is: {bmi:.2f}")

    if bmi<18.5:
        print("Your Are Under Weight") 
        engine.say("Your Are Under Weight") 
    
    elif 18.5<=bmi<24.9:
        print("You ARre Normal")
        engine.say("You ARre Normal") 

    elif 25<=bmi<29.9:
        print("You Are Over Weight")
        engine.say("You Are Over Weight") 

    elif 30<bmi<34.9:
        print("You Are Obese")
        engine.say("You Are Obese") 

    elif 35<bmi:
        print("You Are Extremly Obese") 
        engine.say("You Are Extremly Obese")    

engine.runAndWait()    