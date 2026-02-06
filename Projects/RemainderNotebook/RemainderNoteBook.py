#PERSONAL NOTEBOOK / REMAINDER APP (Console Project)

import os
import datetime

NOTES_FILE = "notes.txt"

#---------------Data Handling Functions------------

def load_notes():
    """Load notes from file into a list of dicts: [{'date':..., 'message':...}, ...]"""
    notes = []
    if not os.path.exists(NOTES_FILE):
        return notes

    with open(NOTES_FILE,"r", encoding="utf-8") as f:
        lines =[line.rstrip("\n") for line in f]

    i = 0
    while i < len(lines):
        if lines[i].strip() == "-----NOTE-----":
            # Expect: Date line, Message line, separator
            dateLine = lines[i +1] if i + 1 < len(lines) else""
            msgLine = lines[i + 2] if i + 2 < len(lines) else""
            #Move index to after block
            i = i + 4 #skip separator line too

            if dateLine.startswith("Data:") and msgLine.startswith("Message:"):
                dateText = dateLine.replace("Date:","",1).strip()
                messageText = msgLine.replace("Message:","",1).strip()
                notes.append({"date":dateText, "message": messageText})
        else:
            i += 1

    return notes


def save_notes(notes):
    """Overwrite file with all notes in the block format."""
    with open(NOTES_FILE, "w",encoding="utf-8") as f:
        for note in notes:
            f.write("-----NOTE-----\n")
            f.write(f"Date: {note['date']}\n")
            f.write(f"Message: {note['message']}\n")
            f.write("----------------\n")

#Core Features

def add_note(notes):
    print("\n📝 ADD NEW NOTE")
    text = input("Enter your note/remainder: ").strip()
    if not text:
        print("Note cannot be empty.")
        return

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    notes.append({"date":now, "message": text})
    save_notes(notes)
    print("✅ Note added successfully with timestamp:", now)

def view_notes(notes):
    print("\n📑 ALL NOTES")
    if not notes:
        print("No notes found yet. Start by adding one!")
        return

    for idx, note in enumerate(notes, start=1):
        print("-" * 40)
        print(f"#{idx}   {note['date']}")
        print(f"       {note['message']}")
    print("-" * 40)

def search_notes(notes):
    print("\n🔍 SEARCH NOTES")
    keyword = input("Enter keyword to search: ").strip().lower()
    if not keyword:
        print("Keyword cannot be empty.")
        return []

    results = []
    for i, note in enumerate(notes):
        if keyword in note["message"].lower() or keyword in note["date"].lower():
            results.append((i, note))

    if not results:
        print("No notes matched your search.")
    else:
        print(f"\nFound {len(results)} matching note(s):")
        for idx, (original_index, note) in enumerate(results, start=1):
            print("-" * 40)
            print(f"Result {idx} (Note #{original_index + 1})")
            print(f"   {note['date']}")
            print(f"   {note['message']}")
        print("-" * 40)

    return results

def choose_from_search(results):
    """Let user pick one note from results. Returns original index or None."""
    if not results:
        return None
    
    try:
        choice = int(input("Enter result number to select ( 0 to cancel): "))
    except ValueError:
        print("Invalid input.")
        return None
    
    if choice == 0:
        return None
    
    if 1 <= choice <= len(results):
        originalIndex, _ = results[choice - 1]
        return originalIndex
    else:
        print("Invalid choice.")
        return None
    
def update_note(notes):
    print("\n ✏UPDATE NOTE (search=-based)")
    results = search_notes(notes)
    index = choose_from_search(results)
    if index is None:
        return
    
    old_note = notes[index]
    print("\nCurrent note:")
    print(f" 📅   {old_note['date']})")
    print(f" 📑 {old_note['message']}")
    
    new_text = input("\nEnter updated note text (leave blank to cancel): ").strip()
    if not new_text:
        print("Update cancelled.")
        return
    
    #Option: keep original date or update note text (leave blank to cancel):").strip()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    notes[index] = {"date": now, "message": new_text}
    save_notes(notes)
    print("✅ Note updated successfully.")

def delete_note(notes):
    print("\n🗑 DELETE NOTE (search-based)")
    results = search_notes(notes)
    index = choose_from_search(results)
    if index is None:
        return
    note = notes[index]
    print("\nYou are about to delete this note:")
    print(f" 📅  {note['date']}")
    print(f" 📑 {note['message']}")

    confirm = input("Are you sure? (y/n): ").strip().lower()
    if confirm == "y":
        notes.pop(index)
        save_notes(notes)
        print("✅ Note deleted.")
    else:
        print("Decletion cancelled.")

#Menu / Main Loop

def print_menu():
    print("\n===============PERSONAL NOTEBOOK===============")
    print("1. 📝 Add New Note")
    print("2. 📒View All Notes")
    print("3. 🔍Search Notes")
    print("4. ✏️Update Note (via search)")
    print("5. 🗑Delete Note (via delete)")
    print("6. 🚪Exit")
    print("============================================")


def main():
    notes = load_notes()
    print("📚 Welcome to Personal NoteBook / Remainder App")
    print(f"Using file: {NOTES_FILE}")

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_note(notes)
        elif choice =="2":
            view_notes(notes)
        elif choice =="3":
            search_notes(notes)
        elif choice =="4":
            update_note(notes)
        elif choice =="5":
            delete_note(notes)
        elif choice =="6":
            print("🧤Exiting Personal NoteBook. Goodbye!")
            break
        else:
            print("Invalid choice.Please select between 1 and 6.")

if __name__ == "__main__":
    main()