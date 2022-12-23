# This is a sample Python script.
import signal
import sys
import time
import traceback

import numpy as np
import psutil
# import matplotlib.pyplot as plt
import os

from matplotlib import pyplot as plt


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def quit(signum, frame):
    print('stop recording')
    sys.exit()

def get_id():
    id = input("processid:\n")
    try:
        process = psutil.Process(int(id))
        return process
    except psutil.NoSuchProcess:
        print("process PID not found (pid="+str(id)+")")
        get_id()
def painter_c():
    if os.path.exists("test.txt"):
        x = []
        y = []
        for line in open('test.txt', 'r'):
            lines = [i for i in line.split("\t")]
            x.append(int(lines[0]))
            y.append(float(lines[1]))

        plt.title("CPU Usage")
        plt.xlabel('time/s')
        plt.ylabel('cpu/percent')
        # plt.yticks(y)
        plt.xticks(x)
        # plt.xlim(min(t), max(t))
        plt.ylim(0, 101)
        plt.yticks(np.arange(0, 100, step=20))
        plt.plot(x, y, marker='o', c='g')

        plt.show()
    else:
        print("can not found monitor log file")

def painter_m():

    mem = psutil.virtual_memory()
    total_mem = (mem.total/1024)/1024
    if os.path.exists("test.txt"):
        x = []
        y = []
        for line in open('test.txt', 'r'):
            lines = [i for i in line.split("\t")]
            x.append(int(lines[0]))
            y.append(float(lines[2]))

        plt.title("Memory Usage")
        plt.xlabel('time/s')
        plt.ylabel('mem/MB')
        # plt.yticks(y)
        plt.xticks(x)
        # plt.xlim(min(t), max(t))
        plt.ylim(0, total_mem+1)
        plt.yticks(np.arange(0, total_mem, step=(total_mem/10)))
        plt.plot(x, y, marker='o', c='g')

        plt.show()
    else:
        print("can not found monitor log file")

def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    process = get_id()

    sleepTime = 3;
    # for()
    signal.signal(signal.SIGINT, quit)
    signal.signal(signal.SIGTERM, quit)

    os.remove("test.txt")
    ti = 0;
    with open('test.txt', 'a') as file:
        while True:
            try:
                cpu_res = psutil.cpu_percent()
                mem_res = (process.memory_info().rss/1024)/1024

                info = str(ti)+"\t"+str(cpu_res)+"\t"+str(int(mem_res))
                print(info)

                file.write(info+"\n")
                time.sleep(sleepTime)
                ti+=3
            except:
                traceback.format_exc()
                break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
    painter_m()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
