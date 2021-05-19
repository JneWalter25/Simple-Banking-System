import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()


class Banking:

    def __init__(self):
        self.iin = 400000
        self.balance = 0
        self.out = False
        self.out2 = False
        self.out3 = False
        self.cringe = 0
        self.falselogin = False
        self.cardnot = False
        cur.execute('''
        DROP TABLE IF EXISTS card
        ''')

    def menu(self):
        if self.cringe == 0:
            cur.execute('''CREATE TABLE card(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NUMBER TEXT,
                PIN TEXT,
                BALANCE INTEGER DEFAULT 0)
                ''')
        self.cringe = self.cringe + 1
        while True:

            if self.out2 == True:
                return
            print(" ")
            print("1. Create an account")
            print("2. Log into account")
            print("0. Exit")

            self.decide = int(input())
            if self.decide == 1:
                Banking.create(self)
            elif self.decide == 2:
                Banking.checkCard(self)
            elif self.decide == 0:
                self.out2 = True
                print("Bye!")
                return

    def card(self):
        self.y = 0
        self.x = ""
        self.card1 = ""
        self.realcard = ""
        self.pincard = ""
        self.iin2 = str(self.iin)
        for i in range(9):
            self.y = random.randint(0, 9)
            self.x = str(self.y)
            self.card1 = self.card1 + self.x
        self.realcard = self.iin2 + self.card1
        for i in range(4):
            self.x = random.randint(0, 9)
            self.y = str(self.x)
            self.pincard = self.pincard + self.y

    def login(self):
        while True:
            if self.out == True:
                return
            print(" ")
            print("1. Balance")
            print("2.Add income")
            print("3. Do transfer")
            print("4. Close accout")
            print("5. Log out")
            print("0. Exit")

            self.decide = int(input())
            if self.decide == 1:
                print(" ")
                print("Balance:", self.balance)
            elif self.decide == 2:
                print("Enter income:")
                self.addbalance = int(input())
                self.balance = self.addbalance + self.balance
                cur.execute('UPDATE card SET BALANCE = (?) WHERE NUMBER = (?)', [self.balance, self.tempcard])
                conn.commit()
                print("Income was added!")
            elif self.decide == 3:
                Banking.dotransfer(self)
            elif self.decide == 4:

                cur.execute('DELETE FROM card WHERE PIN = (?)', [self.temppin])
                conn.commit()
                print("The account has been closed!")
                Banking.menu(self)
                return None
            elif self.decide == 5:
                print(" ")
                print("You have successfully logged out!")
                self.out = True
                Banking.menu(self)
            elif self.decide == 0:
                print("Bye!")
                self.out2 = True
                break

    def create(self):
        Banking.card(self)
        Banking.checkfinalsum(self)
        print(" ")
        print("Your card has been created")
        print("Your card number:")
        print(self.realcard)
        print("Your card PIN:")
        print(self.pincard)
        Banking.Sqlcard(self)

    def checkCard(self):
        print(" ")
        print("Enter your card number:")
        self.tempcard = input()
        print("Enter your PIN:")
        self.temppin = input()

        for i in self.cards:
            if self.tempcard == i:
                for i in self.pins:
                    if self.temppin == i:
                        print("You have successfully logged in!")
                        Banking.login(self)
                        self.out3 = True
                        self.falselogin = True
            else:
                self.falselogin = False
        if self.out3 == True:
            return
        if not self.falselogin:
            print(" ")
            print("Wrong card number or PIN!")
            Banking.menu(self)

    def Sqlcard(self):
        self.example_card = (
            "INSERT INTO card VALUES(NULL,?,?,0)"
        )
        cur.execute(self.example_card, (self.realcard, self.pincard))

        cur.execute("SELECT * FROM card")
        self.comparation = ""
        self.much = cur.fetchall()
        self.pins = [item[2] for item in self.much]
        self.cards = [item[1] for item in self.much]
        self.lastcard1 = self.much[-1]
        conn.commit()

    def checkfinalsum(self):
        self.odd = True
        self.mylist = []
        self.yikes = 0
        self.sum = 0
        self.checksum = 0
        for i in range(15):
            self.mylist.append(self.realcard[i:i + 1])
            self.mylist[i] = int(self.mylist[i])

        for i in range(15):
            if self.odd == True:
                self.mylist[i] = self.mylist[i] * 2
                self.odd = False
            else:
                self.odd = True

        for i in range(15):
            if self.mylist[i] > 9:
                self.mylist[i] = self.mylist[i] - 9

        for i in range(15):
            self.sum += self.mylist[i]

        for i in range(10):
            if (self.sum + i) % 10 == 0:
                self.checksum = i
        self.checksum = str(self.checksum)
        self.realcard = self.realcard + self.checksum

    def dotransfer(self):
        print("Enter card number:")
        self.transfercard = input()
        for i in self.cards:
            if self.transfercard == i:
                print("Enter how much money you want to transfer:")
                self.moneytransfer = int(input())
                if self.balance < self.moneytransfer:
                    print("Not enough money!")
                    self.cardnot = False
                    Banking.login(self)
                    break
                else:
                    print("Success")
                    self.balance = self.balance - self.moneytransfer
                    self.cardnot = False
                    cur.execute('UPDATE card SET BALANCE = (?) WHERE NUMBER = (?)', [self.balance, self.tempcard])
                    conn.commit()
                    cur.execute('UPDATE card SET BALANCE = (?) WHERE NUMBER = (?)', [self.moneytransfer, self.transfercard])
                    conn.commit()
                    self.out = True
                    break


            elif self.transfercard == self.tempcard:
                print("You can't transfer money to the same account!")
                Banking.login(self)
                self.cardnot = False
                break

            else:
                self.cardnot = True

        if self.cardnot:
            self.checktemp = self.transfercard[-1]

            self.transfercard2 = self.transfercard.rstrip(self.transfercard[-1])


            self.odd = True
            self.mylist = []
            self.yikes = 0
            self.sum = 0
            self.checksum = 0
            for i in range(15):
                self.mylist.append(self.transfercard2[i:i + 1])
                self.mylist[i] = int(self.mylist[i])

            for i in range(15):
                if self.odd == True:
                    self.mylist[i] = self.mylist[i] * 2
                    self.odd = False
                else:
                    self.odd = True

            for i in range(15):
                if self.mylist[i] > 9:
                    self.mylist[i] = self.mylist[i] - 9

            for i in range(15):
                self.sum += self.mylist[i]

            self.checktemp = int(self.checktemp)
            if (self.sum + self.checktemp) % 10 == 0:
                print("Such a card does not exist.")
                Banking.login(self)
                self.out = True
                return None
            else:
                print("Probably you made a mistake in the card number. Please try again!")
                Banking.login(self)
                self.out = True
                return None


card1 = Banking()
card1.menu()
