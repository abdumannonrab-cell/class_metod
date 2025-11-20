class SMS:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.sms=""

class kontakt:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.baza=[]
    def add_kontakt(self):
        name=input("name")
        phone=input("phone")
        s=SMS(name,phone)
        s.sms=''
        self.baza.append(s)
    def sms_(self):
        smsname=input("name=")
        t=False
        for item in self.baza:
            if item.name==smsname:
                yangi=item
                t=True
        if t:
            smswrite=input("sms")
            yangi.sms=smswrite
            print("yuborildi")
        else:
            print("topilmadi")

    def delete_kontakt(self):
            name=input("name")
            t = False
            count=0
            for item in self.baza:
                count+=1
                if item.name == name:
                    t = True
            if t:
                self.baza.pop(count-1)
                print("o'chdi")
            else:
                print('topilmadi')
    def delete_sms(self):
        smsname = input("name=")
        t=False
        for item in self.baza:
            if item.name == smsname and item.sms!="":
                item.sms=""
                t=True
        if t:
            print("o'chdi")
        else:
            print("topilmadi")
    def view_sms(self):
        for item in self.baza:
            if item.sms !="":
                print(f'name:{item.name} phone:{item.phone} sms:{item.sms}')
            else:
                pass
    def view_kontakt(self):
        for item in self.baza:
            print(f'name:{item.name} phone:{item.phone} sms:{item.sms}')
sms1=kontakt("ali",998991134543)
def sms_menejer(sms:kontakt):
    while True:
        kod=input(" 1.view_kontakt\n 2.view_sms\n 3.add_kontakt\n 4.sms\n 5.delete_kontakt\n 6.delete_sms\n 7.break")
        if kod=="1":
            sms.view_kontakt()
        elif kod=="2":
            sms.view_sms()
        elif kod=="3":
            sms.add_kontakt()
        elif kod=="4":
            sms.sms_()
        elif kod=="5":
            sms.delete_kontakt()
        elif kod=="6":
            sms.delete_sms()
        else:
            break
# sms_menejer(sms1)

