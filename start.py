import os
import schedule 
#import requests
user_name = "parametr6"
file = open('inc.txt', 'r', encoding='utf-8')
inc = int(file.read())
file.close()

def regen():
    os.system('python3 test.py')

#def ded_kill():
#    os.system('python3 kill.py')
#os.system('python3 sborUserName.py')
def mainn():
    schedule.every(2).seconds.do(regen)
    #schedule.every(20).seconds.do(ded_kill)
    while True:
        global inc
        schedule.run_pending()
        #schedule.run_pending()
        if(inc == 1):
            inc = 0
            file = open('inc.txt', 'w', encoding='utf-8')
            file.write('0')
            file.close()
            os.system('python3 sborUserName.py')

if __name__ == '__main__':
    mainn()
