import os
import shutil

dest_directory = "destination"
os.makedirs(dest_directory)
print("New directory created : " , dest_directory)


source_directory = os.getcwd()
for filename in os.listdir(source_directory):
    if filename.endswith(".jpeg"):
        source_file = os.path.join(source_directory,filename)
        destination_file = os.path.join(dest_directory,filename)
        shutil.copy(source_file,destination_file)
        print("Copied : " ,source_file," - > " , destination_file)

current_directory = os.getcwd()
print("Current ")