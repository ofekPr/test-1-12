def read_files(file_path):
    try:
        file = open(file_path, 'r')
        print(file.read())
    except:
        print("file can't be read or not exists")
    file.close()


read_files(
    '/Users/ofekprimor/Downloads/sample3.txt')
