def my_logic(given_string):
  for char in given_string:
    if (char.isdigit()):
      num1=char
      break

  for char in given_string[::-1]:
    if (char.isdigit()):
      num2=char
      break
  return num1+num2

file_path = '1-input.txt'
total=0

with open(file_path, 'r') as file:
    for line in file:
        total+=int(my_logic(line.strip()))

print(total)
