from kaldagerist import Boy
from kaldagerist import Girl
import time

print("DESCRIBE YOUR CRUSH")

while True:
    gender = input("What is the gender of your crush (G/B and q to quit): ")
    if gender == "B" or gender == "b":
        boyHair = input("Hair type: ")
        boyHeight = input("His height: ")
        boyTalent = input("What is his talent: ")

        boyCrush = Boy(boyHair, boyHeight, boyTalent)
        boyCrush.describe()

    elif gender == "G" or gender == "g":
        girlHair = input("Hair type: ")
        girlHeight = input("Her height: ")
        girlTalent = input("What is her talent: ")

        girlCrush = Girl(girlHair, girlHeight, girlTalent)
        girlCrush.described()

    elif gender == "q" or gender == "Q":
        time.sleep(3)
        print("Closed successfully!")
        break
