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

markdown = ""

while True:
    command = input("Choose a formatter: ")

    if command == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")

    elif command == "!done":
        break

    elif command == "plain":
        text = input("Text: ")
        markdown += text
        print(markdown)
    elif command == "bold":
        text = input("Text: ")
        markdown += f"**{text}**"
        print(markdown)
    elif command == "italic":
        text = input("Text: ")
        markdown += f"*{text}*"
        print(markdown)
    elif command == "inline-code":
        text = input("Text: ")
        markdown += f"`{text}`"
        print(markdown)
    else:
        print("Unknown formatting type or command")
