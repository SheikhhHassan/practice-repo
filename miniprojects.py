# BEGINNER LEVEL

# Basic Calculator

# def calculator(x, y, o):
#     if o == "+":
#         return x + y
#     elif o == "-":
#         return x - y
#     elif o == "/":
#         return x / y
#     elif o == "*":
#         return x * y
#     else:
#         print("Error!")

# print(calculator(4, 5, "/"))

# Even / Odd Counter

# def even_odd_counter(arr):
#     e, o = 0, 0
#     for el in arr:
#         if el % 2 == 0:
#             e += 1
#         else:
#             o += 1
                
#     return f"Even: {e}, Odd: {o}"

# nums = [x for x in range(15)]
# print(even_odd_counter(nums))    


# Word Counter

# def word_counter(sentence):
#     lenght = len(sentence)
#     for el in sentence:
#         if el == " ":
#             lenght -= 1
#     return lenght

# line = "Hi! I'm learning python."
# print(word_counter(line))            


# INTERMEDIATE LEVEL

# Number Guessing Game

# import random

# def guess_number_game():
#     secret_number = random.choice((range(1, 10)))
#     while True:
#         guessed_number = int(input("Enter a number: "))
#         if guessed_number == secret_number:
#             return print("you won!")
#         else:
#             print("Try Again!")

# guess_number_game()            

# Password Genrator

# import random

# def pass_genrator(pass_len):
#     pass_word = ""
#     ans = ["0","a","b","c","d","e", "1", "2", "3", "4", "5", "6", "7", "8", "9","!", "@", "#", "$", "%", "^", "&", "~"]

#     for el in range(pass_len): # for-loop
#         el = random.choice(ans)
#         pass_word += el

#     count = 0  
#     while count != pass_len: # while-loop
#         pass_word += random.choice(ans)
#         count += 1
#     return pass_word

# print(f"Password: {pass_genrator(8)}")        

# To-DO List(CLI):

# class to_do_list():
#     def __init__(self):
#         self.__tasks = []

#     def add_task(self, task):
#         self.__tasks.append(task)

#     def view_tasks(self):
#         print(self.__tasks)

#     def delete_task(self, task):
#         self.__tasks.remove(task)
                            

# list = to_do_list()
# list.add_task("Python") # Adding Tasks in a list
# list.add_task("Exercise")
# list.add_task("5 Prayers")
# list.add_task("Sleep")
# list.view_tasks()  # Viewing all tasks
# list.delete_task("Python") # deleting a task
# list.view_tasks() # Viewing all tasks again


# Students Marks System (using dictonaries)

# students = {}
# user_input = int(input("How many Students: "))
# for i in range(user_input):
#     name = input("Student name: ")  
#     marks = int(input("enter marks: "))
#     students[name] = marks

# highest = max(students, key=students.get)
# lowest = min(students, key=students.get)
# average = sum(students.values()) / len(students) 

# print(highest)
# print(lowest)
# print(average)    

# Function

# def greet(name):
#     return f"Hello {name}"

# greet("Hassan")