# readdat.py
#
# Very simple it just reads a file into a variablew and then into a list
#  then loops over the list to print the contents.
# You can do so much more than this but this will help you play with the language
#
# open a terminal in the same dir as this file and type
# python readdat.py
# 

# Edit this to reflect the path of a dat file you want to open and read.
file_name: str = "filename.dat" 

def open_file(fname: str) -> str:
    with open(fname, "r") as f:
        s: str = f.read()
    return s


def main() -> None:
    #Open .dat file and pack the contents into a string.
    file_data: str = open_file(file_name)
    # Convert the string data into a list each line is an iem in the list
    file_data = file_data.split("\n")
    
    #print the list items one at a time
    for line in file_data:
        print(line)

if __name__ == '__main__':
    main()
