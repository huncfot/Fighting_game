import pickle

class Produkt:
    def __init__(self, name, price, amount, worth):
        self.__name = name
        self.__price = price
        self.__amount = amount
        self.__worth = worth

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getAmount(self):
        return self.__amount

    def getWorth(self):
        return self.__worth

    def setName(self, name):
        self.__name = name

    def setPrice(self, price):
        self.__price = price

    def setAmount(self, amount):
        self.__amount = amount

    def setWorth(self, worth):
        self.__worth = worth


class Basket:

    def addProduct(self, name, price, amount, worth):
        found = False

        for v in self.products:
            if (v.getName() == name):
                v.setAmount(v.getAmount() + amount)
                v.setWorth(v.getPrice() * v.getAmount())
                found = True
                break

        if (found == False):
            product = Produkt(name, price, amount, worth)
            self.products.append(product)

    def showBasket(self):
        for i in self.products:
            print(f"Name: {i.getName()}"
                  f"\nPrice: {format(i.getPrice(), '.2f')} $"
                  f"\nAmount: {i.getAmount()} "
                  f"\nWorth: {format(i.getWorth(), '.2f')} $")
            print("----------------")

        print(f"\nTotal worth: {format(self.allCost(), '.2f')} $")

    def deleteProduct(self, name, amount):
        found = False

        for k, v in enumerate(self.products):
            if (v.getName() == name):
                if (v.getAmount() <= amount):
                    self.products.pop(k)
                    print("All product has been removed")

                else:
                    v.setAmount(v.getAmount() - amount)
                    v.setWorth(v.getPrice() * v.getAmount())

                found = True
                break

        if (found == False):
            print("There is no such product in the basket")

    def allCost(self):
        together = 0

        for v in self.products:
            together = together + v.getWorth()

        return together

    def summary(self):
        print("Shopping basket summary:")
        self.showBasket()
        together = self.allCost()
        if (together > 10):
            print("For shopping over 10 $ we give 10% reduction.")
            print(f"After discount: {format(together * 0.9, '.2f')}")

        print("Thank you for shopping!")

class Shop(Basket):
    print("Welcome to the store!")

    def __init__(self):
        try:
            f = open("product_objects.dat", "rb")
            self.products = pickle.load(f)
            f.close()
        except:
            f = open("product_objects.dat", "wb")
            pickle.dump([], f)
            f.close()

        self.menu()

    def menu(self):
        while (True):

            f = open("product_objects.dat", "rb")
            self.products = pickle.load(f)
            f.close()

            dec = input("A - add product, S - show basket, D - delete product, 'ENTER' - END : ").upper()

            if (dec == "A"):

                plik = open("shopping_basket_assortment.txt", "r")
                print("Store assortment:")
                for i in plik:
                    assortment = i.split(" ")
                    print(f"{assortment[0].strip()} {assortment[1].strip()} {assortment[2].strip()} "
                          f"{assortment[3].strip()} {assortment[4].strip()}")

                plik.close()

                choice = input("Enter product name: ").lower()
                amount = int(input("How many?: "))

                if (amount <= 0):
                    print("Please enter a positive number greater than zero")
                    continue

                else:
                    plik = open("shopping_basket_assortment.txt", "r")
                    found = False
                    for v in plik:
                        assortment = v.split(" ")
                        if (assortment[1] == choice):

                            name = assortment[1].strip()
                            price = float(assortment[3].strip())
                            worth = price * amount
                            self.addProduct(name, price, amount, worth)
                            found = True
                            break
                    plik.close()

                    if (found == False):
                        print("There is no such product")

            elif (dec == "S"):
                self.showBasket()

            elif (dec == "D"):
                name = input("Enter the name of the product you want to delete: ").lower()
                amount = int(input(f"How many pieces do you want to delete?: "))
                self.deleteProduct(name, amount)

            elif (dec == ""):
                self.summary()
                break

            f = open("product_objects.dat", "wb")
            pickle.dump(self.products, f)
            f.close()


try:
    sklep = Shop()

except:
    print("Unexpected error")
