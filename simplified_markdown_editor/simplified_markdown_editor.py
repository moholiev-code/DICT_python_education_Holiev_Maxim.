formatters = [
    "plain",
    "bold",
    "italic",
    "header",
    "link",
    "inline-code",
    "ordered-list",
    "unordered-list",
    "new-line"
]

while True:
    command = input("Choose a formatter: ")

    if command == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")

    elif command == "!done":
        break

    else:
        print("Unknown formatting type or command")