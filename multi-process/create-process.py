# create process
"""
import os

pid = os.fork()

if pid == 0:
    print "child process id : %s, parent process id : %s"%(os.getpid(), os.getppid())
else:
    print "parent process id : %s, child process id : %s"%(os.getpid(), pid)
"""

"""
import multiprocessing
import os

# child process function
def child_processs(process_name):
    print "child process name : %s, child process id : %s"%(process_name, os.getpid() )


if __name__ == '__main__':
    print "parent process id : %s"%(os.getpid())
    childP = multiprocessing.Process(target=child_processs, args=("test_process",))
    print "start child process"
    childP.start()
    print "wait child process exit"
    childP.join()
    print "parent process exit"
"""

import multiprocessing
import os
import time
import random

def random_sleep_task(name):
    print "run task %s, task process id : %s"%(name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print "task %s take %s seconds time"%(name, start-end)

if __name__ == '__main__':
    print "parent process id %s"%(os.getpid())
    processPool = multiprocessing.Pool()
    for i in range(5):
        processPool.apply_async(random_sleep_task, args=(i,))
    print "wait all child process exit"
    processPool.close()
    processPool.join()
    print "prarent process id %s exit"%(os.getpid())



