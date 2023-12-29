import os
import shutil

def get_file_metadata(file_name):
    file_stat = os.stat(file_name)
    print("File Size in Bytes is :", file_stat.st_size)
    print("file name is :", file_stat.st_name)
    print("file type", "Directory" if os.path.isdir(file_name) else "File")
    print("Creation Time :", file_stat.st_ctime)
    print("Last Access Time :", file_stat.st_atime)
    print("Last Modified Time :", file_stat.st_mtime)
    print("Disk usage in bytes for E drive:",shutil.disk_usage("E:").used)

print(get_file_metadata("example.txt"))