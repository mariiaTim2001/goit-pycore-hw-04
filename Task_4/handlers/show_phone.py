def show_phone(args, contacts):
    if len(args) != 1:
        return "❌ Invalid input. Use: phone [name] ❌"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found 😭"
    