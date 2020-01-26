from Modules.test import *

counter = 0

name = input("Enter your name: ")

if question01() == "b":
    counter += 1
if question02() == "b":
    counter += 1
if question03() == "a":
    counter += 1
if question04() == "c":
    counter += 1
if question05() == "a":
    counter += 1
if question06() == "b":
    counter += 1
if question07() == "b":
    counter += 1
if question08() == "c":
    counter += 1
if question09() == "b":
    counter += 1
if question10() == "b":
    counter += 1
if question11() == "c":
    counter += 1
if question12() == "c":
    counter += 1

print(name, "Ви набрали ==== ", counter, "балів")

if counter == 12 or counter == 11 or counter == 10:
    perfectly()
elif counter == 9 or counter == 8 or counter == 7:
    fine()
elif counter == 6 or counter == 5 or counter == 4:
    satisfactorily()
elif counter <= 3:
    unsatisfactory()