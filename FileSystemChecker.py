# user input required to choose fileSystems and prefix
fileSystem1 = input("What is the first file system? ")
fileSystem2 = input("What is the second file system? ")
prefixTest = input("What prefix would you like to test? ")

# opens the two fileSystems
f = open(fileSystem1,encoding="utf-8", errors="ignore")
v = open(fileSystem2,encoding="utf-8", errors="ignore")

# x = iterator for fileSystem1
# z = iterator for fileSystem2

# begin for loop with first line from fileSystem1
for x in f:
    # checks if name of file is = to prefixTest at index 34 (where all file names begin)
    if x.startswith(prefixTest, 34):
        
        # begin nested for loop iterating through filesystem2 while comparing to each line to fileSystem1 line
        for z in v:
            if z.startswith(prefixTest, 34):
                
                # checks if strings are equal including checksum and prints the file is on both fileSystems
                if x == z:
                    print("File: ", x[34:], "Is on both systems")
                    # seek is used to reset cursor on fileSystem file
                    v.seek(0)
                    break
                
                # checks if file name is equal not indluding checksum and prints
                elif x[34:] == z[34:]:
                    print("File: ", x[34:], "Exists on both systems, but is different")
                    v.seek(0)
                    break 

        # if file is not found on fileSystem2 else statement activates and alerts user
        else:
            print("File: ", x[34:], "Exists only on System 1")
            v.seek(0)

# resets the position of each file being read
f.seek(0)
v.seek(0)

# performs above tasks reversed to compare for fileSystem2 omits prints on similar strings because that has already been done
for z in v:
    if z.startswith(prefixTest, 34):
        for x in f:
            if x.startswith(prefixTest,34):
                if z == x:
                    f.seek(0)
                    break

                elif z[34:] == x[34:]:
                    f.seek(0)
                    break

        # alerts user file is only found on fileSystem2 and resets cursor
        else:
            print("File: ", z[34:], "Exists only on System 2")
            f.seek(0)

# closes files upon completion
f.close()
v.close()
