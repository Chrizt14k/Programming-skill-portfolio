import random
from tkinter import *

# Create the main window
root = Tk()
root.title("Exercise 2 - Alexa tell me a joke")
root.geometry("500x300")
root.configure(bg="#f3a155")


#Function to load jokes from a file
def load_jokes(filename):
    with open(filename, 'r') as file:
        jokes = file.readlines()  #Read jokes from the randomJokes.txt file
    return [joke.strip().split('?') for joke in jokes]  #splits the jokes into setup and punchline


#Function to display a random joke to the user
def tell_joke():
    joke = random.choice(jokes)  #Choosing a random joke to show
    setup, punchline = joke[0], joke[1]  #split into setup and punchline
    setup_label.config(text=f"{setup}?")  #display the setup 
    punchline_label.config(text="")  #Clear the punchline
    punchline_button.config(command=lambda: show_punchline(punchline))  #Set-up punchline button for the user
#the first part of the joke should always end with a question mark? and it will be followed up with the punchline and end it with period. 
#to make it work and so the system can split between the joke and punchline
#Function to show the punchline
def show_punchline(punchline):
    punchline_label.config(text=f"{punchline}")  #Displays the punchline

def main():
    global jokes, setup_label, punchline_label, punchline_button
    #Loads and read the jokes from the randomJokes.txt file
    jokes = load_jokes(r"C:\Users\altar\Documents\VS Code phyton\CC5 - advance prog\randomJokes.txt")

    #Create and place labels and buttons in the main window
    Label(root, text="Alexa, tell me a joke", bg="#f3a155", fg="white", font=("tahoma", 16)).pack(pady=10)
    setup_label = Label(root, text="", bg="#f3a155", fg="white", font=("tahoma", 14)) #show the first part of the joke
    setup_label.pack(pady=10)
    punchline_button = Button(root, text="Show Punchline", font=("tahoma", 12)) #button to show the punchline of the joke
    punchline_button.pack(pady=10)
    punchline_label = Label(root, text="", bg="#f3a155", fg="white", font=("tahoma", 14)) #showing the punchline of the joke after clicking the show punchline button 
    punchline_label.pack(pady=10)
    Button(root, text="Next Joke", command=tell_joke, font=("tahoma", 12)).pack(pady=10) #button to show the next joke
    Button(root, text="Quit", command=root.quit, font=("tahoma", 12)).pack(pady=10) #button if to quit if the user wants to quit

    tell_joke()  #Display the first joke
    root.mainloop()  
if __name__ == "__main__":
    main()
