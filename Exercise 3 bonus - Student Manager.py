import tkinter as tk  
from tkinter import messagebox, simpledialog  

root = tk.Tk()  #Creating main window
root.title("Student Management System")#title of the main window
root.geometry("800x700")#size of the window
root.configure(bg="#FE912D")#bg color

#defining the Student class to store student information
class Student:
    def __init__(self, number, name, coursework1, coursework2, coursework3, exam_mark):
        self.number = number  #storing student ID number
        self.name = name  #storing student name
        self.coursework_mark = coursework1 + coursework2 + coursework3  #summing up the 3 coursework marks
        self.exam_mark = exam_mark#Storing the exam mark
        self.total_score = self.coursework_mark + exam_mark#calculating total score from the 3coursework and the exam
        self.percentage = (self.total_score / 160) * 100#calculating the percentage
        self.grade = self.calculate_grade()  #determining grade based on percentage

    #calculating the grade based on the percentage of the student
    def calculate_grade(self):
        if self.percentage >= 70:#if percentage is 70 or above then the grade is A
            return 'A'
        elif self.percentage >= 60: #if percentage is 60 or above then the grade is B
            return 'B'
        elif self.percentage >= 50:#if percentage is 50 or above then grade is C
            return 'C'
        elif self.percentage >= 40:#if percentage is 40 or above then the grade is D
            return 'D'
        else:#if percentage is below 40 then the student fail and it will show F
            return 'F'

#function to load student data from the file
def load_students_from_file(filename):
    students = [] #creating an empty list to store student
    with open(filename, 'r') as file:#opening the file as a read mode
        for line in file: #reading each line in the file
            number, name, coursework1, coursework2, coursework3, exam_mark = line.strip().split(',')#splitting line into components for the student
            students.append(Student(number, name, int(coursework1), int(coursework2), int(coursework3), int(exam_mark))) #creating and adding a Student object to the list
    return students#returning the list of students

#function to save student data to the file
def save_students_to_file(filename, students):
    with open(filename, 'w') as file:#opening the file in write mode
        for student in students:
            file.write(f"{student.number},{student.name},{student.coursework_mark // 3},{student.coursework_mark // 3},{student.coursework_mark // 3},{student.exam_mark}\n")#writing student data to file

file_path = (r"C:\Users\altar\Documents\VS Code phyton\CC5 - advance prog\studentMarks.txt") #path to the data file
students = load_students_from_file(file_path)#loading student data from the file

#function to view all student records
def view_all_records():
    output_box.delete(1.0, tk.END)  #clearing the output box
    for student in students:  
        output_box.insert(tk.END, f"Number: {student.number}\nName: {student.name}\n"
                                  f"Coursework Mark: {student.coursework_mark}\nExam Mark: {student.exam_mark}\n"
                                  f"Overall Percentage: {student.percentage:.2f}%\nGrade: {student.grade}\n\n")#displaying student details
    output_box.insert(tk.END, f"Total Students: {len(students)}\n"  #displaying the total number of students that is in the file record
                              f"Average Percentage: {sum(s.percentage for s in students) / len(students):.2f}%\n")#Displaying the average percentage of the students

#function to view an individual student's record
def view_individual_record():
    number = student_number_entry.get()#getting the student number from entry field
    output_box.delete(1.0, tk.END)#Clearing the output box
    for student in students: 
        if student.number == number:  #checking if student number matches in the record
            output_box.insert(tk.END, f"Number: {student.number}\nName: {student.name}\n"
                                      f"Coursework Mark: {student.coursework_mark}\nExam Mark: {student.exam_mark}\n"
                                      f"Overall Percentage: {student.percentage:.2f}%\nGrade: {student.grade}\n")  #displaying student details
            return  #exiting the loop once the student record is found
    messagebox.showerror("Error", "Student not found")#showing error message if the student is not found

#function to show the student with the highest total score
def show_highest_score():
    highest = max(students, key=lambda s: s.total_score)#finding the student with the highest score
    output_box.delete(1.0, tk.END)#Clearing the output box
    output_box.insert(tk.END, f"Student with Highest Score:\nNumber: {highest.number}\nName: {highest.name}\n"
                              f"Total Score: {highest.total_score}\n")  #Displaying the student with the highest score

#same code with the highest total score but in here we are looking for the student with the lowest score
#function to show the student with the lowest total score
def show_lowest_score():
    lowest = min(students, key=lambda s: s.total_score)#finding the student with the lowest score
    output_box.delete(1.0, tk.END)#Clearing the output box
    output_box.insert(tk.END, f"Student with Lowest Score:\nNumber: {lowest.number}\nName: {lowest.name}\n"
                              f"Total Score: {lowest.total_score}\n")#displaying the student with the lowest score

#function to add a new student record to the list
def add_student_record():
    number = simpledialog.askstring("Input", "Enter student number:")#asking for the student number
    name = simpledialog.askstring("Input", "Enter student name:")#asking for the student name
    coursework1 = int(simpledialog.askstring("Input", "Enter coursework mark 1 (out of 20):"))#asking for the student coursework 1 mark
    coursework2 = int(simpledialog.askstring("Input", "Enter coursework mark 2 (out of 20):"))#asking for coursework 2 mark
    coursework3 = int(simpledialog.askstring("Input", "Enter coursework mark 3 (out of 20):"))#asking for coursework 3 mark
    exam_mark = int(simpledialog.askstring("Input", "Enter exam mark (out of 100):"))#asking for the exam mark
    students.append(Student(number, name, coursework1, coursework2, coursework3, exam_mark))#adding new student to the list
    save_students_to_file(file_path, students)#saving the updated student list to file
    messagebox.showinfo("Success", "Student record added successfully")#showing success message

#function to delete a student record in the list
def delete_student_record():
    number = simpledialog.askstring("Input", "Enter student number to delete:")#asking for the student number to delete
    global students#referencing the global students list
    students = [student for student in students if student.number != number]#removing the student from the list
    save_students_to_file(file_path, students)#saving the updated list to file
    messagebox.showinfo("Success", "Student record deleted successfully")#showing success message after the student has been deleted
    
#function to update the details of an existing student in the list
def update_student_record():
    number = simpledialog.askstring("Input", "Enter student number to update:")
    for student in students:
        if student.number == number:
            student.name = simpledialog.askstring("Input", "Enter new student name:", initialvalue=student.name)
            student.coursework_mark = int(simpledialog.askstring("Input", "Enter new coursework mark 1 (out of 20):")) + \
                                      int(simpledialog.askstring("Input", "Enter new coursework mark 2 (out of 20):")) + \
                                      int(simpledialog.askstring("Input", "Enter new coursework mark 3 (out of 20):"))
            student.exam_mark = int(simpledialog.askstring("Input", "Enter new exam mark (out of 100):"))
            student.total_score = student.coursework_mark + student.exam_mark
            student.percentage = (student.total_score / 160) * 100
            student.grade = student.calculate_grade()
            save_students_to_file(file_path, students)
            messagebox.showinfo("Success", "Student record updated successfully")
            return
    messagebox.showerror("Error", "Student not found")

# Function to sort student records by different criteria
def sort_student_records():
    global students
    sort_by = simpledialog.askstring("Input", "Sort by (number/name/total_score):")
    if sort_by == "number":
        students.sort(key=lambda s: s.number) #sorting for student number
    elif sort_by == "name":
        students.sort(key=lambda s: s.name) #sorting for student names
    elif sort_by == "total_score":
        students.sort(key=lambda s: s.total_score, reverse=True) #sorting for the total score and showing first with the student with the highest score
    else:
        messagebox.showerror("Error", "Invalid sort option") #invalid sort option
        return
    view_all_records()  #display sorted records

#buttons hehe
frame = tk.Frame(root)
frame.pack(pady=10)
view_all_button = tk.Button(frame, text="View All Student Records", command=view_all_records)
view_all_button.grid(row=0, column=0, padx=5, pady=5)
#label for entering the student number
student_number_label = tk.Label(frame, text="Student Number:")
student_number_label.grid(row=1, column=0, padx=5, pady=5)#positioning the label in the grid

#entry box to input the student number for individual record lookup
student_number_entry = tk.Entry(frame)
student_number_entry.grid(row=1, column=1, padx=5, pady=5)#positioning the entry box in the grid

#A button to view individual student's record
view_individual_button = tk.Button(frame, text="View Individual Student Record", command=view_individual_record)
view_individual_button.grid(row=1, column=2, padx=5, pady=5)#positioning the button in the grid

#button to show the student with the highest total score
highest_score_button = tk.Button(frame, text="Show Student with Highest Total Score", command=show_highest_score)
highest_score_button.grid(row=2, column=0, padx=5, pady=5)  
#button to show the student with the lowest total score
lowest_score_button = tk.Button(frame, text="Show Student with Lowest Total Score", command=show_lowest_score)
lowest_score_button.grid(row=2, column=1, padx=5, pady=5)  

#button to add a new student record in the list
add_student_button = tk.Button(frame, text="Add Student Record", command=add_student_record)
add_student_button.grid(row=3, column=0, padx=5, pady=5)  
#button to delete a student record in the list file
delete_student_button = tk.Button(frame, text="Delete Student Record", command=delete_student_record)
delete_student_button.grid(row=3, column=1, padx=5, pady=5)  
#button to update an existing student record in the file
update_student_button = tk.Button(frame, text="Update Student Record", command=update_student_record)
update_student_button.grid(row=3, column=2, padx=5, pady=5) 
#button to sort the student records
sort_student_button = tk.Button(frame, text="Sort Student Records", command=sort_student_records)
sort_student_button.grid(row=3, column=3, padx=5, pady=5)  

#text box to display student records and program outputs for the user
output_box = tk.Text(root, height=15, width=80)
output_box.pack(pady=10)  


root.mainloop()  
