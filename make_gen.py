import glob

path = "./**/*"
file_list = glob.glob(path)
file_list_cpp = [file for file in file_list if file.endswith(".cpp")]

for file in file_list_cpp:
    print(file)

header = (f"cmake_minimum_required(VERSION 3.10.2)\n"
          f"project(hello_cpp_17)\n")

with open("CMakeLists.txt", "w") as f:
    f.write(header)
    for file in file_list_cpp:
        chappter = file.split("/")[1]
        cpp_name = file.split("/")[2]
        project_name = cpp_name.split(".")[0]
        f.write(f"add_executable({chappter}_{project_name} {file})\n")
