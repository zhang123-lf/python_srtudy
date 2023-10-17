import os

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return len(file.readlines())
    except Exception as e:
        print(f"Error counting lines in {file_path}: {e}")
        return 0

def count_lines_in_directory(directory_path, file_extensions):
    total_lines = 0

    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(tuple(file_extensions)):
                file_path = os.path.join(root, file_name)
                lines = count_lines_in_file(file_path)
                total_lines += lines

    return total_lines

if __name__ == "__main__":
    directory_path = "."  # 设置要统计的目录
    file_extensions = (".s", ".h", ".c", ".cpp", ".hpp")  # 设置要统计的文件扩展名，可以根据需要修改

    total_lines = count_lines_in_directory(directory_path, file_extensions)

    print(f"Total lines of code: {total_lines}")
