import os

folders = input("Enter a list of folder paths separated by spaces: ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print(f"Error: {folder} not found")
        continue
    
for file in files:
    print(file)

