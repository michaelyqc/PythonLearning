# 
import threading
import time

#
def test_threading():
    print "thread %s is running"%(threading.current_thread().name)
    sleepTime = 5
    while sleepTime > 0:
        print "thread %s has %s to sleep"%(threading.current_thread().name, sleepTime)
        time.sleep(1)
        sleepTime = sleepTime-1
    print "thread %s is ended"%(threading.current_thread().name)

if __name__ == "__main__":
    print "main thread start"
    print "create test_threading"
    testThread = threading.Thread(target=test_threading, name="test_threading")
    testThread.start()
    testThread.join()
    print "test_threading exit"
    print "main thread exit"

