# Format: A majority of these challenges are simple. I'm putting them all in one file
# I will section off each challenge by printing dividers and making dividers clear for
# those looking at the code

print("_______________________________ Challenge #1 _______________________________\n")
# Goal: Write a Python program to read the entire contents of a text file
# named “example.txt” and print it to the console.
# Source: https://pynative.com/python-read-file/

try:
    fp = open("example_files/example.txt", "r") # 'r' is read
    text = fp.read()
    fp.close()
    print(text)
except FileNotFoundError:
    print("File not found: Please check your file path.")

# Answer: I solved it, but you can also do with open("example.txt", 'r') as file: + rest
print("\n___________________________________ End ____________________________________\n")

print("_______________________________ My Challenge #1 ______________________________\n")
# I wanted to play around with the top, see if I could essentially create my own alias for linux "cat"
# In Python

def cat(file_path):
    try:
        path = open(file_path, "r")  # 'r' is read
        content = path.read()
        path.close()
        print(content)
    except FileNotFoundError:
        print("File not found")

# Test Case
cat("example_files/example.txt") # Should return file contents
cat("sunshine.txt") # Should return "File not found"

print("\n___________________________________ End ____________________________________\n")

print("_______________________________ Challenge #2 _______________________________\n")
# Goal: Write a Python program to read the text file named “example.txt” line by line and print each line.
try:
    with open("example_files/example2.txt", "r") as file:
        line_list = file.readlines()
        for line in line_list:
            print(line)
        file.close()
except FileNotFoundError:
    print("File not found")

# Alternate Solution - for notes
# try:
#   with open("example2.txt", "r") as file:
#       line = file.readline()
#       while line != '':
#           print(line, end='')
#           line = file.readline()

print("___________________________________ End ____________________________________\n")

print("_______________________________ Challenge #3 _______________________________\n")
# Goal: Write a Python program to read only the first 5 lines of “example.txt”.
try:
    with open("example_files/example2.txt", "r") as file:
        for i in range(6):
            print(file.readline())
    file.close()
except FileNotFoundError:
    print("File not found")

# Alternate Solution - for notes
# try:
#   n = 2
#   with open("example2.txt", "r") as file:
#   head = [next(file) for x in range(n)]
#   print(head)

print("___________________________________ End ____________________________________\n")

print("_______________________________ Challenge #4 _______________________________\n")
# Goal: Create a function that takes a filename as input and returns the total number of words in that file.
# Source: https://pynative.com/python-regex-split/
import re

def word_count(file_name):
    try:
        with open(file_name, "r") as file:
            text = file.read()
            words = re.split(r"\s+", text)
            num_words = len(words)
            print(f'The number of words in your file {file_name} is: {num_words}')
    except FileNotFoundError:
        print("File not found")

# Test cases
word_count("example_files/example.txt") # Should print 7
word_count("example_files/example2.txt") # Should print 46

print("\n___________________________________ End ____________________________________\n")

print("_______________________________ Challenge #5 _______________________________\n")
# Goal: Write a function that takes a filename as input and returns the total number of
# characters in that file (including spaces and newlines).
# Source: https://pynative.com/python-regex-findall-finditer/

def character_count(file_name):
    try:
        with open(file_name, "r") as file:
            text = file.read()
            characters = re.findall(r".", text)
            print(f'The number of characters in your file {file_name} is: {len(characters)}')
    except FileNotFoundError:
        print("File not found")

# Test case
character_count("example_files/example.txt") # Should return 37
character_count("example_files/example2.txt")  # Should return 213


print("\n___________________________________ End ____________________________________\n")

print("_______________________________ Challenge #6 _______________________________\n")
# Goal: Write a program to count the occurrences of a specific word (e.g., “hello”) in a given file.
# Source: https://pynative.com/python-search-for-a-string-in-text-files/

def count_string(file_name, string):
    try:
        with open(file_name, "r") as file:
            count = 0
            for l_no, line in enumerate(file):
                if string in line:
                    count += 1
                else:
                    continue
            print(f'The number of occurrences of {string} in {file_name} is: {count}')
    except FileNotFoundError:
        print("File not found")

# Test Case
count_string("example_files/example.txt", "Hello") # Should return 1
count_string("example_files/example2.txt", "line") # Should return 8

print("\n___________________________________ End ____________________________________\n")

print("_______________________________ My Challenge #2 ____________________________\n")
# Goal: I want to do what I did last challenge but list the line number and the line

def find_string(file_name, string):
    try:
        with open(file_name, "r") as file:
            for l_no, line in enumerate(file):
                if string in line:
                    print(f'String found in {file_name}, line {l_no}')
                    print(f'Line {l_no}: {line}\n')
                else:
                    continue
    except FileNotFoundError:
        print("File not found")

# Test case
find_string("example_files/example.txt", "Hello")  # should be in line 1
find_string("example_files/example2.txt", "eighth")  # should be in line 8

print("___________________________________ End ____________________________________\n")

print("_______________________________ Challenge #7 _______________________________\n")
# Goal: Write a Python program to create a new file named “output.txt” and write the string “Hello, PYnative!” into it.
# Source: https://pynative.com/python-write-file/

def echo(text, file_name):
    try:
        with open(file_name, "w") as file:
            file.write(text)
    except FileNotFoundError:
        print("File not found")

# Test Case
# Algorithm: For the sake of this test I'm going to check if example 3 exists, if it does,
# I'm going to delete it and allow the new file to be created

import os
if os.path.exists('example_files/example3.txt'):
    print("Test Case Log: File exists")
    print("Test Case Log: Deleting file...")
    os.remove('example_files/example3.txt')
    print("Test Case Log: File deleted\n")
else:
    print("Test Case Log: File does not exist\n")

print("Test Case Log: Creating file...")
echo("Hello World", "example_files/example3.txt")
print("Test Case Log: File Created\n")
print("Test Case Log: Reading File")
cat("example_files/example3.txt")

print("\n___________________________________ End ____________________________________\n")

print("_______________________________ Challenge #8 _______________________________\n")
# Goal: Modify the previous program to append the string “This is an appended line.” to the end of “output.txt”.
# Source: https://pynative.com/python-write-file/#h-appending-new-content-to-an-existing-file

def text_append(text, file_name):
    try:
        with open(file_name, "a") as file:
            file.write(text)
    except FileNotFoundError:
        print("File not found")

# Test Case:
text_append("\nHello World again!", "example_files/example3.txt")
cat("example_files/example3.txt")

print("\n___________________________________ End ____________________________________\n")

print("_______________________________ Challenge #9 _______________________________\n")
# Goal: Write a program that takes two filenames as input (source and destination) and copies
# the content of the source file to the destination file.
# Source: https://pynative.com/python-copy-files-and-directories/

import shutil

def copy_paste(source, destination):
    try:
        shutil.copy(source, destination)
    except FileNotFoundError:
        print("File not found")

# Test case
# Algorithm: For the sake of this test I'm going to check if the copy of example 3 exists, if it does,
# I'm going to delete it and allow the new file to be created

import os
if os.path.exists('example_files/example3copy.txt'):
    print("Test Case Log: Copy File exists")
    print("Test Case Log: Deleting file...")
    os.remove('example_files/example3copy.txt')
    print("Test Case Log: File deleted\n")
else:
    print("Test Case Log: Copy File does not exist\n")

print("Test Case Log: Copying file...")
copy_paste("example_files/example3.txt", "example_files/example3copy.txt")
print("Test Case Log: File Copied\n")
print("Test Case Log: Reading Original File")
cat("example_files/example3.txt")
print("\nTest Case Log: Reading Copied File")
cat("example_files/example3copy.txt")

print("\n___________________________________ End ____________________________________\n")

print("_______________________________ Challenge #10 ______________________________\n")
# Goal: Write a program to read data from a binary file (“input.bin”) and
# write it to another binary file (“output.bin”).

def copy_binary(source, destination):
    try:
        with open(source, "rb") as source_file:
            binary_data = source_file.read()
        with open(destination, "wb") as destination_file:
            destination_file.write(binary_data)
    except FileNotFoundError:
        print("Source File not found")

# Test Case
# Algorithm: For the sake of this test I'm going to create a function that will create a binary file
# Then I'll check if the file exists and if it doesn't I'll create it so I can copy it.

import os

def write_binary(file, binary):
    try:
        with open(file, "wb") as bin_file:
            bin_file.write(binary)
    except FileNotFoundError:
        print("File not found")

def read_binary(file):
    try:
        with open(file, "rb") as bin_file:
            data = bin_file.read()
            print(data)
    except FileNotFoundError:
        print("File not found")

# Making sure the example file we need to copy, exists
if not os.path.exists('example_files/example4.bin'):
    print("Test Case Log: Example Binary File does not exist")
    print("Test Case Log: Creating Example binary file...")
    write_binary("example_files/example4.bin", b'\x48\x65\x6C\x6C\x6F')
    print("Test Case Log: Example Binary File Created\n")
else:
    print("Test Case Log: Example Binary File exists\n")

# Making sure the copy of the example doesn't exist so we can create it
if os.path.exists('example_files/example4copy.bin'):
    print("Test Case Log: Copy File exists")
    print("Test Case Log: Deleting copy file...")
    os.remove('example_files/example4copy.bin')
    print("Test Case Log: Copy File deleted\n")
else:
    print("Test Case Log: Copy File does not exist\n")

# Actual test
print("Test Case Log: Copying file...")
copy_binary("example_files/example4.bin", "example_files/example4copy.bin")
print("Test Case Log: File Copied\n")
print("Test Case Log: Reading Original Binary File")
read_binary("example_files/example4.bin")
print("\nTest Case Log: Reading Copied Binary File")
read_binary("example_files/example4copy.bin")

print("\n___________________________________ End ____________________________________\n")

print("_______________________________ Challenge #11 ______________________________\n")
# Goal: Write a function that takes a filename as input and returns True if the file exists and False otherwise.

def check_existence(file_name):
    if os.path.exists(file_name):
        return True
    else:
        return False

# Test Case
print(check_existence("example_files/example.txt"))   # Should return True
print(check_existence("fakeexample.txt"))   # Should return False

print("\n___________________________________ End ____________________________________\n")

print("_______________________________ Challenge #12 ______________________________\n")
# Goal: Write a program to get the size of a file (in bytes).
# Source: https://pynative.com/python-get-file-size/

def get_file_size(file_name):
    try:
        size = os.path.getsize(file_name)
        return size
    except FileNotFoundError:
        print("File not found")

# Test Case
# According to stat -f%z example.txt in terminal - should be 37
print("example.txt size in bytes:", get_file_size("example_files/example.txt"))
# According to stat -f%z beemovie.txt in terminal - should be 87916
print("beemovie.txt size in bytes:", get_file_size("example_files/beemovie.txt"))

print("\n___________________________________ End ____________________________________\n")

print("_______________________________ Challenge #13 ______________________________\n")
# Goal: Write a program that takes an old filename and a new filename as input and renames the file.
# Handle potential errors if the old file doesn’t exist.
# Source: https://pynative.com/python-rename-file/

def rename(old_name, new_name):
    try:
        os.rename(old_name, new_name)
    except FileNotFoundError:
        print("File not found")

# Test case
# Algorithm: I'm going to create a new file called example5.txt, then check if it exists, then rename the file
# and check again if it exists.
print("Test Case Log: Creating file example5.txt...\n")
echo("This file was originally named example5.txt", "example_files/example5.txt")
print("Test Case Log: Checking if file example5.txt exists...")
print("Output:", check_existence("example_files/example5.txt"), "\n")
print("Test Case Log: Renaming example5.txt to example6.txt...\n")
rename("example_files/example5.txt", "example_files/example6.txt")
print("Test Case Log: Checking if file example5.txt exists...")
print("Output:", check_existence("example_files/example5.txt"), "\n")
print("Test Case Log: Checking if file example6.txt exists...")
print("Output:", check_existence("example_files/example6.txt"))

print("\n___________________________________ End ____________________________________\n")

print("_______________________________ Challenge #14 ______________________________\n")
# Goal: Write a program that takes a filename as input and deletes the file.
# Handle potential errors if the file doesn’t exist.
# Source: https://pynative.com/python-delete-files-and-directories/

def rm(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("File not found")

# Test case
# Algorithm: Create test file -> check existence -> delete test file -> check existence

print("Test Case Log: Creating file example7.txt...\n")
echo("This file will have a short life span", "example_files/example7.txt")
print("Test Case Log: Checking if file example7.txt exists...")
print("Output:", check_existence("example_files/example7.txt"), "\n")
print("Test Case Log: Deleting example7.txt...\n")
rm("example_files/example7.txt")
print("Test Case Log: Checking if file example7.txt exists...")
print("Output:", check_existence("example_files/example7.txt"))

print("\n___________________________________ End ____________________________________\n")

print("_______________________________ Challenge #15 ______________________________\n")
# Goal: Write a program that reads a text file, replaces all occurrences of a specific word with another word,
# and writes the modified content to a new file.
# Source: hint

def replace(old_word, new_word, file_name):
    try:
        with open(file_name, "r") as file:
            text = file.read()
            edited_text = text.replace(old_word, new_word)
        with open(file_name, "w") as file:
            file.write(edited_text)
    except FileNotFoundError:
        print("File not found")

# Test Case
print("Test Case Log: Creating file example8.txt...\n")
echo("Hi, my name is Emma", "example_files/example8.txt")
print("Test Case Log: Reading example8.txt...")
cat("example_files/example8.txt")
print("\nTest Case Log: Replacing Emma with Redacted...")
replace("Emma", "Redacted", r"example_files/example8.txt")
print("Test Case Log: Reading example8.txt...")
cat("example_files/example8.txt")

print("\n___________________________________ End ____________________________________\n")