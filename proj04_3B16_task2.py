# Coded by 3B16 Ng Tsz Yin

# Importing Module "Random" & "Time".
# Their module will be used in the later program.
import random
import time

# This is used for allow users to input value like numbers.
# /
# Chinese, English and Maths are the Variables.
# It will show "Enter the Chinese / English / Maths Mark" when you started run the program,
# And you may type the value of Chinese / English / Maths Marks.
# This is an input by the way.
Chinese = float(input("Enter the Chinese Marks: "))
English = float(input("Enter the English Marks: "))
Maths = float(input("Enter the Maths Marks: "))

# This is a Variable that about the Easter Egg chances.
# The chances of the Easter Egg are 0.10.
# The Easter Egg Chance program is in almost the bottom of the code.
easter_egg_chances = 0.10

# This is the messages that about showing "Calculating the average mark",
# I used "For loop" here.
# "i" is a variable, the range means how many "print" message will showed and i put 1 inside. So it will show 
# one "Calculating the avergae mark." & "Calculating the avergae mark.." & "Calculating the avergae mark..."
# Also, I added a time delay here, the time.sleep() is the time delay function and (1) mean 1 second.
# So basically, time.sleep(1) mean There is a 1 second time delay between three "Calculating the avergae mark." message.
for i in range(1):
    print("\nCalculating the avergae mark.")
    time.sleep(1)
for i in range(1):
    print("Calculating the avergae mark..")
    time.sleep(1)
for i in range(1):
    print("Calculating the avergae mark...")
    time.sleep(1)

# Average is the variable,
# This is the process of calculating the mean of Chinese, English and Maths marks.
# "(Chinese + English + Maths)/3" is the formula of calculating the mean of Chinese, English and Maths.
average = (Chinese + English + Maths)/3

# It is a 2 seconds time delay.
time.sleep(2)

# "random.random()" means return a random floating number between 0 and 1.  
# So if the easter_egg_chances (0.10) is larger than random.random(),
# The Easter Egg will occur. 
# /
# It will print three messages below and there are also the time delay function - time.sleep()
if random.random() < easter_egg_chances:
    print("\nOh wait... Something stucked")
    time.sleep(1)
    print("Fixing...")
    time.sleep(2)
    print("Done fixing!")
    time.sleep(1)
    print("\nRecalculating the avergae mark...")

# It will print the two decimal places 
# Average mark of Chinese, English and Maths.
# /
# This is the output.
print("\nYour Average Mark is %.2f" %average)

# It is a 1 seconds time delay (cooldown).
time.sleep(1)

# This is the if-statement.
# It's about if the Variable "average" is Greater Than or Equal To the value 50 / 60 / 70 / 90
# or Lower than the value 50,
# then it will randomly print out the text where inside [""].
# /
# If the inputs are wrong or something else occurred like error or cannot calculate,
# It will show "Unknown" in the console.

if average >= 90:
    print( random.choice(["Excellent!", "Fantastic!", "Wow! You just did a Great Job!", "Impressive!", "Incredible!"]))
elif average >= 70:
    print( random.choice(["Good!", "Amazing!", "Beautiful work!"]))
elif average >= 60:
    print( random.choice(["Satisfactory!", "Gratifying.", "Good job!", "Cool!"]))
elif average >= 50:
    print( random.choice(["Pass!", "Not Bad!", "Keep it up!"]))
elif average < 50 and average > 0:
    print( random.choice(["Below Average.", "Don’t ever give up!", "Fail!", "Hang in there."]))
elif average < 0:
    print( random.choice(["Huh?", "Unknown.", "Error", "Error404 O_o"]))
else:
    print("Unknown")



