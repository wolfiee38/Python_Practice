import os

def readdir(dpath, output):
    try:
        # Get the list of items in the directory
        entries = os.listdir(dpath)
        
        # Open file in write mode
        with open(output, 'w') as file:
            for e in entries:
                file.write(e + '\n')

    except Exception as e:
        print("Your error is", e)

# Set the directory path and output file
dirpath = '.'
outputfile = 'hhhho.txt'

# Call the function
readdir(dirpath, outputfile)
