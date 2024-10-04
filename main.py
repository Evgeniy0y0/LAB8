def add_person(person_data):
  while True:
      group = input("Enter group of new student or 'stop' to return to menu: ")
      if group.lower() == "stop": 
          return person_data
      person_data["Group"] = group
      person_data["Name"] = input("Enter name of student: ")
      person_data["Course"] = input("Enter course of student: ")
      while True:
          discipline = input("Enter discipline or 'stop' to return to menu: ")
          if discipline.lower() == "stop":
                print("----------------")     
                break   
          person_data[discipline, " grades"] = input("Enter grades of this discipline: ")
      return person_data
def show_dict():
    for i in range(0, len(persons)):
        print(persons[i], "\n")
        
count = 0
persons = {}
person_data = {}
while True:
  print("Choose option: " , "\n", "1 - Add person info", "\n", "2 - Show full dictionary", "\n", "3 - Exit")
  ans = int(input())
  if ans == 1:
      person_data = add_person(person_data)
      persons[count] = person_data
      person_data = {}
      count += 1
  if ans == 2:
      show_dict()
  if ans == 3:
      break
