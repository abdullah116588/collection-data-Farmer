import csv

file_name = "data.csv"
code_file_name = "dragon_fruit_farmer_management.py"
def save_script():
    with open(__file__, "r") as current_file:
        code_content = current_file.read()
    with open(code_file_name, "w") as code_file:
        code_file.write(code_content)
def initialize_file():
    try:
        with open(file_name, "r") as file:
            pass
    except FileNotFoundError:
        with open(file_name, "w", newline="") as file:
            csv.writer(file).writerow(["Name", "Phone", "Land", "Production", "Price", "Expenditure", "Destruction", "Variety"])

def add_farmer():
    data = [input(f"Enter {field}: ") for field in ["Name", "Phone", "Land", "Production", "Price", "Expenditure", "Destruction", "Variety"]]
    with open(file_name, "a", newline="") as file:
        csv.writer(file).writerow(data)
    print("Farmer added.")
def edit_farmer():
    phone = input("Enter Phone to Edit: ")
    rows, found = [], False
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        rows.append(next(reader))  # Read header
        for row in reader:
            if row[1] == phone:
                row = [input(f"Enter New {rows[0][i]}: ") or row[i] for i in range(len(row))]
                found = True
            rows.append(row)
    if found:
        with open(file_name, "w", newline="") as file:
            csv.writer(file).writerows(rows)
        print("Farmer updated.")
    else:
        print("Farmer not found.")
def remove_farmer():
    phone = input("Enter Phone to Remove: ")
    rows, found = [], False
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        rows.append(next(reader))  # Read header
        for row in reader:
            if row[1] != phone:
                rows.append(row)
            else:
                found = True
    if found:
        with open(file_name, "w", newline="") as file:
            csv.writer(file).writerows(rows)
        print("Farmer removed.")
    else:
        print("Farmer not found.")
def show_all_farmers():
    with open(file_name, "r") as file:
        for row in csv.reader(file):
            print(", ".join(row))
def search_farmer():
    phone = input("Enter Phone to Search: ")
    with open(file_name, "r") as file:
        for row in csv.reader(file):
            if row[1] == phone:
                print(", ".join(row))
                return
    print("Farmer not found.")
def main():
    initialize_file()
    save_script()  # Save the script initially
    while True:
        print("\n1. Add Farmer\n2. Edit Farmer\n3. Remove Farmer\n4. Show All\n5. Search Farmer\n6. Exit")
        choice = input("Choice: ")
        if choice == "1":
            add_farmer()
        elif choice == "2":
            edit_farmer()
        elif choice == "3":
            remove_farmer()
        elif choice == "4":
            show_all_farmers()
        elif choice == "5":
            search_farmer()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()