import math

while True:

    #user's gender
    gender = input("Please choose your gender (M/F): ")

    #if user is female
    if gender.lower() == "f":

        #loop for height
        while True:
            #user's body data
            height = float(input("Height (cm): ")) 

            #check whether this mdfk's height is realistic or not
            if height <= 0:
                print("Height cannot be negative or zero.")
            else:
                break

        #loop for neck
        while True:
            #user's body data
            neck = float(input("Neck Circumference (cm): "))

            #check whether this mdfk is realistic or not
            if neck <= 0:
                print("Neck cannot be negative or zero.")
            else:
                break

        #loop for waist
        while True:
            #user's body data
            waist = float(input("Waist Circumference (cm): "))

            #check whether this mdfk is realistic or not
            if waist <= 0:
                print("waist cannot be negative or zero.")
            else:
                break

        #loop for hip
        while True:
            hip = float(input("Hip Circumference (cm): "))

            if hip <= 0:
                print("Hip cannot be negative or zero.")
            else:
                break
        
        #calculation
        fat = 163.205 * math.log10((waist + hip - neck)/2.54) - 97.684 * math.log10(height/2.54) - 78.387
        print(f"Body Fat: {round(fat, 2)}%")

    #if user is male
    elif gender.lower() == "m":

        #loop for height
        while True:
            #user's body data
            height = float(input("Height (cm): ")) 

            #check whether this mdfk's height is realistic or not
            if height <= 0:
                print("Height cannot be negative or zero.")
            else:
                break

        #loop for neck
        while True:
            #user's body data
            neck = float(input("Neck Circumference (cm): "))

            #check whether this mdfk is realistic or not
            if neck <= 0:
                print("Neck cannot be negative or zero.")
            else:
                break

        #loop for waist
        while True:
            #user's body data
            waist = float(input("Waist Circumference (cm): "))

            #check whether this mdfk is realistic or not
            if waist <= 0:
                print("waist cannot be negative or zero.")
            else:
                break

        #loop for abdomen
        while True:
            abdomen = float(input("Hip Circumference (cm): "))

            if abdomen <= 0:
                print("Abdomen cannot be negative or zero.")
            else:
                break
        
        fat = 86.010 * math.log10((abdomen - neck)/2.54) - 70.041 * math.log10(height/2.54) + 36.76
        print(f"Body Fat: {round(fat, 2)}%")

    else:
        print("Please type either 'M' or 'F' according to your biological gender.")