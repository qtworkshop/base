
import os
path = r"D:\save\serg\progects\base\testProject"
project_name = "testProject"
folders = [
    ["scr", [
        ["scr", []],
        ["scr2", [
            ["scr3", []]
        ]]
    ]],
    ["gui", []]
    ]


def create_folder(path):
    if not os.path.isdir(path):
         os.mkdir(path)


def build(root, data: list):
    if data:
        for d in data:
            path = os.path.join(root, d[0])
            create_folder(path)
            build(path, d[1])


full_path = os.path.join(path, project_name)
#
# create_folder(full_path)
#
build(full_path, folders)

# print("1".zfill(6))
# print(333)