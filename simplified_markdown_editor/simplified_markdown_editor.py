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
    elif command == "link":
        label = input("Label: ")
        url = input("URL: ")
        markdown += f"[{label}]({url})"
        print(markdown)
    elif command == "new-line":
        markdown += "\n"
        print(markdown)
    elif command == "header":
        while True:
            level = int(input("Level: "))
            if 1 <= level <= 6:
                break
            print("The level should be within the range of 1 to 6")
        text = input("Text: ")
        markdown += "#" * level + " " + text + "\n"
        print(markdown)
    else:
        print("Unknown formatting type or command")
