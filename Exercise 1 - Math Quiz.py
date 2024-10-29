from tkinter import *  
import tkinter.messagebox 
import random 


root = Tk() 
root.title("Exercise 1 - Math Quiz") #name of the main window
root.geometry("500x500")  #size of the main window
root.configure(bg="#FE912D")  #bg color

score = 0  #set the score variable of the user
question_count = 0  # initializing the question variable
difficulty = 1  #set the value difficulty of the level variable for the user



def displayMenu():
    global difficulty
    menu_frame = Frame(root, bg="#f3a155")  #creating a frame for the menu
    menu_frame.pack(pady=50)  #packing the frame with padding

    #Labels and buttons for the difficulty level for easy, moderate, and advance
    Label(menu_frame, text="DIFFICULTY LEVEL", bg="#f3a155", fg="white", font=("tahoma", 16)).pack()
    Button(menu_frame, text="Easy", command=lambda: setDifficulty(1, menu_frame), font=("tahoma", 12)).pack(pady=5)
    Button(menu_frame, text="Moderate", command=lambda: setDifficulty(2, menu_frame), font=("tahoma", 12)).pack(pady=5)
    Button(menu_frame, text="Advanced", command=lambda: setDifficulty(3, menu_frame), font=("tahoma", 12)).pack(pady=5)


def setDifficulty(level, frame):
    global difficulty
    difficulty = level  #setting the difficulty level for the user
    frame.destroy()  #destroying the menu frame for the next page
    nextQuestion()  #proceeding to the next question


def randomInt():
    #gnerating random integers based on the difficulty level of the user
    if difficulty == 1:  #for easy level
        return random.randint(1, 9)
    elif difficulty == 2:   #for moderate level
        return random.randint(10, 99)
    else:    #for advance level
        return random.randint(1000, 9999)



def decideOperation():
    return random.choice(['+', '-'])  #randomly choosing between addition and subtraction for the question


def displayProblem():
    global question_count
    if question_count < 10:  #checking if the quiz is still ongoing
        num1 = randomInt()  #generating the first number for the question
        num2 = randomInt()  #generating the second number for the question
        operation = decideOperation()  #Deciding the operation( + or - )
        if operation == '-' and num1 < num2: #Ensuring no negative results for subtraction
            num1, num2 = num2, num1 
        question = f"{num1} {operation} {num2} = "  #Forming the question string
        return question, eval(question[:-2])  #returning the question and its answer
    else:
        displayResults()  #displaying the results if quiz is over



def checkAnswer(user_answer, correct_answer, attempt):
    global score
    if user_answer == correct_answer:
        if attempt == 1:
            score += 10  #Awarding 10 points for the first correct attempt of the user
        else:
            score += 5  #Awarding 5 points for the second correct attempt of theuser
        return True
    return False



def nextQuestion():
    global question_count
    question_count += 1  #incrementing the question count
    question, answer = displayProblem()  #getting the next question and answer

    question_frame = Frame(root, bg="#f3a155")  #creating a frame for the question
    question_frame.pack(pady=50)  #packing the frame with padding

    Label(question_frame, text=question, bg="#f3a155", fg="white", font=("tahoma", 16)).pack()
    user_answer = Entry(question_frame, font=("tahoma", 12))  #creating an entry widget for the user's answer
    user_answer.pack(pady=10)



    def submitAnswer(attempt):
        if checkAnswer(int(user_answer.get()), answer, attempt):
            tkinter.messagebox.showinfo("Correct!", "Correct Answer!")  #Showing a message for correct answer
            question_frame.destroy()  # destroying the question frame
            nextQuestion()  #Proceeding to the next question
        else:
            if attempt == 1:
                tkinter.messagebox.showinfo("Try Again", "Wrong Answer! Try again.")  #Prompting to try again
                submit_button.config(command=lambda: submitAnswer(2))  #Allowing a second attempt for the user if the user did not get the correct answer on the first try
            else:
                tkinter.messagebox.showinfo("Incorrect", f"Wrong Answer! The correct answer was {answer}.")
                question_frame.destroy()  #Destroying the question frame
                nextQuestion()  # proceeding to the next question

    submit_button = Button(question_frame, text="Submit", command=lambda: submitAnswer(1), font=("tahoma", 12))
    submit_button.pack(pady=10)  #packing the submit button with padding



def displayResults():
    result_frame = Frame(root, bg="#f3a155")  #Creating a frame for the results
    result_frame.pack(pady=50)  #packing the frame with padding

    Label(result_frame, text=f"Your final score is: {score}/100", bg="#f3a155", fg="white", font=("tahoma", 16)).pack()
    #Determining the rank based on the score of the user
    if score > 90:
        rank = "A+"
    elif score > 80:
        rank = "A"
    elif score > 70:
        rank = "B"
    elif score > 60:
        rank = "C"
    else:
        rank = "D"
    Label(result_frame, text=f"Your rank is: {rank}", bg="#f3a155", fg="white", font=("tahoma", 16)).pack()

    Button(result_frame, text="Play Again", command=lambda: restartQuiz(result_frame), font=("tahoma", 12)).pack(pady=10)


def restartQuiz(frame):
    global score, question_count
    score = 0  #resetting the score to 0
    question_count = 0  #Resetting the question count
    frame.destroy()  #Destroyig the result frame
    displayMenu()  #Displaying the menu again



displayMenu()
root.mainloop() 
