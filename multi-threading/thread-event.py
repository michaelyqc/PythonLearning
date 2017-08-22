#!/usr/bin/python

# coding=utf-8
"""
    brief :
    author : michaelyqc
    date : 2017/08/22
"""

import threading
import time

# global variable
coordinate_event = threading.Event()
sleep_time = 10

def child_thread(sleep_time, coordinate_event):
    print "child_thread is running"
    while sleep_time > 0:
        print "left %s seconds"%(sleep_time)
        time.sleep(1)
        sleep_time -= 1
    coordinate_event.set()


if __name__ == "__main__":
    print "create coordinate thread"
    coordinate_thread = threading.Thread(target=child_thread, args=(sleep_time, coordinate_event))
    coordinate_thread.start()

    print "wait child_thread to exit"
    coordinate_event.wait()
    print "child_thread having exited"
