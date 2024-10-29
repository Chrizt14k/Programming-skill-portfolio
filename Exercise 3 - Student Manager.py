import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Student Management System")
root.geometry("800x700")
root.configure(bg="#FE912D")  

#Defining the Student class
class Student:
    def __init__(self, number, name, coursework1, coursework2, coursework3, exam_mark):
        self.number = number  #Student's ID numbers
        self.name = name  #Student's name
        #adding up the marks from the three courseworks
        self.coursework_mark = coursework1 + coursework2 + coursework3
        self.exam_mark = exam_mark  # Mark from the final exam
        #Total score of the sum of courseworks and exam mark
        self.total_score = self.coursework_mark + exam_mark
        # Calculating percentage based on a maximum possible score of 160
        self.percentage = (self.total_score / 160) * 100
        self.grade = self.calculate_grade()  #assigning a grade based on percentage of the student

    def calculate_grade(self):
        # determines the grade based on percentage they get
        if self.percentage >= 70:
            return 'A'
        elif self.percentage >= 60:
            return 'B'
        elif self.percentage >= 50:
            return 'C'
        elif self.percentage >= 40:
            return 'D'
        else:
            return 'F'

#Function to load student data from a file
def load_students_from_file(filename):
    students = []  #creating an empty list to hold all student objects
    with open(filename, 'r') as file:
        for line in file:
            #Reading and splitting each line of the file using ","
            number, name, coursework1, coursework2, coursework3, exam_mark = line.strip().split(',')
            #Creating a new Student object and adding it to the list
            students.append(Student(number, name, int(coursework1), int(coursework2), int(coursework3), int(exam_mark)))
    return students

#Loads the student list from studentMarks.txt file
file_path = (r"C:\Users\altar\Documents\VS Code phyton\CC5 - advance prog\studentMarks.txt")
students = load_students_from_file(file_path)

#displays all student records in the output box
def view_all_records():
    output_box.delete(1.0, tk.END)  #Clear the output box
    for student in students:
        #Inserts student details into the output box
        output_box.insert(tk.END, f"Student Number: {student.number}\nName: {student.name}\n"
                                  f"Coursework Mark: {student.coursework_mark}\nExam Mark: {student.exam_mark}\n"
                                  f"Overall Percentage: {student.percentage:.2f}%\nGrade: {student.grade}\n\n")
    #displays the total number of students and average percentage
    output_box.insert(tk.END, f"Total Students: {len(students)}\n"
                              f"Average Percentage: {sum(s.percentage for s in students) / len(students):.2f}%\n")

#views the record of a single student based on their student number
def view_individual_record():
    number = student_number_entry.get()  #Get the student number from the user entry
    output_box.delete(1.0, tk.END)  #Clear the output box
    for student in students:
        if student.number == number:
            #insert details of the matched student into the output box
            output_box.insert(tk.END, f"Student Number: {student.number}\nName: {student.name}\n"
                                      f"Coursework Mark: {student.coursework_mark}\nExam Mark: {student.exam_mark}\n"
                                      f"Overall Percentage: {student.percentage:.2f}%\nGrade: {student.grade}\n")
            return
    #Show error message if student number is not found in the list
    messagebox.showerror("Error", "Student number not found")

#function to display the student with the highest total score
def show_highest_score():
    highest = max(students, key=lambda s: s.total_score)  #finds the student with the highest score
    output_box.delete(1.0, tk.END)  #Clear the output box
    #inserts the details of the highest scoring student
    output_box.insert(tk.END, f"Student with Highest Score:\nNumber: {highest.number}\nName: {highest.name}\n"
                              f"Total Score: {highest.total_score}\n")

#Function to display the student with the lowest total score
def show_lowest_score():
    lowest = min(students, key=lambda s: s.total_score)  #Find the student with the lowest score
    output_box.delete(1.0, tk.END)  #Clear the output box
    #inserts the details of the low scoring student
    output_box.insert(tk.END, f"Student with Lowest Score:\nNumber: {lowest.number}\nName: {lowest.name}\n"
                              f"Total Score: {lowest.total_score}\n")

#buttons and labels for the main window.
frame = tk.Frame(root)
frame.pack(pady=10)
view_all_button = tk.Button(frame, text="View All Student Records", command=view_all_records) #button for the view all student
view_all_button.grid(row=0, column=0, padx=5, pady=5)
student_number_label = tk.Label(frame, text="Student Number:") 
student_number_label.grid(row=1, column=0, padx=5, pady=5)
student_number_entry = tk.Entry(frame) #for the user to enter the student number
student_number_entry.grid(row=1, column=1, padx=5, pady=5)
view_individual_button = tk.Button(frame, text="View Individual Student Record", command=view_individual_record) #will show a single student 
view_individual_button.grid(row=1, column=2, padx=5, pady=5)
highest_score_button = tk.Button(frame, text="Show Student with Highest Total Score", command=show_highest_score) #will show the student with the highest score
highest_score_button.grid(row=2, column=0, padx=5, pady=5)
lowest_score_button = tk.Button(frame, text="Show Student with Lowest Total Score", command=show_lowest_score) #will show the student with the lowest score
lowest_score_button.grid(row=2, column=1, padx=5, pady=5)
output_box = tk.Text(root, height=15, width=80) #the text box for the labels and text
output_box.pack(pady=10)

root.mainloop()
