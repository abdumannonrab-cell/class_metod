import shop


class Product:
    def __init__(self,title,price,year):
        self.title=title
        self.price=price
        self.year=year
        self.type=''
class Shop:
    def __init__(self,title,phone):
        self.title=title
        self.phone=phone
        self.baza=[]
    def add_water(self):
        title=input("title:")
        price=input("price:")
        year=input("year:")
        p1=Product(title,price,year)
        p1.type='water'
        self.baza.append(p1)
    def add_food(self):
        title = input("title:")
        price = input("price:")
        year = input("year:")
        p1 = Product(title, price, year)
        p1.type='food'
        self.baza.append(p1)
    def view_water(self):
        for item in self.baza:
            if item.type=="water":
                print(f'title:{item.title} price:{item.price} year:{item.year} type:{item.type}')
            else:
                pass
    def view_food(self):
        for item in self.baza:
            if item.type=="food":
                print(f'title:{item.title} price:{item.price} year:{item.year} type:{item.type}')
            else:
                pass
    def delete_all(self):
        delete=input("delete:")
        t=False
        count=0
        for item in self.baza:
            count+=1
            if item.title==delete:
                t=True
        if t:
            self.baza.pop(count-1)
            print("o'chdi")
        else:
            print("topilmadi")


    def update_all(self):
        update = input("o'zgartirish:")
        t = False
        count = 0
        for item in self.baza:
            count += 1
            if item.title == update:
                yangi=item
                t = True
            if t:
                kod=input(f'1.title\n 2.price\n 3.year\n 4.type\n 5.all')
                if kod=="1":
                    new_title= input("new_title:")
                    yangi.title=new_title
                    print("o'zgardi")
                elif kod=="2":
                    new_price=input("new_price")
                    yangi.price=new_price
                    print("o'zgardi")
                elif kod=="3":
                    new_year=input("new_year")
                    yangi.year=new_year
                    print("o'zgardi")
                elif kod=="4":
                    new_type=input("new_type")
                    yangi.type=new_type
                    print("o'zgardi")
                else:
                    new_title = input("new_title:")
                    new_price = input("new_price")
                    new_year = input("new_year")
                    new_type = input("new_type")
                    yangi.title = new_title
                    yangi.price = new_price
                    yangi.year = new_year
                    yangi.type = new_type
                    print("o'zgardi")
            else:
                print('topilmadi')
    def view_all(self):
        for item in self.baza:
            print(f'title:{item.title} price:{item.price} year:{item.year} type:{item.type}')
shop1 = Shop("shop1", 78625082)
def menejer(shop:shop):
    while True:
        kod=input("1.add_water\n 2.add_food\n 3.view_all\n 4.view_water\n 5.view_food\n 6.delete_all\n 7.uptade_all\n 8.break")
        if kod=="1":
            shop.add_water()
        elif kod=="2":
            shop.add_food()
        elif kod=="3":
            shop.view_all()
        elif kod=="4":
            shop.view_water()
        elif kod=="5":
            shop.view_food()
        elif kod=="6":
            shop.delete_all()
        elif kod=="7":
            shop.update_all()
        else:
            break
# shop.menejer(shop1)