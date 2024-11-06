# Функція для додавання нового студента в словник
def add_person(person_data): 
    while True:
        group = input("Enter group of new student or 'stop' to return to menu: ")
        if group.lower() == "stop": 
            return person_data
        
        person_data["Group"] = group
        person_data["Name"] = input("Enter name of student: ")
        person_data["Course"] = input("Enter course of student: ")
        
        # Створюємо словник для дисциплін та оцінок
        disciplines = {}
        
        while True:
            discipline = input("Enter discipline or 'stop' to return to menu: ")
            if discipline.lower() == "stop":
                print("----------------")     
                break   
            
            grade = input(f"Enter grades for {discipline}: ")
            disciplines[discipline] = grade
        
        # Додаємо дисципліни до словника студента
        person_data["Disciplines"] = disciplines
        return person_data

# Функція для показу всіх студентів у словнику
def show_dict():
    for i in range(0, len(persons)):
        print(f"Student ID: {i}")
        print(persons[i], "\n")

# Функція для видалення студента з словника за ID
def delete_person(): 
    try: # Запитуємо у користувача ID студента, якого потрібно видалити
        student_id = int(input("Enter the ID of the student to delete: "))
        if student_id in persons: # Перевіряємо, чи існує студент з таким ID
            del persons[student_id]
            print(f"Student with ID {student_id} has been deleted.")
        else:
            print(f"Student with ID {student_id} not found.")
    except ValueError: # Випадок, коли користувач ввів неправильний ID (не ціле число)
        print("Invalid input. Please enter a valid student ID.")

# Функція для сортування студентів за курсом
def sort_students_by_course():
    # Сортуємо список студентів за їхнім курсом
    sorted_persons = sorted(persons.items(), key=lambda x: x[1]["Course"])
    
    # Виводимо відсортовані дані
    for student_id, student_data in sorted_persons:
        print(f"Student ID: {student_id}, Name: {student_data['Name']}, Group: {student_data['Group']}, Course: {student_data['Course']}")

# Функція для редагування оцінки дисципліни
def edit_grade():
    try:
        student_id = int(input("Enter the ID of the student whose grade you want to edit: "))
        if student_id in persons:  # Перевірка на наявність студента в списку
            discipline = input("Enter the name of the discipline: ")
            if discipline in persons[student_id]["Disciplines"]:  # Перевірка на наявність дисципліни
                new_grade = input(f"Enter the new grade for {discipline}: ")
                persons[student_id]["Disciplines"][discipline] = new_grade
                print(f"The grade for {discipline} has been updated to {new_grade}.")
            else:
                print(f"No discipline named {discipline} found for this student.")
        else:
            print(f"Student with ID {student_id} not found.")
    except ValueError:
        print("Invalid input. Please enter a valid student ID.")

# Основна частина програми
count = 0
persons = {}
person_data = {}

while True:
    print("Choose option: ", "\n", "1 - Add person info", "\n", "2 - Show full dictionary", "\n", "3 - Delete student", "\n", "4 - Sort students by course", "\n", "5 - Edit grade", "\n", "6 - Exit")
    ans = int(input())
    if ans == 1:
        person_data = add_person(person_data)
        persons[count] = person_data
        person_data = {}
        count += 1
    elif ans == 2:
        show_dict()
    elif ans == 3:
        delete_person()
    elif ans == 4:
        sort_students_by_course()
    elif ans == 5:
        edit_grade()
    elif ans == 6:
        break
