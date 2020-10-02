import qrcode
import os
import random
import string
import sys


def set_dir(dir_name):
    current_dir = os.getcwd()
    final_dir = os.path.join(current_dir, dir_name)
    if not os.path.exists(final_dir):
        try:
            print("Folder not exist \n Creating folder...")
            os.makedirs(dir_name)
        except OSError:
            return "Failed creating %s directory" % dir_name
        else:
            return "Successfully creating %s directory" % dir_name
    else:
        return "Folder exist \n Skipping creation"


def get_dir(dir_name):
    return os.getcwd() + "/" + dir_name


def gen_name(length=9):
    result = ''.join(random.choice(string.ascii_lowercase)
                     for i in range(length))
    return result


def main(path, data):
    set_dir(path)
    final_dir = get_dir(path)
    img = qrcode.make(data)
    img.save(final_dir + "/" + gen_name() + ".png")
    return "Successfully generate qrcode " + final_dir


if __name__ == "__main__":
    if len(sys.argv) > 3:
        print("Argumen error, its just two argument accepted")
    else:
        print(main(sys.argv[1], sys.argv[2]))
