import threading
import time
import random


def executeThread(i):
    print('Thread {} sleeps at {} '.format(i, time.strftime('%H:%M:%S', time.gmtime())))
    randSleepTime = random.randint(1, 5)

    time.sleep(randSleepTime)

    print('Thread {} stops sleeping at {}'.format(i, time.strftime('%H:%M:%S', time.gmtime())))



for i in range(10):

    thread = threading.Thread(target=executeThread, args=(i,))
    thread.start()

    print('Active Threads :', threading.active_count())

    print('Thread Objects :', threading.enumerate())


class CustThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name

    def run(self):
        getTime(self.name)
        print('Thread', self.name, 'Execution Ends')


def getTime(name):
    print('Thread {} sleeps at {}'.format(name, time.strftime('%H:%M:%S', time.gmtime())))

    randSleepTime = random.randint(1, 5)

    time.sleep(randSleepTime)

thread1 = CustThread('1')
thread2 = CustThread('2')

thread1.start()
thread2.start()

print('Thread 1 alive :', thread1.is_alive())
print('Thread 2 alive :', thread2.is_alive())


print('Thread 1 Name :', thread1.getName())
print('Thread 2 Name :', thread2.getName())

thread1.join()
thread2.join()

print('Execution Ends')