import json
#import time
#start_time = time.monotonic()
#import schedule
#import requests
hp  = None
rad = None
sost_psy = None
arm_rad = None
arm_psy = None
arm_elect = None
arm_ximiy = None

def write_info(data, file_name):
    data = json.dumps(data)
    data = json.loads(data)

    with open(file_name, 'w', encoding = "utf-8") as file:
        json.dump(data, file, indent = 4)

#
def read_info(file_name):
    with open(file_name, 'r', encoding = "utf-8") as file:
        return json.load(file)

class User:
    def __init__(self):
        self.hp  = hp
        self.rad = rad
        self.sost_psy = sost_psy
        self.arm_rad = arm_rad
        self.arm_psy = arm_psy
        self.arm_elect = arm_elect
        self.arm_ximiy = arm_ximiy

data = {
    "parametr" : []
}

def zapis():
    data['parametr'].append(User().__dict__)
    write_info(data,'info1.json')

def sbor():
    d_data = read_info('info1.json')
    g = User()
    g.hp  = d_data['parametr'][0]['hp']
    g.rad = d_data['parametr'][0]['rad']
    g.sost_psy = d_data['parametr'][0]['sost_psy']
    g.arm_rad = d_data['parametr'][0]['arm_rad']
    g.arm_psy = d_data['parametr'][0]['arm_psy']
    g.arm_elect = d_data['parametr'][0]['arm_elect']
    g.arm_ximiy = d_data['parametr'][0]['arm_ximiy']
    global hp, rad, sost_psy, arm_rad, arm_psy, arm_elect, arm_ximiy
    hp =  (g.hp)
    rad = (g.rad)
    sost_psy = (g.sost_psy)
    arm_rad = (g.arm_rad)
    arm_psy = (g.arm_psy)
    arm_elect = (g.arm_elect)
    arm_ximiy = (g.arm_ximiy)




def regen():
    sbor()
    global hp, rad, sost_psy, arm_rad, arm_psy, arm_elect, arm_ximiy
    if(hp != -1):
        if(hp < 10000 and rad == 0):
            hp +=1
        if(rad > 0 and rad < 100):
            hp  -= 1
            rad -= 1
        if (rad >= 100 and rad <= 400):
            hp  -= 2
            rad -= 1
        if(rad > 400 and rad < 700):
            hp -= 2
        if (rad >= 700):
            hp -= 4


        if(hp <= 0):
            hp = -1
        if (hp >= 10000 ):
            hp = 10000
        if(rad <= 0):
            rad = 0
    else:
        rad = 0
        arm = 0
        sost_psy  = 0
        arm_rad   = 0
        arm_psy   = 0
        arm_elect = 0
        arm_ximiy = 0
    print("HP ", + hp)
    print("RAD", + rad)
    print("Psi Sost", + sost_psy)
    print("ARM Radiac", + arm_rad)
    print("ARM Psy", + arm_psy)
    print("ARM Electro", + arm_elect)
    print("ARM Ximiy", + arm_ximiy)





regen()
zapis()
#print(f"прошло: {time.monotonic() - start_time}")






