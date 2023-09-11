# age = int(input("How old are you?"))
# drink = 2
#
#
#
# print(type(age))
#
# if age < 18:
#     print("you cant drink")
# elif age > 18 and age < 35:
#     print("you drink beer!")
# elif age == 60 or age == 70:
#     print("birthday party")
# else:
#     print("GO ahead!")


from random import randint



print("welcome to python casino")
# pc_choice = int(input("Choose numbre :"))



pc_choice = randint(1,10) # I imported this

playing = True

while playing:
    user_choice = int(input("choose number."))
    if user_choice == pc_choice:
        print("you win")
        playing = False
    elif user_choice > pc_choice:
        print("Lower!")
    elif user_choice < pc_choice:
        print("Higher computer chose")

