#!user/bin/env python3

userScore = int(input("Please enter the grade: "))

if 100 >= userScore >= 90:
    print(f"The score {userScore} is A!!!")
elif 89 >= userScore >= 80:
    print(f"The score {userScore} is B!!!")
elif 79 >= userScore >= 70:
    print(f"The score {userScore} is C!!!")
elif userScore <= 69 <= userScore:
    print(f"The score {userScore} is D!!!")
elif userScore <= 60:
    print(f"The score {userScore} is F :(")
else:
    print("Please enter a number from 1 to 100")

# if 91 > userScore < 100:
#     print(f"The score {userScore} is A!!!")
# elif 89 >= userScore <= 80:
#     print(f"The score {userScore} is B!!!")
# elif 79 >= userScore <= 70:
#     print(f"The score {userScore} is C!!!")
# elif 69 >= userScore <= 60:
#     print(f"The score {userScore} is D!!!")
# elif userScore >= 60:
#     print(f"The score {userScore} is F :(")
# else:
#     print("Please enter a number from 1 to 100")
