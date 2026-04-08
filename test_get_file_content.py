from functions.get_file_content import get_file_content

print("Test: read existing file lorem.txt")
print(get_file_content("calculator", "lorem.txt"))
print("---")

print("Test: read file in subdirectory pkg/__init__.py")
print(get_file_content("calculator", "pkg/calculator.py"))
print("---")

print("Test: attempt to read file outside working directory /bin/cat")
print(get_file_content("calculator", "/bin/cat"))
print("---")

print("Test: read non-existent file pkg/does_not_exist.py")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
print("---")