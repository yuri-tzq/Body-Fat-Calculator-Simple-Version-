import math

while True:

    #user's gender
    gender = input("Please choose your gender (M/F): ")

    #if user is female
    if gender.lower() == "f":

        #user's body data
        height = float(input("Height (cm): ")) 
        neck = float(input("Neck Circumference (cm): "))
        waist = float(input("Waist Circumference (cm): "))
        hip = float(input("Hip Circumference (cm): "))
        
        fat = 163.205 * math.log10(waist + hip - neck) - 97.684 * math.log10(height) - 78.387
        print(round(fat/2.54 , 2))

    #if user is male
    elif gender.lower() == "m":

        #user's body data
        height = float(input("Height (cm): "))
        neck = float(input("Neck Circumference (cm): "))
        waist = float(input("Waist Circumference (cm): "))
        abdomen = float(input("Abdomen (cm): "))
        
        fat = 86.010 * math.log10(abdomen - neck) - 70.041 * math.log10(height) + 36.76
        print(round(fat/2.54 , 2))

    else:
        print("I mean biological NOT your identity.")