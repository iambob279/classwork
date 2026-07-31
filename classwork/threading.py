import threading
import time

def thread_function(name):
    print("Thread: " + str(name) +" starting")
    for i in range(10):
        time.sleep(1)
        print("Thread: " +  str(name) +  " count " + str(i))
    print("Thread: " + str(name) + " finishing")

print("Main    : before creating thread")
thread1 = threading.Thread(target=thread_function, args=(1,))
thread2 = threading.Thread(target=thread_function, args=(2,))
print ("Main    : before running thread")
thread1.start()
thread2.start()

print("Main    : all done")