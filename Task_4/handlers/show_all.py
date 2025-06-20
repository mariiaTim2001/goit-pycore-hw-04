def show_all(contacts):
    if not contacts:
        return "No contacts found 🤷‍♀️"
    result = ["📒 All contacts:"]
    for name, phone in contacts.items():
        result.append(f"   👤 {name}: 📞 {phone}")
    return "\n".join(result)

