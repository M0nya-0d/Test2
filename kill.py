import json
def write_info(data, file_name):
    data = json.dumps(data)
    data = json.loads(data)
    with open(file_name, 'w', encoding = "utf-8") as file:
        json.dump(data, file, indent = 4)

def zapis():
    data['parametr'].append(User().__dict__)
    write_info(data,'info1.json')

class User:
    def __init__(self):
        self.hp  = -1
        self.rad = 0
        self.sost_psy = 0
        self.arm_rad = 0
        self.arm_psy = 0
        self.arm_elect = 0
        self.arm_ximiy = 0
data = {
    "parametr" : []
}
zapis()