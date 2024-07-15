import json
from start import user_name

hp  = None
rad = None
sost_psy = None
arm_rad = None
arm_psy = None
arm_elect = None
arm_ximiy = None
flag = False




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

class User2:
    def __init__(self):
        self.hp  = None
        self.rad = None
        self.sost_psy = None
        self.arm_rad = None
        self.arm_psy = None
        self.arm_elect = None
        self.arm_ximiy = None

data = {
    "parametr" : []
}
def zapis():
    data['parametr'].append(User().__dict__)
    write_info(data,'user.json')
    write_info(data,'info1.json')

def zatir():
    data['parametr'].append(User2().__dict__)
    write_info(data,'name_user.json')

def sbor():
    d_data = read_info('name_user.json')
    if user_name in d_data:

        g = User()
        g.hp  = d_data[user_name][0]['hp']
        g.rad = d_data[user_name][0]['rad']
        g.sost_psy = d_data[user_name][0]['sost_psy']
        g.arm_rad = d_data[user_name][0]['arm_rad']
        g.arm_psy = d_data[user_name][0]['arm_psy']
        g.arm_elect = d_data[user_name][0]['arm_elect']
        g.arm_ximiy = d_data[user_name][0]['arm_ximiy']
        global hp, rad, sost_psy, arm_rad, arm_psy, arm_elect, arm_ximiy
        hp =  (g.hp)
        rad = (g.rad)
        sost_psy = (g.sost_psy)
        arm_rad = (g.arm_rad)
        arm_psy = (g.arm_psy)
        arm_elect = (g.arm_elect)
        arm_ximiy = (g.arm_ximiy)
        flag = True
    else:
        print(f"нет ника")
        flag = False

sbor()
zapis()
zatir()