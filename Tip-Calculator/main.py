#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total = input("what was the total bill?  ")
tip = input("How much tip would you like to give? 10, 12, or 15?  ")
people = input("How many people to split the bill?  ")

float_total = float(total)
int_tip = round(int(tip) / 100 + 1, 2)
int_people = int(people)

final_total = (float_total / int_people) * int_tip
print(f"Each person should pay: ${round(final_total,2)}")