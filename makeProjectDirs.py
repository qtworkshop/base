
import os
path = r"D:\0SYNC\python_projects\workshop\base\testProject"
project_name = "testProject"
folders = ["scr",
           "gui"]

def create_folder(path):
    if not os.path.isdir(path):
         os.mkdir(path)


full_path = os.path.join(path, project_name)

create_folder(full_path)


for folder in folders:
    path = os.path.join(full_path, folder)
    create_folder(path)