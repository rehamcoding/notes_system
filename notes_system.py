import datetime

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content 
        self.timestamp = datetime.datetime.now()

    def display_full_note(self):
        print(f"""
--- Note ---
              
Title: {self.title}

Content: {self.content}
""")

    def __str__(self):
        return f"{self.title} | {self.timestamp.strftime('%Y-%m-%d')}"


class User:
    def __init__(self, name):
        self.name = name
        self.notebook = Notebook()

    def add_note(self, title, content="Nothing"):
        note = Note(title, content)
        self.notebook.store_note(note)

    def _safe_action(self, action, *args):
        try:
            action(*args)
        except (IndexError, ValueError, TypeError) as e:
            print(e)
    
    def view_notes(self):
        self._safe_action(self.notebook.list_notes)

    def update_note(self,index, choice, value):
        self._safe_action(self.notebook.update_note, index, choice, value)

    def delete_note(self, index):
        self._safe_action(self.notebook.delete_note, index)



class Notebook:
    def __init__(self):
        self.notes = []

    def store_note(self, note):
        self.notes.append(note)

    def list_notes(self):
        if not self.notes:
            raise ValueError("Notebook is empty.")
        print(f"\nYour Notes:")
        for index, note in enumerate(self.notes, start=1):
            print(f"{index}- {note}")

    def update_note(self, index, field, new_value):
        if not self.notes:
            raise ValueError("Notebook is empty")
        
        actual_index = int(index) - 1

        if actual_index >= len(self.notes) or actual_index < 0:
            raise IndexError("Invalid note number.")
        #self.notes[actual_index].display_full_note()
        obj = self.notes[actual_index]
        if field not in ("title", "content"):
            raise ValueError("You can only update title or content.")
        setattr(obj, field, new_value)


    def delete_note(self,index):
        if not self.notes:
            raise ValueError("Notebook is empty.")
        actual_index = index - 1
        if actual_index >= len(self.notes) or actual_index < 0:
            raise IndexError("Invalid note number.")
        name_note = self.notes[actual_index].title
        del self.notes[actual_index]
        print(f"'{name_note}' deleted.\n")



def create_user():
    name = input("Enter your name: ")    
    return User(name)

def add_note(user):
    title = input("Enter title: ")
    content = input("Enter content: ") 
    user.add_note(title, content)

def update_note(user):
    index = input("Enter note number to update: ")
    field = input("Update title or content: ").lower()
    new_value = input(f"Enter new {field}: ")
    user.update_note(index, field, new_value)

def delete_note(user):
    index = int(input("Enter note number to delete: "))
    user.delete_note(index)


def main():
    user = create_user()

    while True:
        print("\nMenu [A]dd | [U]pdate | [V]iew | [D]elete | [Q]uit")
        choice = input("Choose an option: ").lower()

        if choice == "a":
            add_note(user)
        elif choice == "u":
            update_note(user)
        elif choice == "v":
            user.view_notes()
        elif choice == "d":
            delete_note(user)
        else:
            break
    

