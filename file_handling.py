import os


file_name = 'data.txt'

if not os.path.exists(file_name):
    print('File not found')
    exit()
else:
    print('File found')

try:
    input_file = open(file_name, 'r')
    data_lines = input_file.readlines()
    i = 0
    for line in data_lines:
        i += 1
        income = int(line.strip())
        profit = income * 123
       # print(str(i) + ' ' + str(profit))
        print(f'{i} {profit}')
    input_file.close()
except FileNotFoundError:
    print("The file was not found. Please check the file path.")

except PermissionError:
    print("Permission error. Check your file permissions.")

except UnicodeError as e:
    print(f"Unicode error occurred: {e}")

except ValueError as e:
    print(f"A value error occurred: {e}")

except NotADirectoryError:
    print("The specified path is not a directory.")

# except UnsupportedOperation as e:
#     print(f"Unsupported operation error occurred: {e}")

except OSError as e:
    print(f"OS error occurred: {e}")

except FileExistsError:
    print("The file already exists.")

except BlockingIOError:
    print("A blocking I/O error occurred.")

except UnicodeDecodeError as e:
    print(f"Unicode decode error occurred: {e}")

except UnicodeEncodeError as e:
    print(f"Unicode encode error occurred: {e}")

except IOError as e:
    print(f"An I/O error occurred: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
