
file = open("test.txt", "a")
userinput = input("Enter a line to write to the file: ")
file.write(userinput + "\n")
file.close()