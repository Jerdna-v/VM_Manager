import re
import sqlite3
from tkinter import messagebox

import test5
import test6

global conn
conn = sqlite3.connect('test2.db')
global cur
cur = conn.cursor()
class Machine():
    def __init__(self, from_, date_, data):
        self.email = from_
        self.date = date_
        self.data = data
        self.old_data= data
        self.name = ''

    def promet_setter(self):
        conn.execute(f'''CREATE TABLE IF NOT EXISTS "{self.code}+{self.name}+Promet+{self.date[3:]}" (
                                    "Day"	Text,
                                    "Promet"	INTEGER
                                );''')

    def price_setter(self):
        cur.execute(f'''SELECT name FROM sqlite_master WHERE type='table' AND name='{self.code}+{self.name}+Prices' ''')
        identifier = cur.fetchall()
        if identifier == [] and self.name == 'Canto':
            conn.execute(f'''CREATE TABLE "{self.code}+{self.name}+Prices" (
                                        "Pay2"	INTEGER,
                                        "Pay3"	INTEGER,
                                        "Pay4"	INTEGER,
                                        "Pay5"	INTEGER,
                                        "Pay6"	INTEGER,
                                        "Pay7"	INTEGER,
                                        "Pay8"	INTEGER,
                                        "Pay9"	INTEGER,
                                        "Pay10"	INTEGER,
                                        "Pay12"	INTEGER,
                                        "Pay13"	INTEGER,
                                        "Pay14"	INTEGER,
                                        "Pay15"	INTEGER,
                                        "Pay16"	INTEGER,
                                        "Pay17"	INTEGER,
                                        "Pay18"	INTEGER,
                                        "Pay19"	INTEGER,
                                        "Pay20"	INTEGER,
                                        "Pay21"	INTEGER,
                                        "Pay22"	INTEGER,
                                        "Pay23"	INTEGER,
                                        "Pay24"	INTEGER,
                                        "Pay25"	INTEGER,
                                        "Pay26"	INTEGER,
                                        "Pay27"	INTEGER,
                                        "Pay29"	INTEGER,
                                        "Pay30"	INTEGER,
                                        "Pay31"	INTEGER,
                                        "Pay32"	INTEGER,
                                        "Pay33"	INTEGER,
                                        "Pay34"	INTEGER,
                                        "Pay35"	INTEGER,
                                        "Pay36"	INTEGER,
                                        "Pay37"	INTEGER,
                                        "Pay38"	INTEGER,
                                        "Pay39"	INTEGER,
                                        "Pay40"	INTEGER
                                    );''')
            cur.execute(f'''INSERT INTO "{self.code}+{self.name}+Prices" VALUES (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ''')
        if identifier == [] and self.name == 'Astro35':
            conn.execute(f'''CREATE TABLE "{self.code}+{self.name}+Prices" (
                                "Pay1"	INTEGER,
                                "Pay2"	INTEGER,
                                "Pay3"	INTEGER,
                                "Pay4"	INTEGER,
                                "Pay5"	INTEGER,
                                "Pay6"	INTEGER,
                                "Pay7"	INTEGER,
                                "Pay8"	INTEGER,
                                "Pay9"	INTEGER,
                                "Pay10"	INTEGER,
                                "Pay11"	INTEGER,
                                "Pay12"	INTEGER,
                                "Pay13"	INTEGER,
                                "Pay14"	INTEGER,
                                "Pay15"	INTEGER,
                                "Pay16"	INTEGER,
                                "Pay17"	INTEGER,
                                "Pay18"	INTEGER,
                                "Pay21"	INTEGER,
                                "Pay22"	INTEGER,
                                "Pay23"	INTEGER,
                                "Pay24"	INTEGER,
                                "Pay25"	INTEGER,
                                "Pay26"	INTEGER,
                                "Pay27"	INTEGER,
                                "Pay28"	INTEGER,
                                "Pay29"	INTEGER,
                                "Pay30"	INTEGER,
                                "Pay31"	INTEGER,
                                "Pay32"	INTEGER,
                                "Pay33"	INTEGER,
                                "Pay34"	INTEGER,
                                "Pay35"	INTEGER
                                                    );''')
            cur.execute(f'''INSERT INTO "{self.code}+{self.name}+Prices" VALUES (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ''')
        if identifier == [] and (self.name == 'Astro40(1e)' or self.name == 'Astro40'):
            conn.execute(f'''CREATE TABLE "{self.code}+{self.name}+Prices" (
                                        "Pay1"	INTEGER,
                                        "Pay2"	INTEGER,
                                        "Pay3"	INTEGER,
                                        "Pay4"	INTEGER,
                                        "Pay5"	INTEGER,
                                        "Pay6"	INTEGER,
                                        "Pay7"	INTEGER,
                                        "Pay8"	INTEGER,
                                        "Pay9"	INTEGER,
                                        "Pay10"	INTEGER,
                                        "Pay11"	INTEGER,
                                        "Pay12"	INTEGER,
                                        "Pay13"	INTEGER,
                                        "Pay14"	INTEGER,
                                        "Pay15"	INTEGER,
                                        "Pay16"	INTEGER,
                                        "Pay17"	INTEGER,
                                        "Pay18"	INTEGER,
                                        "Pay21"	INTEGER,
                                        "Pay22"	INTEGER,
                                        "Pay23"	INTEGER,
                                        "Pay24"	INTEGER,
                                        "Pay25"	INTEGER,
                                        "Pay26"	INTEGER,
                                        "Pay27"	INTEGER,
                                        "Pay28"	INTEGER,
                                        "Pay29"	INTEGER,
                                        "Pay30"	INTEGER,
                                        "Pay31"	INTEGER,
                                        "Pay32"	INTEGER,
                                        "Pay33"	INTEGER,
                                        "Pay34"	INTEGER,
                                        "Pay35"	INTEGER,
                                        "Pay36"	INTEGER,
                                        "Pay37"	INTEGER,
                                        "Pay38"	INTEGER,
                                        "Pay39"	INTEGER,
                                        "Pay40"	INTEGER
                                                            );''')
            cur.execute(f'''INSERT INTO "{self.code}+{self.name}+Prices" VALUES (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ''')
        if identifier == [] and (self.name == 'FSE' or self.name == 'Kikko'):
            conn.execute(f'''CREATE TABLE "{self.code}+{self.name}+Prices" (
                                        "Pay1"	INTEGER,
                                        "Pay2"	INTEGER,
                                        "Pay3"	INTEGER,
                                        "Pay4"	INTEGER,
                                        "Pay5"	INTEGER,
                                        "Pay6"	INTEGER,
                                        "Pay7"	INTEGER,
                                        "Pay8"	INTEGER,
                                        "Pay9"	INTEGER,
                                        "Pay10"	INTEGER,
                                        "Pay11"	INTEGER,
                                        "Pay12"	INTEGER,
                                        "Pay13"	INTEGER,
                                        "Pay14"	INTEGER,
                                        "Pay15"	INTEGER,
                                        "Pay16"	INTEGER
                                                        );''')
            cur.execute(f'''INSERT INTO "{self.code}+{self.name}+Prices" VALUES (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ''')
        if identifier == [] and (self.name == 'Colibri' or self.name == 'Colibri(1e)' or self.name == 'Venezia' or self.name == 'Brio'):
            conn.execute(f'''CREATE TABLE "{self.code}+{self.name}+Prices" (
                                        "Pay1"	INTEGER,
                                        "Pay2"	INTEGER,
                                        "Pay3"	INTEGER,
                                        "Pay4"	INTEGER,
                                        "Pay5"	INTEGER,
                                        "Pay6"	INTEGER,
                                        "Pay7"	INTEGER,
                                        "Pay8"	INTEGER
                                                        );''')
            cur.execute(f'''INSERT INTO "{self.code}+{self.name}+Prices" VALUES (0,0,0,0,0,0,0,0) ''')
        if identifier == [] and self.name == 'VeneziaLX':
            conn.execute(f'''CREATE TABLE "{self.code}+{self.name}+Prices" (
                                                    "Pay1"	INTEGER,
                                                    "Pay2"	INTEGER,
                                                    "Pay3"	INTEGER,
                                                    "Pay4"	INTEGER,
                                                    "Pay5"	INTEGER,
                                                    "Pay6"	INTEGER,
                                                    "Pay7"	INTEGER,
                                                    "Pay8"	INTEGER,
                                                    "Pay9"	INTEGER,
                                                    "Pay10"	INTEGER
                                                                        );''')
            cur.execute(f'''INSERT INTO "{self.code}+{self.name}+Prices" VALUES (0,0,0,0,0,0,0,0,0,0) ''')
        if identifier == [] and self.name == 'Astro40(s)':
            conn.execute(f'''CREATE TABLE "{self.code}+{self.name}+Prices" (
                                        "Pay1"	INTEGER,
                                        "Pay2"	INTEGER,
                                        "Pay3"	INTEGER,
                                        "Pay4"	INTEGER,
                                        "Pay5"	INTEGER,
                                        "Pay6"	INTEGER,
                                        "Pay7"	INTEGER,
                                        "Pay8"	INTEGER,
                                        "Pay9"	INTEGER,
                                        "Pay10"	INTEGER,
                                        "Pay11"	INTEGER,
                                        "Pay12"	INTEGER,
                                        "Pay13"	INTEGER,
                                        "Pay14"	INTEGER,
                                        "Pay15"	INTEGER,
                                        "Pay16"	INTEGER,
                                        "Pay17"	INTEGER,
                                        "Pay18"	INTEGER
                                                            );''')
            cur.execute(f'''INSERT INTO "{self.code}+{self.name}+Prices" VALUES (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ''')
        # test5.everything(self.code, self.name, numEnt=self.num)

    def size_identifier(self):
        try:
            self.name = str(re.compile(r'(KIKKO)').findall(self.data)[0])
        except IndexError:
            pass
        if len(self.data) >= 2200 or self.name == 'KIKKO':
            self.data = re.compile(r'(Cod. = \d{8})|(TOTAL COUNT\s\S*\s*\d{6,10})|([N,n]\D{0,3}.o\D?.Total =\s\d{1,8})|(maint\S{0,3}Total = \d{1,8})|(SELECTION N\S{0,2}.\s*\d{1,2} Total = \d{1,8})|(Coin N. \d Total = \d{1,8})|(TOTAL CASH\S{0,2} Tot. = \d{1,6})|(TOTAL CASH \S?\s?CRED.\s?Tot. = \d{1,8})|(Counter \S?\s?\d{1,6})').findall(self.data)
        elif len(self.data) <= 2000:
            self.data = re.compile(r'(od+\S*\s+\S{0,4}\s*=\s+\d{1,4})|([P,p]+\w{0,7}\s\w{1,2}.\s=\s\d{0,6})|(Pa\D{4,7}\d{1,6})|(Test\s*=\s\d{1,6})|(Pr\D{1,2}\s*\d{1,2}\s*=\s\d{1,6})|([C,M]o\D{1,2}\s*\d{1,6}\s*=\s*\d{1,6})|(et.\s*=\s\d{1,6})|(CA\S{2,4}\s*\D{0,7}\s=\s*\d{1,9})|(I\S{1,5}\s*=\s\d{1,6})|(Er\D{0,2}\d{1,2}\s*=\s\d{1,6})').findall(self.data)
        if len(self.data) == 0:
            self.data = re.compile(
                r'(od+\S*\s+\S{0,4}\s*=\s+\d{1,4})|([P,p]+\w{0,7}\s\w{1,2}.\s=\s\d{0,6})|(Pa\D{4,7}\d{1,6})|(Test\s*=\s\d{1,6})|(Pr\D{1,2}\s*\d{1,2}\s*=\s\d{1,6})|([C,M]o\D{1,2}\s*\d{1,6}\s*=\s*\d{1,6})|(et.\s*=\s\d{1,6})|(CA\S{2,4}\s*\D{0,7}\s=\s*\d{1,9})|(I\S{1,5}\s*=\s\d{1,6})|(Er\D{0,2}\d{1,2}\s*=\s\d{1,6})').findall(
                self.old_data)
        n = 0
        for tupl in self.data:
            for el in tupl:
                if el == '':
                    continue
                self.data[n] = el
                n+=1

    def data_sorter(self):
        n=0
        print(self.email, self.date)
        for el in self.data:
            self.data[n] = re.sub("[^0-9]", "", el)
            n+=1
        if self.name == 'KIKKO':
            self.name = 'Kikko'
            n=4
            for w in self.data[4:20]:
                self.data[n] = w[2:]
                n+=1
            n=-8
            for w in self.data[-8:-2]:
                self.data[n] = w[1:]
                n+=1
            self.num = 16
        elif len(self.data) == 47:
            self.name = 'Colibri'
            n = 18
            for w in self.data[18:35]:
                self.data[n] = w[1:]
                n += 1
            for w in self.data[35:39]:
                self.data[n] = w[2:]
                n += 1
            n = -8
            for w in self.data[-8:-2]:
                self.data[n] = w[1:]
                n += 1
            self.num = 8
        elif len(self.data) == 48:
            self.name = 'Colibri(1e)'
            n = 18
            for w in self.data[18:35]:
                self.data[n] = w[1:]
                n += 1
            for w in self.data[35:39]:
                self.data[n] = w[2:]
                n += 1
            n = -8
            for w in self.data[-8:-2]:
                self.data[n] = w[1:]
                n += 1
            self.num = 8
        if len(self.data) == 75:
            self.name = 'FSE'
            n = 34
            for w in self.data[34:43]:
                self.data[n] = w[1:]
                n += 1
            for w in self.data[43:50]:
                self.data[n] = w[2:]
                n += 1
            for w in self.data[50:56]:
                self.data[n] = w[1:]
                n += 1
            n = -16
            for w in self.data[-16:-7]:
                self.data[n] = w[1:]
                n += 1
            for w in self.data[-7:]:
                self.data[n] = w[2:]
                n += 1
            self.num = 16
        if len(self.data) == 46:
            try:
                self.name = str(re.compile(r'(BRIO)').findall(self.old_data)[0])
            except IndexError:
                pass
            if not self.name:
                self.name = 'Venezia'
            else:
                self.name = 'Brio'
            n = 18
            for w in self.data[18:32]:
                self.data[n] = w[1:]
                n += 1
            n = -11
            for w in self.data[-11:-2]:
                self.data[n] = w[1:]
                n += 1
            for w in self.data[-2:]:
                self.data[n] = w[2:]
                n += 1
            self.num = 8
        if len(self.data) == 50:
            self.name = 'VeneziaLX'
            n = 22
            for w in self.data[22:36]:
                self.data[n] = w[1:]
                n += 1
            n=-11
            for w in self.data[-11:-2]:
                self.data[n] = w[1:]
                n += 1
            for w in self.data[-2:]:
                self.data[n] = w[2:]
                n += 1
            self.num = 10
        if len(self.data) == 115:
            self.name = 'Canto'
            n = 4
            for w in self.data[4:12]:
                self.data[n] = w[1:]
                n += 1
            for w in self.data[12:41]:
                self.data[n] = w[2:]
                n += 1
            n = -8
            for w in self.data[-8:-2]:
                self.data[n] = w[1:]
                n += 1
            self.num = 37
        if len(self.data) == 74:
            self.name = 'Astro35'
            n = 4
            for w in self.data[4:13]:
                self.data[n] = w[1:]
                n += 1
            for w in self.data[13:37]:
                self.data[n] = w[2:]
                n += 1
            n = -8
            for w in self.data[-8:-2]:
                self.data[n] = w[1:]
                n += 1
            self.num = 33
        if len(self.data) == 80:
            self.name = 'Astro40'
            n = 4
            for w in self.data[4:13]:
                self.data[n] = w[1:]
                n += 1
            for w in self.data[13:42]:
                self.data[n] = w[2:]
                n += 1
            n = -8
            for w in self.data[-8:-2]:
                self.data[n] = w[1:]
                n += 1
            self.num = 38
        if len(self.data) == 79:
            self.name = 'Astro40(1e)'
            n = 4
            for w in self.data[4:13]:
                self.data[n] = w[1:]
                n += 1
            for w in self.data[13:42]:
                self.data[n] = w[2:]
                n += 1
            n = -8
            for w in self.data[-8:-2]:
                self.data[n] = w[1:]
                n += 1
            self.num = 38
        if len(self.data) == 59:
            self.name = 'Astro40(s)'
            n = 4
            for w in self.data[4:13]:
                self.data[n] = w[1:]
                n += 1
            for w in self.data[13:22]:
                self.data[n] = w[2:]
                n += 1
            n = -8
            for w in self.data[-8:-2]:
                self.data[n] = w[1:]
                n += 1
            self.num = 18
        n=0
        print(self.data)
        for w in self.data:
            self.data[n] = int(w)
            n+=1

        self.code = self.data.pop(0)
        self.data.insert(0, self.email)
        self.data.insert(0, self.date)

    def table_auth(self):
        conn.execute('''CREATE TABLE IF NOT EXISTS "machines" (
                        "Code"	INTEGER UNIQUE,
                        "Name"	TEXT,
                        "Location"	TEXT,
                        "Description"	TEXT,
                        PRIMARY KEY("Code")
                                            );''')
        conn.execute('''INSERT INTO "machines" (Code, Name) VALUES (?,?)''', (self.code, self.name))

        #conn.execute('''CREATE TABLE IF NOT EXISTS "emails" (
        #                "Email"	TEXT UNIQUE,
        #                "Name"	TEXT,
        #                "Description"	TEXT,
        #                PRIMARY KEY("Email")
        #                                    );''')
        #conn.execute(f'''INSERT INTO "emails" (Email) VALUES ({self.email})''')
        #conn.commit()

    def table_machine(self):
        if self.name == 'FSE':
            conn.execute(f'''CREATE TABLE IF NOT EXISTS "{self.code}+FSE+Prints" (
                            "Date"	TEXT,
                            "Email"	TEXT,
                            "Print"	INTEGER,
                            "Pay1"	INTEGER,
                            "Test1"	INTEGER,
                            "Pay2"	INTEGER,
                            "Test2"	INTEGER,
                            "Pay3"	INTEGER,
                            "Test3"	INTEGER,
                            "Pay4"	INTEGER,
                            "Test4"	INTEGER,
                            "Pay5"	INTEGER,
                            "Test5"	INTEGER,
                            "Pay6"	INTEGER,
                            "Test6"	INTEGER,
                            "Pay7"	INTEGER,
                            "Test7"	INTEGER,
                            "Pay8"	INTEGER,
                            "Test8"	INTEGER,
                            "Pay9"	INTEGER,
                            "Test9"	INTEGER,
                            "Pay10"	INTEGER,
                            "Test10"	INTEGER,
                            "Pay11"	INTEGER,
                            "Test11"	INTEGER,
                            "Pay12"	INTEGER,
                            "Test12"	INTEGER,
                            "Pay13"	INTEGER,
                            "Test13"	INTEGER,
                            "Pay14"	INTEGER,
                            "Test14"	INTEGER,
                            "Pay15"	INTEGER,
                            "Test15"	INTEGER,
                            "Pay16"	INTEGER,
                            "Test16"	INTEGER,
                            "Price1"	INTEGER,
                            "Price2"	INTEGER,
                            "Price3"	INTEGER,
                            "Price4"	INTEGER,
                            "Price5"	INTEGER,
                            "Price6"	INTEGER,
                            "Price7"	INTEGER,
                            "Price8"	INTEGER,
                            "Price9"	INTEGER,
                            "Price10"	INTEGER,
                            "Price11"	INTEGER,
                            "Price12"	INTEGER,
                            "Price13"	INTEGER,
                            "Price14"	INTEGER,
                            "Price15"	INTEGER,
                            "Price16"	INTEGER,
                            "Coin1"	INTEGER,
                            "Coin2"	INTEGER,
                            "Coin3"	INTEGER,
                            "Coin4"	INTEGER,
                            "Coin5"	INTEGER,
                            "Coin6"	INTEGER,
                            "Token"	INTEGER,
                            "Total Cash"	INTEGER,
                            "Total Credit"	INTEGER,
                            "Error1"	INTEGER,
                            "Error2"	INTEGER,
                            "Error3"	INTEGER,
                            "Error4"	INTEGER,
                            "Error5"	INTEGER,
                            "Error6"	INTEGER,
                            "Error7"	INTEGER,
                            "Error8"	INTEGER,
                            "Error9"	INTEGER,
                            "Error10"	INTEGER,
                            "Error11"	INTEGER,
                            "Error12"	INTEGER,
                            "Error13"	INTEGER,
                            "Error14"	INTEGER,
                            "Error15"	INTEGER,
                            "Error16"	INTEGER
                                            );''')
            conn.execute(f'''INSERT INTO "{self.code}+FSE+Prints" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',self.data)

        if self.name == 'Colibri':
            conn.execute(f'''CREATE TABLE IF NOT EXISTS"{self.code}+Colibri+Prints" (
                            "Date"	TEXT,
                            "Email"	TEXT,
                            "Print"	INTEGER,
                            "Pay1"	INTEGER,
                            "Test1"	INTEGER,
                            "Pay2"	INTEGER,
                            "Test2"	INTEGER,
                            "Pay3"	INTEGER,
                            "Test3"	INTEGER,
                            "Pay4"	INTEGER,
                            "Test4"	INTEGER,
                            "Pay5"	INTEGER,
                            "Test5"	INTEGER,
                            "Pay6"	INTEGER,
                            "Test6"	INTEGER,
                            "Pay7"	INTEGER,
                            "Test7"	INTEGER,
                            "Pay8"	INTEGER,
                            "Test8"	INTEGER,
                            "Price1"	INTEGER,
                            "Price2"	INTEGER,
                            "Price3"	INTEGER,
                            "Price4"	INTEGER,
                            "Price5"	INTEGER,
                            "Price6"	INTEGER,
                            "Price7"	INTEGER,
                            "Price8"	INTEGER,
                            "Coin1"	INTEGER,
                            "Coin2"	INTEGER,
                            "Coin3"	INTEGER,
                            "Coin4"	INTEGER,
                            "Coin5"	INTEGER,
                            "Coin6"	INTEGER,
                            "TotalCash"	INTEGER,
                            "TotalCredit"	INTEGER,
                            "Error1"	INTEGER,
                            "Error2"	INTEGER,
                            "Error3"	INTEGER,
                            "Error4"	INTEGER,
                            "Error5"	INTEGER,
                            "Error6"	INTEGER,
                            "Error7"	INTEGER,
                            "Error8"	INTEGER,
                            "Error9"	INTEGER,
                            "Error10"	INTEGER,
                            "Error11"	INTEGER,
                            "Error12"	INTEGER,
                            "Error13"	INTEGER
                                            );''')
            conn.execute(f'''INSERT INTO "{self.code}+Colibri+Prints" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',self.data)
        if self.name == 'Colibri(1e)':
            conn.execute(f'''CREATE TABLE IF NOT EXISTS"{self.code}+Colibri(1e)+Prints" (
                            "Date"	TEXT,
                            "Email"	TEXT,
                            "Print"	INTEGER,
                            "Pay1"	INTEGER,
                            "Test1"	INTEGER,
                            "Pay2"	INTEGER,
                            "Test2"	INTEGER,
                            "Pay3"	INTEGER,
                            "Test3"	INTEGER,
                            "Pay4"	INTEGER,
                            "Test4"	INTEGER,
                            "Pay5"	INTEGER,
                            "Test5"	INTEGER,
                            "Pay6"	INTEGER,
                            "Test6"	INTEGER,
                            "Pay7"	INTEGER,
                            "Test7"	INTEGER,
                            "Pay8"	INTEGER,
                            "Test8"	INTEGER,
                            "Price1"	INTEGER,
                            "Price2"	INTEGER,
                            "Price3"	INTEGER,
                            "Price4"	INTEGER,
                            "Price5"	INTEGER,
                            "Price6"	INTEGER,
                            "Price7"	INTEGER,
                            "Price8"	INTEGER,
                            "Coin1"	INTEGER,
                            "Coin2"	INTEGER,
                            "Coin3"	INTEGER,
                            "Coin4"	INTEGER,
                            "Coin5"	INTEGER,
                            "Coin6"	INTEGER,
                            "TotalCash"	INTEGER,
                            "TotalCredit"	INTEGER,
                            "Error1"	INTEGER,
                            "Error2"	INTEGER,
                            "Error3"	INTEGER,
                            "Error4"	INTEGER,
                            "Error5"	INTEGER,
                            "Error6"	INTEGER,
                            "Error7"	INTEGER,
                            "Error8"	INTEGER,
                            "Error9"	INTEGER,
                            "Error10"	INTEGER,
                            "Error11"	INTEGER,
                            "Error12"	INTEGER,
                            "Error13"	INTEGER,
                            "Error14"	INTEGER
                                            );''')
            conn.execute(f'''INSERT INTO "{self.code}+Colibri(1e)+Prints" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',self.data)
        if self.name == 'Brio' or self.name == 'Venezia':
            conn.execute(f'''CREATE TABLE IF NOT EXISTS "{self.code}+{self.name}+Prints" (
                            "Date"	TEXT,
                            "Email"	TEXT,
                            "Print"	INTEGER,
                            "Pay1"	INTEGER,
                            "Test1"	INTEGER,
                            "Pay2"	INTEGER,
                            "Test2"	INTEGER,
                            "Pay3"	INTEGER,
                            "Test3"	INTEGER,
                            "Pay4"	INTEGER,
                            "Test4"	INTEGER,
                            "Pay5"	INTEGER,
                            "Test5"	INTEGER,
                            "Pay6"	INTEGER,
                            "Test6"	INTEGER,
                            "Pay7"	INTEGER,
                            "Test7"	INTEGER,
                            "Pay8"	INTEGER,
                            "Test8"	INTEGER,
                            "Price1"	INTEGER,
                            "Price2"	INTEGER,
                            "Price3"	INTEGER,
                            "Price4"	INTEGER,
                            "Price5"	INTEGER,
                            "Price6"	INTEGER,
                            "Price7"	INTEGER,
                            "Price8"	INTEGER,
                            "Coin1"	INTEGER,
                            "Coin2"	INTEGER,
                            "Coin3"	INTEGER,
                            "Coin4"	INTEGER,
                            "Coin5"	INTEGER,
                            "Coin6"	INTEGER,
                            "Token"	INTEGER,
                            "Total Cash"	INTEGER,
                            "Total Credit"	INTEGER,
                            "Error1"	INTEGER,
                            "Error2"	INTEGER,
                            "Error3"	INTEGER,
                            "Error4"	INTEGER,
                            "Error5"	INTEGER,
                            "Error6"	INTEGER,
                            "Error7"	INTEGER,
                            "Error8"	INTEGER,
                            "Error9"	INTEGER,
                            "Error10"	INTEGER,
                            "Error11"	INTEGER
                                                );''')
            conn.execute(
                f'''INSERT INTO "{self.code}+{self.name}+Prints" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                self.data)
        if self.name == 'VeneziaLX':
            conn.execute(f'''CREATE TABLE IF NOT EXISTS "{self.code}+VeneziaLX+Prints" (
                                        "Date"	TEXT,
                                        "Email"	TEXT,
                                        "Print"	INTEGER,
                                        "Pay1"	INTEGER,
                                        "Test1"	INTEGER,
                                        "Pay2"	INTEGER,
                                        "Test2"	INTEGER,
                                        "Pay3"	INTEGER,
                                        "Test3"	INTEGER,
                                        "Pay4"	INTEGER,
                                        "Test4"	INTEGER,
                                        "Pay5"	INTEGER,
                                        "Test5"	INTEGER,
                                        "Pay6"	INTEGER,
                                        "Test6"	INTEGER,
                                        "Pay7"	INTEGER,
                                        "Test7"	INTEGER,
                                        "Pay8"	INTEGER,
                                        "Test8"	INTEGER,
                                        "Pay9"	INTEGER,
                                        "Test9"	INTEGER,
                                        "Pay10"	INTEGER,
                                        "Test10"	INTEGER,
                                        "Price1"	INTEGER,
                                        "Price2"	INTEGER,
                                        "Price3"	INTEGER,
                                        "Price4"	INTEGER,
                                        "Price5"	INTEGER,
                                        "Price6"	INTEGER,
                                        "Price7"	INTEGER,
                                        "Price8"	INTEGER,
                                        "Coin1"	INTEGER,
                                        "Coin2"	INTEGER,
                                        "Coin3"	INTEGER,
                                        "Coin4"	INTEGER,
                                        "Coin5"	INTEGER,
                                        "Coin6"	INTEGER,
                                        "Token"	INTEGER,
                                        "Total Cash"	INTEGER,
                                        "Total Credit"	INTEGER,
                                        "Error1"	INTEGER,
                                        "Error2"	INTEGER,
                                        "Error3"	INTEGER,
                                        "Error4"	INTEGER,
                                        "Error5"	INTEGER,
                                        "Error6"	INTEGER,
                                        "Error7"	INTEGER,
                                        "Error8"	INTEGER,
                                        "Error9"	INTEGER,
                                        "Error10"	INTEGER,
                                        "Error11"	INTEGER
                                                            );''')
            conn.execute(
                f'''INSERT INTO "{self.code}+VeneziaLX+Prints" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                self.data)
        if self.name == 'Canto':
            conn.execute(f'''CREATE TABLE IF NOT EXISTS "{self.code}+Canto+Prints" (
                            "Date"	TEXT,
                            "Email"	TEXT,
                            "Print"	INTEGER,
                            "Sold"	INTEGER,
                            "Tested"	INTEGER,
                            "Pay2"	INTEGER,
                            "Pay3"	INTEGER,
                            "Pay4"	INTEGER,
                            "Pay5"	INTEGER,
                            "Pay6"	INTEGER,
                            "Pay7"	INTEGER,
                            "Pay8"	INTEGER,
                            "Pay9"	INTEGER,
                            "Pay10"	INTEGER,
                            "Pay12"	INTEGER,
                            "Pay13"	INTEGER,
                            "Pay14"	INTEGER,
                            "Pay15"	INTEGER,
                            "Pay16"	INTEGER,
                            "Pay17"	INTEGER,
                            "Pay18"	INTEGER,
                            "Pay19"	INTEGER,
                            "Pay20"	INTEGER,
                            "Pay21"	INTEGER,
                            "Pay22"	INTEGER,
                            "Pay23"	INTEGER,
                            "Pay24"	INTEGER,
                            "Pay25"	INTEGER,
                            "Pay26"	INTEGER,
                            "Pay27"	INTEGER,
                            "Pay29"	INTEGER,
                            "Pay30"	INTEGER,
                            "Pay31"	INTEGER,
                            "Pay32"	INTEGER,
                            "Pay33"	INTEGER,
                            "Pay34"	INTEGER,
                            "Pay35"	INTEGER,
                            "Pay36"	INTEGER,
                            "Pay37"	INTEGER,
                            "Pay38"	INTEGER,
                            "Pay39"	INTEGER,
                            "Pay40"	INTEGER,
                            "Coin1"	INTEGER,
                            "Coin2"	INTEGER,
                            "Coin3"	INTEGER,
                            "Coin4"	INTEGER,
                            "Coin5"	INTEGER,
                            "Coin6"	INTEGER,
                            "Total Cash"	INTEGER,
                            "Total Credit"	INTEGER,
                            "Error1"	INTEGER,
                            "Error2"	INTEGER,
                            "Error3"	INTEGER,
                            "Error4"	INTEGER,
                            "Error5"	INTEGER,
                            "Error6"	INTEGER,
                            "Error7"	INTEGER,
                            "Error8"	INTEGER,
                            "Error9"	INTEGER,
                            "Error10"	INTEGER,
                            "Error11"	INTEGER,
                            "Error12"	INTEGER,
                            "Error13"	INTEGER,
                            "Error14"	INTEGER,
                            "Error15"	INTEGER,
                            "Error16"	INTEGER,
                            "Error17"	INTEGER,
                            "Error18"	INTEGER,
                            "Error19"	INTEGER,
                            "Error20"	INTEGER,
                            "Error21"	INTEGER,
                            "Error22"	INTEGER,
                            "Error23"	INTEGER,
                            "Error24"	INTEGER,
                            "Error25"	INTEGER,
                            "Error26"	INTEGER,
                            "Error27"	INTEGER,
                            "Error28"	INTEGER,
                            "Error29"	INTEGER,
                            "Error30"	INTEGER,
                            "Error31"	INTEGER,
                            "Error32"	INTEGER,
                            "Error33"	INTEGER,
                            "Error34"	INTEGER,
                            "Error35"	INTEGER,
                            "Error36"	INTEGER,
                            "Error37"	INTEGER,
                            "Error38"	INTEGER,
                            "Error39"	INTEGER,
                            "Error40"	INTEGER,
                            "Error41"	INTEGER,
                            "Error42"	INTEGER,
                            "Error43"	INTEGER,
                            "Error44"	INTEGER,
                            "Error45"	INTEGER,
                            "Error46"	INTEGER,
                            "Error47"	INTEGER,
                            "Error48"	INTEGER,
                            "Error49"	INTEGER,
                            "Error50"	INTEGER,
                            "Error51"	INTEGER,
                            "Error52"	INTEGER,
                            "Error53"	INTEGER,
                            "Error54"	INTEGER,
                            "Error55"	INTEGER,
                            "Error56"	INTEGER,
                            "Error57"	INTEGER,
                            "Error58"	INTEGER,
                            "Error59"	INTEGER,
                            "Error60"	INTEGER,
                            "Error61"	INTEGER,
                            "Error62"	INTEGER,
                            "Error63"	INTEGER,
                            "Error64"	INTEGER,
                            "Error65"	INTEGER,
                            "Error66"	INTEGER
                        );''')
            conn.execute(f'''INSERT INTO "{self.code}+Canto+Prints" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',self.data)
        if self.name == 'Kikko':
            conn.execute(f'''CREATE TABLE IF NOT EXISTS"{self.code}+Kikko+Prints" (
                            "Date"	TEXT,
                            "Email"	TEXT,
                            "Print"	INTEGER,
                            "Sold"	INTEGER,
                            "Tested"	INTEGER,
                            "Pay1"	INTEGER,
                            "Pay2"	INTEGER,
                            "Pay3"	INTEGER,
                            "Pay4"	INTEGER,
                            "Pay5"	INTEGER,
                            "Pay6"	INTEGER,
                            "Pay7"	INTEGER,
                            "Pay8"	INTEGER,
                            "Pay9"	INTEGER,
                            "Pay10"	INTEGER,
                            "Pay11"	INTEGER,
                            "Pay12"	INTEGER,
                            "Pay13"	INTEGER,
                            "Pay14"	INTEGER,
                            "Pay15"	INTEGER,
                            "Pay16"	INTEGER,
                            "Coin1"	INTEGER,
                            "Coin2"	INTEGER,
                            "Coin3"	INTEGER,
                            "Coin4"	INTEGER,
                            "Coin5"	INTEGER,
                            "Coin6"	INTEGER,
                            "Total Cash"	INTEGER,
                            "Total Credit"	INTEGER,
                            "Error1"	INTEGER,
                            "Error2"	INTEGER,
                            "Error3"	INTEGER,
                            "Error4"	INTEGER,
                            "Error5"	INTEGER,
                            "Error6"	INTEGER,
                            "Error7"	INTEGER,
                            "Error8"	INTEGER,
                            "Error9"	INTEGER,
                            "Error10"	INTEGER,
                            "Error11"	INTEGER,
                            "Error12"	INTEGER,
                            "Error13"	INTEGER,
                            "Error14"	INTEGER
                                                );''')
            conn.execute(
                f'''INSERT INTO "{self.code}+Kikko+Prints" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                self.data)
        if self.name == 'Astro35':
            conn.execute(f'''CREATE TABLE IF NOT EXISTS "{self.code}+Astro35+Prints" (
                            "Date"	TEXT,
                            "Email"	TEXT,
                            "Print"	INTEGER,
                            "Sold"	INTEGER,
                            "Tested"	INTEGER,
                            "Pay1"	INTEGER,
                            "Pay2"	INTEGER,
                            "Pay3"	INTEGER,
                            "Pay4"	INTEGER,
                            "Pay5"	INTEGER,
                            "Pay6"	INTEGER,
                            "Pay7"	INTEGER,
                            "Pay8"	INTEGER,
                            "Pay9"	INTEGER,
                            "Pay10"	INTEGER,
                            "Pay11"	INTEGER,
                            "Pay12"	INTEGER,
                            "Pay13"	INTEGER,
                            "Pay14"	INTEGER,
                            "Pay15"	INTEGER,
                            "Pay16"	INTEGER,
                            "Pay17"	INTEGER,
                            "Pay18"	INTEGER,
                            "Pay21"	INTEGER,
                            "Pay22"	INTEGER,
                            "Pay23"	INTEGER,
                            "Pay24"	INTEGER,
                            "Pay25"	INTEGER,
                            "Pay26"	INTEGER,
                            "Pay27"	INTEGER,
                            "Pay28"	INTEGER,
                            "Pay29"	INTEGER,
                            "Pay30"	INTEGER,
                            "Pay31"	INTEGER,
                            "Pay32"	INTEGER,
                            "Pay33"	INTEGER,
                            "Pay34"	INTEGER,
                            "Pay35"	INTEGER,
                            "Coin1"	INTEGER,
                            "Coin2"	INTEGER,
                            "Coin3"	INTEGER,
                            "Coin4"	INTEGER,
                            "Coin5"	INTEGER,
                            "Coin6"	INTEGER,
                            "Total Cash"	INTEGER,
                            "Total Credit"	INTEGER,
                            "Error1"	INTEGER,
                            "Error2"	INTEGER,
                            "Error3"	INTEGER,
                            "Error4"	INTEGER,
                            "Error5"	INTEGER,
                            "Error6"	INTEGER,
                            "Error7"	INTEGER,
                            "Error8"	INTEGER,
                            "Error9"	INTEGER,
                            "Error10"	INTEGER,
                            "Error11"	INTEGER,
                            "Error12"	INTEGER,
                            "Error13"	INTEGER,
                            "Error14"	INTEGER,
                            "Error15"	INTEGER,
                            "Error16"	INTEGER,
                            "Error17"	INTEGER,
                            "Error18"	INTEGER,
                            "Error19"	INTEGER,
                            "Error20"	INTEGER,
                            "Error21"	INTEGER,
                            "Error22"	INTEGER,
                            "Error23"	INTEGER,
                            "Error24"	INTEGER,
                            "Error25"	INTEGER,
                            "Error26"	INTEGER,
                            "Error27"	INTEGER,
                            "Error28"	INTEGER,
                            "Error29"	INTEGER
                                                );''')
            conn.execute(
                f'''INSERT INTO "{self.code}+Astro35+Prints" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                self.data)
        if self.name == 'Astro40':
            conn.execute(f'''CREATE TABLE IF NOT EXISTS "{self.code}+Astro40+Prints" (
                            "Date"	TEXT,
                            "Email"	TEXT,
                            "Print"	INTEGER,
                            "Sold"	INTEGER,
                            "Tested"	INTEGER,
                            "Pay1"	INTEGER,
                            "Pay2"	INTEGER,
                            "Pay3"	INTEGER,
                            "Pay4"	INTEGER,
                            "Pay5"	INTEGER,
                            "Pay6"	INTEGER,
                            "Pay7"	INTEGER,
                            "Pay8"	INTEGER,
                            "Pay9"	INTEGER,
                            "Pay10"	INTEGER,
                            "Pay11"	INTEGER,
                            "Pay12"	INTEGER,
                            "Pay13"	INTEGER,
                            "Pay14"	INTEGER,
                            "Pay15"	INTEGER,
                            "Pay16"	INTEGER,
                            "Pay17"	INTEGER,
                            "Pay18"	INTEGER,
                            "Pay21"	INTEGER,
                            "Pay22"	INTEGER,
                            "Pay23"	INTEGER,
                            "Pay24"	INTEGER,
                            "Pay25"	INTEGER,
                            "Pay26"	INTEGER,
                            "Pay27"	INTEGER,
                            "Pay28"	INTEGER,
                            "Pay29"	INTEGER,
                            "Pay30"	INTEGER,
                            "Pay31"	INTEGER,
                            "Pay32"	INTEGER,
                            "Pay33"	INTEGER,
                            "Pay34"	INTEGER,
                            "Pay35"	INTEGER,
                            "Pay36"	INTEGER,
                            "Pay37"	INTEGER,
                            "Pay38"	INTEGER,
                            "Pay39"	INTEGER,
                            "Pay40"	INTEGER,
                            "Coin1"	INTEGER,
                            "Coin2"	INTEGER,
                            "Coin3"	INTEGER,
                            "Coin4"	INTEGER,
                            "Coin5"	INTEGER,
                            "Coin6"	INTEGER,
                            "Total Cash"	INTEGER,
                            "Total Credit"	INTEGER,
                            "Error1"	INTEGER,
                            "Error2"	INTEGER,
                            "Error3"	INTEGER,
                            "Error4"	INTEGER,
                            "Error5"	INTEGER,
                            "Error6"	INTEGER,
                            "Error7"	INTEGER,
                            "Error8"	INTEGER,
                            "Error9"	INTEGER,
                            "Error10"	INTEGER,
                            "Error11"	INTEGER,
                            "Error12"	INTEGER,
                            "Error13"	INTEGER,
                            "Error14"	INTEGER,
                            "Error15"	INTEGER,
                            "Error16"	INTEGER,
                            "Error17"	INTEGER,
                            "Error18"	INTEGER,
                            "Error19"	INTEGER,
                            "Error20"	INTEGER,
                            "Error21"	INTEGER,
                            "Error22"	INTEGER,
                            "Error23"	INTEGER,
                            "Error24"	INTEGER,
                            "Error25"	INTEGER,
                            "Error26"	INTEGER,
                            "Error27"	INTEGER,
                            "Error28"	INTEGER,
                            "Error29"	INTEGER,
                            "Error30"	INTEGER
                                                );''')
            conn.execute(
                f'''INSERT INTO "{self.code}+Astro40+Prints" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                self.data)
        if self.name == 'Astro40(1e)':
            conn.execute(f'''CREATE TABLE IF NOT EXISTS "{self.code}+Astro40(1e)+Prints" (
                            "Date"	TEXT,
                            "Email"	TEXT,
                            "Print"	INTEGER,
                            "Sold"	INTEGER,
                            "Tested"	INTEGER,
                            "Pay1"	INTEGER,
                            "Pay2"	INTEGER,
                            "Pay3"	INTEGER,
                            "Pay4"	INTEGER,
                            "Pay5"	INTEGER,
                            "Pay6"	INTEGER,
                            "Pay7"	INTEGER,
                            "Pay8"	INTEGER,
                            "Pay9"	INTEGER,
                            "Pay10"	INTEGER,
                            "Pay11"	INTEGER,
                            "Pay12"	INTEGER,
                            "Pay13"	INTEGER,
                            "Pay14"	INTEGER,
                            "Pay15"	INTEGER,
                            "Pay16"	INTEGER,
                            "Pay17"	INTEGER,
                            "Pay18"	INTEGER,
                            "Pay21"	INTEGER,
                            "Pay22"	INTEGER,
                            "Pay23"	INTEGER,
                            "Pay24"	INTEGER,
                            "Pay25"	INTEGER,
                            "Pay26"	INTEGER,
                            "Pay27"	INTEGER,
                            "Pay28"	INTEGER,
                            "Pay29"	INTEGER,
                            "Pay30"	INTEGER,
                            "Pay31"	INTEGER,
                            "Pay32"	INTEGER,
                            "Pay33"	INTEGER,
                            "Pay34"	INTEGER,
                            "Pay35"	INTEGER,
                            "Pay36"	INTEGER,
                            "Pay37"	INTEGER,
                            "Pay38"	INTEGER,
                            "Pay39"	INTEGER,
                            "Pay40"	INTEGER,
                            "Coin1"	INTEGER,
                            "Coin2"	INTEGER,
                            "Coin3"	INTEGER,
                            "Coin4"	INTEGER,
                            "Coin5"	INTEGER,
                            "Coin6"	INTEGER,
                            "Total Cash"	INTEGER,
                            "Total Credit"	INTEGER,
                            "Error1"	INTEGER,
                            "Error2"	INTEGER,
                            "Error3"	INTEGER,
                            "Error4"	INTEGER,
                            "Error5"	INTEGER,
                            "Error6"	INTEGER,
                            "Error7"	INTEGER,
                            "Error8"	INTEGER,
                            "Error9"	INTEGER,
                            "Error10"	INTEGER,
                            "Error11"	INTEGER,
                            "Error12"	INTEGER,
                            "Error13"	INTEGER,
                            "Error14"	INTEGER,
                            "Error15"	INTEGER,
                            "Error16"	INTEGER,
                            "Error17"	INTEGER,
                            "Error18"	INTEGER,
                            "Error19"	INTEGER,
                            "Error20"	INTEGER,
                            "Error21"	INTEGER,
                            "Error22"	INTEGER,
                            "Error23"	INTEGER,
                            "Error24"	INTEGER,
                            "Error25"	INTEGER,
                            "Error26"	INTEGER,
                            "Error27"	INTEGER,
                            "Error28"	INTEGER,
                            "Error29"	INTEGER
                                                );''')
            conn.execute(
                f'''INSERT INTO "{self.code}+Astro40(1e)+Prints" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                self.data)
        if self.name == 'Astro40(s)':
            conn.execute(f'''CREATE TABLE IF NOT EXISTS "{self.code}+Astro40(s)+Prints" (
                            "Date"	TEXT,
                            "Email"	TEXT,
                            "Print"	INTEGER,
                            "Sold"	INTEGER,
                            "Tested"	INTEGER,
                            "Pay1"	INTEGER,
                            "Pay2"	INTEGER,
                            "Pay3"	INTEGER,
                            "Pay4"	INTEGER,
                            "Pay5"	INTEGER,
                            "Pay6"	INTEGER,
                            "Pay7"	INTEGER,
                            "Pay8"	INTEGER,
                            "Pay9"	INTEGER,
                            "Pay10"	INTEGER,
                            "Pay11"	INTEGER,
                            "Pay12"	INTEGER,
                            "Pay13"	INTEGER,
                            "Pay14"	INTEGER,
                            "Pay15"	INTEGER,
                            "Pay16"	INTEGER,
                            "Pay17"	INTEGER,
                            "Pay18"	INTEGER,
                            "Coin1"	INTEGER,
                            "Coin2"	INTEGER,
                            "Coin3"	INTEGER,
                            "Coin4"	INTEGER,
                            "Coin5"	INTEGER,
                            "Coin6"	INTEGER,
                            "Total Cash"	INTEGER,
                            "Total Credit"	INTEGER,
                            "Error1"	INTEGER,
                            "Error2"	INTEGER,
                            "Error3"	INTEGER,
                            "Error4"	INTEGER,
                            "Error5"	INTEGER,
                            "Error6"	INTEGER,
                            "Error7"	INTEGER,
                            "Error8"	INTEGER,
                            "Error9"	INTEGER,
                            "Error10"	INTEGER,
                            "Error11"	INTEGER,
                            "Error12"	INTEGER,
                            "Error13"	INTEGER,
                            "Error14"	INTEGER,
                            "Error15"	INTEGER,
                            "Error16"	INTEGER,
                            "Error17"	INTEGER,
                            "Error18"	INTEGER,
                            "Error19"	INTEGER,
                            "Error20"	INTEGER,
                            "Error21"	INTEGER,
                            "Error22"	INTEGER,
                            "Error23"	INTEGER,
                            "Error24"	INTEGER,
                            "Error25"	INTEGER,
                            "Error26"	INTEGER,
                            "Error27"	INTEGER,
                            "Error28"	INTEGER,
                            "Error29"	INTEGER
                                                );''')
            conn.execute(
                f'''INSERT INTO "{self.code}+Astro40(s)+Prints" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                self.data)
        conn.commit()

    def table_email(self):
        conn.execute(f'''CREATE TABLE IF NOT EXISTS "{self.email}" (
                        "Date"	TEXT,
                        "Code"	INTEGER,
                        "Name"	TEXT,
                        "Location"	TEXT
                                        );''')
        conn.execute(f'''INSERT INTO "{self.email}" (Date, Code, Name) VALUES (?,?,?)''', (self.date, self.code, self.name))
        conn.commit()