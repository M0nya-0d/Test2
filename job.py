import os
import schedule # type: ignore
import requests
user_name = "parametr6"
file = open('inc.txt', 'r', encoding='utf-8')
inc = int(file.read())
file.close()

#if(inc == 1):
#    os.system('py sborUserName.py')
    #file.write('0')


def regen():
    os.system('py test.py')

#def ded_kill():
#    os.system('python kill.py')
#os.system('py sborUserName.py')
def main():
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
            os.system('py sborUserName.py')




if __name__ == '__main__':
    main()
