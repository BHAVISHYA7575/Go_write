# global variable to store notes 
notes = []

#function defintions
def create_note():
    title = input("Enter the title of the new note: ")
    content = input("Enter the content of the new note:")
    new_note = {"title": title,"content": content}
    notes.append(new_note )
    print("Note created successfully!")

def edit_note():
    print("select a note to edit:")
    display_notes()
    note_index = int(input("Enter the index of the note you want to edit:"))
    if 0 <= note_index < len(notes):
        new_title = input("Enter the new title for the note: ")
        new_content = input("Enter the new content for the note: ")
        notes[note_index]["title"] = new_title
        notes[note_index]["content"] = new_content
        print("Note edited successfully!")
    else:
        print("Invalid note index. Please try again.")

def delete_note():
    print("Select a note to delete: ")
    display_notes()
    note_index = int(input("Enter the index of the note you want to delete:"))
    if 0 <= note_index < len(notes):
     del notes[note_index]
     print("Note deleted successfully! ")
    else:
     print("Invalid note index.Please try again.")

def view_note():
    print("All notes:")
    display_notes()

def display_notes():
    for index , note in enumerate(notes):
     print(f"{index}:{note['title']}")
     print(note['content'])
     print()

# main logic 

while True:
   print("Select an option:")
   print("1. Create a new note")
   print("2. Edit an existing note")
   print("3. Delete a note")
   print("4. View all notes")
   print("5. Exit")

   choice = input("Enter your choice:")

   if choice == '1':
      create_note()
   elif choice == '2':
      edit_note()
   elif choice  == '3':
      delete_note()
   elif choice == '4':
      view_note()
   elif choice == '5':
      print("Existing the notes app. ")
      break
   else:
      print("Invalid chocie.please try again.")







#display a menu of options to the user
def display_menu():
   print("1. Create a new note ")
   print("2. Edit a note")
   print("3. Delete a note")
   print("4. View all notes")
   print("5. Exit")

# function to handle user input and execute corresponding functionality
def handle_input():
   while True:
      choice = input("Enter your chocie (1-5):")
      if choice == '1':
         create_note()
      elif choice == '2':
         edit_note()
      elif choice == '3':
         delete_note()
      elif choice == '4':
         view_note()
      elif choice == '5':
         print("Existing the program...")
         break
      else:
         print("Invalid choice.Please enter a number between 1 and 5.")

#main function to start the program 
def main():
   while True:
      display_menu()
      handle_input()

if __name__ == " _main_ ":
   main()      




#open the text file for writing 
with open ('notes.txt','w') as file:
   pass # Placeholder , we'll add content later 




import os
def create_note():
   title = input("Enter the title of the new note: ")
   content = input("Enter the content of the new note: ")
   with open('notes.txt' , 'a') as file:
      file.write(f"{title}\n{content}\n\n")

def read_notes():
 with open('notes.txt','r')as file:
  notes = file.readlines()
 for i in range(0,len(notes),3):
    print(f"Title:{notes[i].strip()}")
    print(f"Content:{notes[i+1].strip()}\n")

def edit_note():
   title_to_edit = input("Enter the title of the note to edit: ")
   content_to_edit = input("Enter the new content for the note: ")
   with open('notes.txt' , 'r') as file:
      lines = file.readlines()
      with open('notes.txt' , 'w') as file:
         for i in range(0,len(lines),3):
            title = lines[i].strip()
            content = lines[i+1].strip()
            if title == title_to_edit:
               file.write(f"{title}\n{content_to_edit}\n\n")
            else:
               file.write(f"{title}\n{content}\n\n")

def delete_note():
   title_to_delete = input("Enter the title of the note to delete: ")
   with open('notes.txt','r')as file:
      lines = file.readline()
      with open('notes.txt' , 'w')as file:
       for i in range(0,len(lines),3):
          title = lines[i].strip()
          content = lines[i+1].strip()
          if title != title_to_delete:
             file.write(f"{title}\n{content}\n\n")

def main():
   while True:
      print("\nNotes App Menu:")
      print("1. Create a new note")
      print("2. Read existing notes")
      print("3. Edit a note")
      print("4. Delete a note")
      print("5. Exit")

      choice = input("Enter your choice (1-5): ")
      if choice == '1':
         create_note()
      elif choice == '2':
         read_notes()
      elif choice == '3':
         edit_note()
      elif choice == '4':
         delete_note()
      elif choice == '5':
         print("Existing Notes App.Goodbye!")
         break
      else:
         print("Invalid choice.Please enter a number from 1 to 5.")

if __name__ == "_main_":
 if not os.path.exists('notes.txt'):
  open('notes.txt','w').close()

 # create an empty notes file if it doesn't exist 
main()






import os
# global variable to store notes
notes = []

# function definitions 
def create_note():
   title = input("Enter the title of the new note: ")
   content = input("Enter the content of the new note: ")
   new_note = {"title":title,"content":content}
   notes.append(new_note)
   print("Note created successfully!")

def edit_note():
   print("Select a note to edit:")
   display_notes()
   try: 
      note_index = int(input("Enter the index of the note you want to edit :"))
      if 0 <= note_index < len(notes):
         new_title = input("Enter the new title for the note: ")
         new_content = input("Enter the new content for the note: ")
         notes[note_index]["title"] = new_title
         notes[note_index]["content"]= new_content
         print("Note edited successfully!")
      else:
         print("Invalid note index.Please try again.")
   except ValueError:
      print("Invalid input.Please enter a valid index.")

def delete_note():
   print("Select a note to delete:")
   display_notes()
   try:
      note_index = int(input("Enter the index of the note you want to delete: "))
      if 0 <= note_index < len(notes):
         del notes[note_index]
         print("Note deleted successfully!")
      else:
         print("Invalid note index.Please try again.")
   except ValueError:
      print("Invalid input.Please enter a valid index.")

def view_notes():
   print("All notes:")
   display_notes()

def display_notes():
   for index,note in enumerate(notes):
      print(f"{index}:{note['title']}")
      print(note['content'])
      print()

# main logic
def main():
   while True:
      print("Select an option:")
      print("1. Create Note")
      print("2. Edit Note")
      print("3. Delete Note")
      print("4. View Notes")
      print("5. Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
         create_note()
      elif choice == "2":
         edit_note()
      elif choice == "3":
         delete_note()
      elif choice == "4":
         view_notes()
      elif choice == "5":
         print("Existing...")
         break
      else:
         print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "_main_":
   main()



def create_note():
   title = input("enter the title of the new note:")
   content = input("enter the content of the new note:")
   with open ("notes.txt" , "a") as file :
      file.write(f"{title}\n{content}\n\n")
      print("note created successfully!")

def view_notes():
   print("all notes:")
   with open ("notes.txt" , "r") as file :
      notes = file.readlines()
      for i in range (0,len(notes) , 3):
         print(f"title:{notes[i].strip()}")
         print(f"content:{notes[i+1].strip()}")
         print()

def edit_note():
   view_notes()
   note_index = int(input("enter the index of the note you want to edit:"))
   with open ("notes.txt" , "r") as file :
      notes = file.readline()
      if 0 <= note_index < len (notes) / 3 :
       new_title = input("enter the new title for the note :")
       new_content = input("enter the new content for the note :")
       notes[note_index*3] = new_title + '\n'
       notes[note_index*3 + 1] = new_content + '\n'
       with open ("notes.txt" ,"w") as file :
          file.writelines(notes)
          print("note edited successfully!")
      else:
       print ("invalid note index , please try again, ") 

def delete_notes():
   view_notes()
   note_index = int(input("enter the index of the note you want to delete:"))
   with open ("notes.txt" , "r") as file :
      notes = file.readlines()
      if 0 <= note_index < len(notes) / 3 :
         del notes[note_index*3:note_index*3 +3]
         with open ("notes.txt" , "w") as file :
            file.writelines(notes)
            print("note deleted successfully!")
      else:
          print("invalid note index. please try again. ")



import tkinter as tk

# define functions for the notes app 
def create_note():
   # add functionality to create a new note 
   pass

def edit_note():
   # add functionality to edit an existing note 
   pass

def view_note():
   # add functionality to view all notes 
   pass

def delete_note():
   # add functionality to delete a note 
   pass

def main():
   while True:
      # prompt the user for input 
      command = input("enter a command (create/edit/view/delete/exit):").strip().lower()

      # perform actions based on user input
      if command == "create":
       create_note()
      elif command == "edit":
       edit_note()
      elif command == "view":
       view_notes()
      elif command == "delete":
       delete_note()
      elif command == "exit":
       print("exisitng the program goodbye!")
      break
   else:
    print("invalid command.please try again.")

   if __name__ == "_main_":
      main()


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class NotesApp(App):
 def build(self):
  layout = BoxLayout(orientation='vertical')

    # User Interface
    title_label = Label(text='Notes App', size_hint=(1, 0.1))
    layout.add_widget(title_label)

    notes_label = Label(text='Your Notes:', size_hint=(1, 0.1))
    layout.add_widget(notes_label)

    # Buttons for CRUD operations
    add_button = Button(text='Add Note', size_hint=(1, 0.1))
    add_button.bind(on_press=self.add_note)
    layout.add_widget(add_button)

    edit_button = Button(text='Edit Note', size_hint=(1, 0.1))
    edit_button.bind(on_press=self.edit_note)
    layout.add_widget(edit_button)

    delete_button = Button(text='Delete Note', size_hint=(1, 0.1))
    delete_button.bind(on_press=self.delete_note)
    layout.add_widget(delete_button)

    view_button = Button(text='View Notes', size_hint=(1, 0.1))
    view_button.bind(on_press=self.view_notes)
    layout.add_widget(view_button)

    return layout

# Functionality for CRUD operations
def add_note(self, instance):
    # Add functionality to add a new note
    pass

def edit_note(self, instance):
    # Add functionality to edit an existing note
    pass

def delete_note(self, instance):
    # Add functionality to delete a note
    pass

def view_notes(self, instance):
    # Add functionality to view all notes
    pass

if __name__== '**main**': NotesApp().run()