#the open() function is used to open files. 
#read() returns an extra empty string once it reaches the end of a file

filepath_01 = 'text_files/pi_digits.txt' 
filepath_02 = 'text_files/pi_million_digits.txt'

with open(filepath_01) as file_object:
    lines = file_object.readlines()
    print(lines)

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

print("-----")

with open(filepath_02) as file_object:
    lines = file_object.readlines()


pi_string=''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))
