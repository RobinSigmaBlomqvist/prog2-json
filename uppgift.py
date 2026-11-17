import json

FILE_NAME = "user_config.json"


def load_user_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return None


def save_user_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def main():
    user_data = load_user_data()

    if user_data is None:
        name = input("Vad heter du? ")
        user_data = {"name": name, "visits": 1}
        save_user_data(user_data)
        print(f"Välkommen {user_data['name']}!")
    else:
        user_data["visits"] = user_data.get("visits", 0) + 1
        save_user_data(user_data)
        print(
            f"Välkommen tillbaka {user_data['name']}! "
            f"Du har startat programmet {user_data['visits']} gånger"
        )


if __name__ == "__main__":
    main()