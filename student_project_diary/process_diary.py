import os

text = ""
list_of_files = []
#Grabs files that end in .txt in a directory to process with the read_diary function
def get_list_of_files(directory_path):
    for path in os.listdir(directory_path):
        if os.path.isfile(path) and path.endswith(".txt"):
            list_of_files.append(path)
    return list_of_files



#Reads the files and returns the text in the files as a dictionary with the date as key and the text as value
def read_diary(list_of_files):
    text = {}
    for file in list_of_files:
        with open(file, "r") as f:
            read_txt = f.read()
            read_txt = read_txt.lower()
            filename = f.name.replace(".txt", "")
            text[filename] = read_txt
    return text

