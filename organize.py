import os
import shutil

#Path to folder to be organized

TARGET_FOLDER = "example_folder"

#List of all files and folders in the directory

def list_files(path):
    for item in os.listdir(path):
        print(item)

#dictionary of categories to organize files
EXTENSION_MAPPING = {
    'images' : ['.png', '.jpg', '.gif', '.jpeg'],
    'documents' : ['.pdf', '.docx', '.txt'],
    'spreadsheets': ['.csv', '.xlsx'],
    'videos': ['.mp4', '.mov' ],
    'code' : ['.py', '.js', '.html', '.css'],
    'others': []

}  

def get_category(file_ext):
    #for loop to loop through each file category and its list of file extensions
    for category, extensions in EXTENSION_MAPPING.items():
        #checks if the files extensions is in the list for that category
        if file_ext.lower() in extensions:
            #if a match it returns the category 
            return category
    #no match, returns to others
    return 'others'

def organize_folder(path):
    #loop through everthing in the folder
    for filename in os.listdir(path):
        #builds the full path to each item
        full_path = os.path.join(path,filename)

        #focuses on files
        if os.path.isfile(full_path):
            #split the file name into name and extension
            _, ext = os.path.splitext(filename)
            category = get_category(ext)

            #builds the path to folder where file should go
            category_folder = os.path.join(path,category)
            #only creates folder if it does not exist already
            os.makedirs(category_folder, exist_ok=True)

            #sets destination path
            new_path = os.path.join(category_folder, filename)
            #moves the file to new folder
            shutil.move(full_path, new_path)
           # prints in terminal
            print(f"Moved: {filename} -> {category}/")


if __name__ == "__main__":
    list_files(TARGET_FOLDER)
    print(f"Listing files in {TARGET_FOLDER}")
    print("==================================================")
    print("**************************************************")
    print("==================================================")
    print(f"Organizing folder: {TARGET_FOLDER}")
    organize_folder(TARGET_FOLDER)
   