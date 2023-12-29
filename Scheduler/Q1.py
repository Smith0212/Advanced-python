import schedule
import os
import shutil

def job(source, destination): 

    if not os.path.exists(source):
        print("Source path does not exist")
        return

    if not os.path.exists(destination):
        os.mkdir(destination)
        print(f"Destination path created: {destination}")  

    print("I'm working...")
    shutil.copy(source, destination)
    print("Backup completed")


source = input("Enter the source path: ")
destination = input("Enter the destination path: ")
schedule.every().day.at("11:28").do(job, source, destination)

while True:
    schedule.run_pending()


