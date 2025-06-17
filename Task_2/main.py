def get_cats_info(path: str) -> list:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats = []
            for line in file:
                try:
                    id, name, age = line.strip().split(',')
                    cats.append({'id': id, 'name': name, 'age': int(age)})
                except (IndexError, ValueError):
                    print(f"Not correct format of line: {line.strip()}")
                    continue

        return cats

    except FileNotFoundError:
        print(f"File {path} does not exist.")
        return []

# Test case
# cats_info = get_cats_info("Task_2/file_cats.txt")
# print(cats_info)
