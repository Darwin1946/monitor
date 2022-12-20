# This is a sample Python script.
import psutil
import os
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(processid):
    # Use a breakpoint in the code line below to debug your script.
    process = psutil.Process(int(processid))
    print(process.memory_info().rss)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    id = input("processid:\n")
    print_hi(id)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
