import os
import schedule
import requests

def regen():
    os.system('python test.py')

def ded_kill():
    os.system('python kill.py')

def main():
    schedule.every(2).seconds.do(regen)
    #schedule.every(20).seconds.do(ded_kill)
    while True:
        schedule.run_pending()
        #schedule.run_pending()



if __name__ == '__main__':
    main()
