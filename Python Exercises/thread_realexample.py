import threading
import time
import random

class BankAccount(threading.Thread):


    accountBalance = 100

    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)

        self.name = name
        self.moneyRequest = moneyRequest


    def run(self):

        threadLock.acquire()

        BankAccount.getMoney(self)

        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print('{} tries to withdrawal ${} at {}'.format(customer.name, customer.moneyRequest, time.strftime('%H:%M:%S', time.gmtime())))

        if BankAccount.accountBalance - customer.moneyRequest > 0:
            BankAccount.accountBalance -= customer.moneyRequest
            print('New account balance : ${}'.format(BankAccount.accountBalance))
        else:
            print('Not enough money in account')
            print('Current balance : ${}'.format(BankAccount.accountBalance))

        time.sleep(3)


threadLock = threading.Lock()

doug = BankAccount('Doug', 1)
Paul = BankAccount('Paul', 100)
Sally = BankAccount('Sally', 50)

doug.start()
Paul.start()
Sally.start()

doug.join()
Paul.join()
Sally.join()

print('Execution Ends')

