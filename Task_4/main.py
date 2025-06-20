from parse_input import parse_input
from handlers.add_contact import add_contact
from handlers.change_contact import change_contact
from handlers.show_phone import show_phone
from handlers.show_all import show_all
from handlers.help import help


def main():
    contacts = {}
    print("\n🤖 Welcome to the Assistant Bot!")
    print("💡 Type 'hello' to begin or 'help' to see commands\n")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("👋 Good bye!")
            break
        elif command == "hello":
            print("🙋‍♂️ How can I help you?")
        elif command == "help":
            help()
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("❓ Invalid command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
