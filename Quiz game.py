print("Welcome to the quiz game")
variant=input("Select the variant: capitals or writers : ")
marks=0
if (variant=="capitals"):
    print("Question 1: What is the capital of India:")
    answer1=input()
    if(answer1.lower()=="delhi"):
        marks=marks+1
        print("Correct!")
    else:
        print("Incorrect!")
    print("Question 2: What is the capital of United States of America:")
    answer2 = input()
    if (answer2.lower()== "washington dc" ):
        print("Correct!")
        marks = marks + 1
    else:
        print("Incorrect!")
    print("Question 3: What is the capital of United Kingdom:")
    answer3 = input()
    if (answer3.lower()=="london"):
        print("Correct!")
        marks = marks + 1
    else:
        print("Incorrect!")
    marks1 = str(marks)
    print("your total score is: " + marks1 + " out of 3")
    print("your percentage is:", (marks / 3) * 100)
else:
    print("Question 1: Who is the writer of Harry Potter: ")
    answer1 = input()
    if (answer1.lower() == "jk rowling"):
        marks = marks + 1
        print("Correct!")
    else:
        print("Incorrect!")
    print("Question 2: Who is the writer of Should we tell the President: ")
    answer2 = input()
    if (answer2.lower() == "jeffrey archer"):
        marks = marks + 1
        print("Correct!")
    else:
        print("Incorrect!")
    print("Question 3: Who is the writer of The Alchemist")
    answer3 = input()
    if (answer3.lower() == "paulo coelho"):
        marks = marks + 1
        print("Correct!")
    else:
        print("Incorrect!")
    print("Question 4: Who is the writer of The Kane and abel")
    answer4 = input()
    if (answer4.lower() == "jeffrey archer"):
        marks = marks + 1
        print("Correct!")
    else:
        print("Incorrect!")
    print("Question 5: Who is the writer of The Call of the wild")
    answer5 = input()
    if (answer5.lower() == "jack london"):
        marks = marks + 1
        print("Correct!")
    else:
        print("Incorrect!")

    marks1 = str(marks)
    print("your total score is: " + marks1 + " out of 5")
    print("your percentage is:", (marks / 5) * 100)





