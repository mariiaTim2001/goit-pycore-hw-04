from handlers.is_valid_phone import is_valid_phone

def add_contact(args, contacts):
    if len(args) != 2:
        return "❌ Invalid input! Use: add [name] [phone]\n""📌 Example: add John +380931234567"
    name, phone = args
    if not is_valid_phone(phone):
        return "❌ Invalid phone number. Use only digits, 10–15 characters. May start with '+'❌"
    contacts[name] = phone
    return f"✅ Contact '{name}' added with phone 📞 {phone}"
