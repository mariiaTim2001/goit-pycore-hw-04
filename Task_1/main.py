def total_salary(path: str) -> tuple:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                try:
                    salary = float(line.strip().split(',')[1])
                    salaries.append(salary)
                except (IndexError, ValueError):
                    print(f"Not correct format of line: {line.strip()}")
                    continue

        total = sum(salaries)
        average = total / len(salaries) if salaries else 0
        return total, average

    except FileNotFoundError:
        print(f"File {path} does not exist.")
        return 0, 0


# Test case
# total, average = total_salary("Task_1/file.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
