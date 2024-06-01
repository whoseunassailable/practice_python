# Open the file in read mode ('r')\
list_of_numbers1 = []
list_of_numbers2 = []

with open('E:\\projects\\problem_solving\\file1.txt', 'r') as file:
    # Read the entire contents of the file into a string
    file_contents = file.read()
    list_of_numbers1 = file_contents.split('\n')
    list_of_numbers1 = [int(string) for string in list_of_numbers1]

with open('E:\\projects\\problem_solving\\file2.txt', 'r') as file:
    # Read the entire contents of the file into a string
    file_contents = file.read()
    list_of_numbers2 = file_contents.split('\n')
    list_of_numbers2 = [int(string) for string in list_of_numbers2]
    
result = [number1 for number1 in list_of_numbers1 for number2 in list_of_numbers2 if number1 == number2]


# Write your code above 👆
print(result)
