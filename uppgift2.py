import json
import random

FILE_NAME = "highscores.json"


def load_highscores():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_highscores(highscores):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(highscores, file, indent=2, ensure_ascii=False)


def print_top_three(highscores):
    top_three = sorted(highscores, key=lambda item: item["guesses"])[:3]

    print("Top 3:")
    if not top_three:
        print("Det finns inga highscores ännu.")
        return

    for index, item in enumerate(top_three, start=1):
        print(f"{index}. {item['name']} - {item['guesses']} gissningar")


def main():
    highscores = load_highscores()
    print_top_three(highscores)

    target = random.randint(1, 50)
    guesses = 0

    while True:
        try:
            guess = int(input("Gissa ett tal mellan 1 och 50: "))
        except ValueError:
            print("Du måste skriva in ett heltal.")
            continue

        guesses += 1

        if guess < target:
            print("För lågt!")
        elif guess > target:
            print("För högt!")
        else:
            name = input("Skriv ditt namn: ")
            highscores.append({"name": name, "guesses": guesses})
            highscores = sorted(highscores, key=lambda item: item["guesses"])[:5]
            save_highscores(highscores)
            print(f"Rätt! Du gissade {guesses} gånger.")
            print("Highscore-listan har sparats.")
            break


if __name__ == "__main__":
    main()
