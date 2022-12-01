import glob
import os
import shutil
import pyautogui
import pyperclip as pc

import protocol
import server

PHOTO_PATH = server.PHOTO_PATH


def func_dir(params):
    return glob.glob(params[0] + '/*.*')


def func_delete(params):
    os.remove(params[0])
    return True


def func_execute(params):
    os.system(f"open {params[0]}")


def func_copy(params):
    shutil.copy(params[0], params[1])
    return True


def func_takephoto(params):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(PHOTO_PATH)
    print(PHOTO_PATH)
    return True


def func_sendphoto(params):
    file = open(PHOTO_PATH, 'rb')
    byte = file.read()
    lengthOfByte = str(len(byte))
    lengthOfLength = str(len(lengthOfByte))
    file.close()

    return lengthOfLength.zfill(protocol.LENGTH_FIELD_SIZE) + lengthOfByte, byte


def func_copyclipboard(params):
    pc.copy(params[0])


def func_pasteclipboard(params):
    text = pc.paste()

    return text


def func_exit(params):
    return True


COMMANDS = {"DIR": func_dir,
            "DELETE": func_delete,
            "EXECUTE": func_execute,
            "COPY": func_copy,
            "TAKE_SCREENSHOT": func_takephoto,
            "SEND_PHOTO": func_sendphoto,
            "COPY_CLIPBOARD": func_copyclipboard,
            "PASTE_CLIPBOARD": func_pasteclipboard,
            "EXIT": func_exit
            }
