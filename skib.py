import json

filename = "notes.json"

def save_notes(notes: list[str]):
    with open(filename,"w",encoding="utf-8") as file:
        json.dump(notes, file, indent=2, ensure_ascii= False)

def load_notes():
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    notes = load_notes()

    while True:
        print("Vad vill du?")
        print("1. visa")
        print("2. lägg till")
        print("3. nukeem")
        print("4. gita")

        choice = input("välj en (1-4): ").strip()

        if choice == "1":
            print("\nDina antekningar")
            if not notes:
                print("du har inget")
            else:
                for i, note in enumerate(notes, start=1):
                    print(f"{i}.{note}")

        elif choice == "2":
            text = input("skriv nåt: ")
            notes.append(text)
            save_notes(notes)
            print("sparad")

        elif choice == "3":
            notes.clear()
            save_notes(notes)
            print("allt borta")

        elif choice == "4":
            print("skib")
            break

        else:
            print("ogiltigt val")

if __name__ == "__main__":
    main()