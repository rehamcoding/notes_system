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
        return f"{self.title} | {self.timestamp.strftime("%Y-%m-%d")}"


class User:
    def __init__(self, name):
        self.name = name
        self.notebook = Notebook()

    def add_note(self, title, content="Nothing"):
        note = Note(title, content)
        self.notebook.store_note(note)

    def check_note(self):
        self.notebook.list_notes()

    def display_note(self,index):
        self.notebook.display_note(index)

    def delete_note(self, index):
        self.notebook.delete_note(index)



class Notebook:
    def __init__(self):
        self.notes = []

    def store_note(self, note):
        self.notes.append(note)

    def list_notes(self):
        if not self.notes:
            print("Your notebook is empty.\n")
            return
        print(f"\nYour Notes:")
        for index, note in enumerate(self.notes, start=1):
            print(f"{index}- {note}")

    def display_note(self, index):
        if not self.notes:
            print("Your notebook is empty")
            return
        actual_index = index - 1
        if actual_index >= len(self.notes) or actual_index < 0:
            print("Invalid note number.\n")
            return
        self.notes[actual_index].display_full_note()

    def delete_note(self,index):
        if not self.notes:
            print("Yuor notebook is empty.")
            return
        actual_index = index - 1
        if actual_index >= len(self.notes) or actual_index < 0:
            print("Invalid note number.")
            return
        name_note = self.notes[actual_index].title
        del self.notes[actual_index]
        print(f"'{name_note}' deleted.\n")


