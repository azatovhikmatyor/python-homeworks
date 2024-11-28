import json
from datetime import datetime

class Note:
    def __init__(self, note_id, text, created_date):
        self.id = note_id
        self.text = text
        self.created_date = created_date

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'created_date': self.created_date
        }

class Notebook:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.notes = [Note(**note) for note in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.notes = []

    def save_notes(self):
        with open(self.filename, 'w') as file:
            json.dump([note.to_dict() for note in self.notes], file)

    def show_all_notes(self):
        if not self.notes:
            print("No notes available.")
        for note in self.notes:
            print(f"ID: {note.id}, Created: {note.created_date}")

    def show_note_details(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            print(f"ID: {note.id}\nText: {note.text}\nCreated Date: {note.created_date}")
        else:
            print("Note not found.")

    def create_note(self, text):
        note_id = len(self.notes) + 1
        created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(note_id, text, created_date)
        self.notes.append(new_note)
        self.save_notes()
        print(f"Note created with ID: {note_id}")

    def update_note(self, note_id, new_text):
        note = self.get_note_by_id(note_id)
        if note:
            note.text = new_text
            self.save_notes()
            print("Note updated.")
        else:
            print("Note not found.")

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            self.save_notes()
            print("Note deleted.")
        else:
            print("Note not found.")

    def get_note_by_id(self, note_id):
        return next((note for note in self.notes if note.id == note_id), None)



def main():
    notebook = Notebook()
    while True:
        print("\nMenu:")
        print("1. Show all notes")
        print("2. Show note details")
        print("3. Create a new note")
        print("4. Update an existing note")
        print("5. Delete a note")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            notebook.show_all_notes()
        elif choice == '2':
            note_id = int(input("Enter note ID: "))
            notebook.show_note_details(note_id)
        elif choice == '3':
            text = input("Enter the note text: ")
            notebook.create_note(text)
        elif choice == '4':
            note_id = int(input("Enter note ID: "))
            new_text = input("Enter the new text: ")
            notebook.update_note(note_id, new_text)
        elif choice == '5':
            note_id = int(input("Enter note ID: "))
            notebook.delete_note(note_id)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
