import os

def find_missing_number(path):
    files = os.listdir(path)
    numbers = []
    for file in files:
        try:
            number = int(file.split('.')[0])
            numbers.append(number)
        except ValueError:
            pass
    
    numbers.sort()
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i-1] + 1:
            return numbers[i-1] + 1
    
    return None

missing_number = find_missing_number("D:\\Dropbox\\visualProjects\\blender\\cubismMograph\\renderOutput")
if missing_number:
    print(f"The missing number is: {missing_number}")
else:
    print("No missing number found.")