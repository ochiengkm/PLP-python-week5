# Task 1: Create and write to a new file
try:
    with open("my_file.txt", 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is line 2 with a number: 42\n")
        file.write("Python file handling is fun!\n")
    print("File created and written successfully.")
except Exception as e:
    print(f"Error while writing to the file: {e}")

# Task 2: Read and display the contents of the file
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nFile content:")
        print(content)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"Error while reading the file: {e}")

# Task 3: Append more lines to the file
try:
    with open("my_file.txt", 'a') as file:
        file.write("Appending line 4.\n")
        file.write("Appending line 5 with a number: 100\n")
        file.write("Appending the final line.\n")
    print("Lines appended successfully.")
except Exception as e:
    print(f"Error while appending to the file: {e}")

# Task 4: Error handling using try, except, and finally blocks
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nUpdated File content after appending:")
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File operations completed.")
