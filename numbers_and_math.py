print("I have a class of 33 students.")
print("There are 11 girls, so that means..")
# This line subtracts 11 (the number of girls) from 33 (the total number of students), thus yielding the number of boys
print(f"there are {33 - 11} boys.") 
print()
# This line divides 11 by 33 to find the ratio of girls to the total number of people inside the class. However, it may be missing a * 100 as the output should be a percentage rather than a decimal. 
print(f"That means {round(11 / 33, 2)} % are girls...")
# This line subtracts 11 from 33 to find the number of boys, and divides it by 33 to find the ratio of boys to total number of people in the class. However, it may be missing a * 100 as the output should be a percentage rather than a decimal. 
print(f"and {round((33 - 11) / 33, 2)} % are boys.")
print()
print("If we made groups of six...")
# A floor division is used in this line to divide 33 by 6 and round the answer down to the nearest integer. This is because it is impossible to have a fraction of a person and it would not make sense to round up, as it is impossible to conjure up a new person. 
print(f"There would be {33 // 6} groups of six.")
# This line finds the remainder of 33 divided by 6. 
print(f"And then a smaller group of {33 % 6} people.")
# This line prints out 30 dashes. 
print("-" * 30)
print("If we had 17 apples and 3 people...")
# This line uses a floor division to find 17 divided by 3 to the nearest integer (rounded down)
print(f"Each person would get {17 // 3} whole apples.")
# This line finds the remainder—that is, the number of apples remaining after dividing it evenly among 3 people. 
print(f"There would be {17 % 3} apples remaining.")
print()
print("If we charged each person $2 each for their 5 apples..")
# This line multiplies the number of apples (5) by the number of dollars per apple (2), yielding the total amount of money that the three people will pay for their share of 5 apples. 
print(f"they would each pay ${2 * 5}.")
