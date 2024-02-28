class Bank:
    def __init__(self, name):
        self.__name  = name
        self.__user_list = []
        #self.__card_list = []
        self.__atm_list = []
        self.__seller_list = []

    @property
    def name(self):
        return self.__name

    @property
    def user_list(self):
        return self.__user_list

    # @property
    # def card_list(self):
    #     return self.__card_list

    @property
    def atm_list(self):
        return self.__atm_list

    @property
    def seller_list(self):
        return self.__seller_list
        
    def add_user(self, user):
        self.__user_list.append(user)
    
    def search_user_from_id(self, citizen_id):
        for user in self.__user_list:
            if user.citizen_id == citizen_id:
                return user

    def add_atm_machine(self, atm):
        self.__atm_list.append(atm)

    def add_seller(self,seller):
        self.__seller_list.append(seller)

    def search_atm_machine(self, machine_id):
        for atm in self.__atm_list:
            if atm.atm_no == machine_id:
                return atm

    def search_account_from_card(self, card_no):
        for user in self.__user_list:
            for account in user.account_list:
                if account.get_card().card_no == card_no:
                    return account

    def search_account_from_account_no(self, account_no):
        for user in self.__user_list:
            for account in user.account_list:
                if account.account_no == account_no:
                    return account
    
    def search_seller(self, seller_name):
        for seller in self.__seller_list:
            if seller.name == seller_name:
                return seller

class User:
    def __init__(self, citizen_id, name):
        self.__citizen_id = citizen_id
        self.__name = name
        self.__account_list = []

    @property
    def citizen_id(self):
        return self.__citizen_id

    @property
    def name(self):
        return self.__name

    @property
    def account_list(self):
        return self.__account_list

    def add_account(self, account):
        self.__account_list.append(account)

    def search_account(self, account_no):
        for account in self.__account_list:
            if account.account_no == account_no:
                return account

class Account:
    def __init__(self, account_no, user, amount):
        self.__account_no = account_no
        self.__user = user
        self.__amount = amount
        self.__transaction = []

    def __add__(self, money):
        if money >= 0:
            self.__amount += money
        

    def __sub__(self, money):
        if money > 0 and money <= self.__amount:
            self.__amount -= money

    @property
    def account_no(self):
        return self.__account_no

    @property
    def user(self):
        return self.__user

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount += amount

    @property
    def transaction(self):
        return self.__transaction

    def transfer(self, counter,money,account):
        if money < 0:
            return "Error"
        else:
            self.__amount -= money
            account + money
            transaction = Transaction("T", money, account.amount,account.user.name)
            account.transaction.append(transaction)

class SavingAccount(Account):
    interest_rate = 0.5 #ดอกเบี้ยออมทรัพย์
    type = "Saving"

    def __init__(self, account_no, user, amount):
        Account.__init__(self, account_no, user, amount)
        self.__card = None

    def get_card(self):
        return self.__card

    def add_card(self, card):
        self.__card = card

class FixDepositAccount(Account):
    interest_rate = 2.5 

class Transaction:
    def __init__(self, transaction_type, amount, total, target_account):
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.__total = total
        self.__target_account = target_account

    def __str__(self):
        return f'{self.__transaction_type}, {self.__amount}, {self.__total}, {self.__target_account}'

    @property
    def transaction_type(self):
        return self.__transaction_type

    @property
    def amount(self):
        return  self.__amount

    @property
    def total(self):
        return  self.__total

    @property
    def target_account(self):
        return self.__target_account

class Card:
    def __init__(self, card_no, account, pin):
        self.__card_no = card_no
        self.__account = account
        self.__pin = pin

    @property
    def card_no(self):
        return self.__card_no

    @property
    def account(self):
        return self.__account

    @property
    def pin(self):
        return self.__pin

class ATM_Card(Card):
    fee = 150

class Debit_Card(Card):
    fee = 300

class ATM_machine:
    withdraw_limit = 20000

    def __init__(self, atm_no, money):
        self.__atm_no = atm_no
        self.__money = money

    @property
    def atm_no(self):
        return self.__atm_no

    @property
    def money(self):
        return self.__money

    def insert_card(self, card, pin):
        if atm_card.pin == pin:
            return "Success"
        return None

    def deposit(self, account, amount):
        if amount < 0:
            return "Error"
        else:
            account + amount
            self.__money += amount
            transaction = Transaction("D",amount,account.amount,'')
            account.transaction.append(transaction)

    def withdraw(self, account, amount):
        if amount > ATM_machine.withdraw_limit or amount < 0:
            return "Error"
        else:
            account - amount
            self.__money -= amount
            transaction = Transaction("W",amount,account.amount,'')
            account.transaction.append(transaction)

    def transfer(self, account, amount, target_account):
        pass

class Seller:
    def __init__(self, seller_no, name):
        self.__seller_no = seller_no
        self.__name = name
        self.__edc_list = []

    @property
    def seller_no(self):
        return self.__seller_no

    @property
    def name(self):
        return self.__name

    @property
    def edc_list(self):
        return self.__edc_list

    def add_edc(self, edc):
        self.__edc_list.append(edc)

    def search_edc_from_no(self, edc_no):
        for edc in self.__edc_list:
            if edc.edc_no == edc_no:
                return edc

    def paid(self, account, money, target_account):
        account - money
        target_account + money
        transaction = Transaction("P", money, account.amount, target_account.user.name)
        account.transaction.append(transaction)

class EDC_machine:
    def __init__(self, edc_no, seller):
        self.__edc_no = edc_no
        self.__seller = seller

    @property
    def edc_no(self):
        return self.__edc_no

    @property
    def seller(self):
        return self.__seller

    def paid(self, cardtype, money, target):
        cardtype.account - money
        target + money
        transaction = Transaction("P", money, cardtype.account.amount,target.user.name)
        cardtype.account.transaction.append(transaction)


##################################################################################  

# กำหนด รูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, ประเภทบัญชี, หมายเลขบัญชี, จำนวนเงินในบัญชี, ประเภทบัตร, หมายเลขบัตร ]}
user ={'1-1101-12345-12-0':['Harry Potter','Savings','1234567890',20000,'ATM','12345'],
    '1-1101-12345-13-0':['Hermione Jean Granger','Saving','0987654321',1000,'Debit','12346'],
    '1-1101-12345-13-0':['Hermione Jean Granger','Fix Deposit','0987654322',1000,'',''],
    '9-0000-00000-01-0':['KFC','Savings','0000000321',0,'',''],
    '9-0000-00000-02-0':['Tops','Savings','0000000322',0,'','']}

atm ={'1001':1000000,'1002':200000}

seller_dic = {'210':"KFC", '220':"Tops"}

EDC = {'2101':"KFC", '2201':"Tops"}

# TODO 1 : สร้าง Instance ของธนาคาร และ สร้าง Instance ของ User, Account, บัตร
# TODO   : จากข้อมูลใน user รูปแบบการนำข้อมูลไปใช้สามารถใช้ได้โดยอิสระ
# TODO   : โดย Account แบ่งเป็น 2 subclass คือ Savings และ FixedDeposit
# TODO   : โดย บัตร แบ่งเป็น 2 subclass คือ ATM และ Debit

scb = Bank('SCB')
scb.add_user(User('1-1101-12345-12-0','Harry Potter'))
scb.add_user(User('1-1101-12345-13-0','Hermione Jean Granger'))
scb.add_user(User('9-0000-00000-01-0','KFC'))
scb.add_user(User('9-0000-00000-02-0','Tops'))

harry = scb.search_user_from_id('1-1101-12345-12-0')
harry.add_account(SavingAccount('1234567890', harry, 20000))
harry_account = harry.search_account('1234567890')
harry_account.add_card(ATM_Card('12345', harry, '1234'))

hermione = scb.search_user_from_id('1-1101-12345-13-0')#แก้เลข 2 เป็น 3
hermione.add_account(SavingAccount('0987654321',hermione,2000))
hermione_account1 = hermione.search_account('0987654321')
hermione_account1.add_card(Debit_Card('12346',hermione_account1,'1234'))
hermione.add_account(FixDepositAccount('0987654322',hermione,1000))

kfc = scb.search_user_from_id('9-0000-00000-01-0')
kfc.add_account(SavingAccount('0000000321', kfc, 0))
tops = scb.search_user_from_id('9-0000-00000-02-0')
tops.add_account(SavingAccount('0000000322', tops, 0))

# TODO 2 : สร้าง Instance ของเครื่อง ATM

scb.add_atm_machine(ATM_machine('1001',1000000))
scb.add_atm_machine(ATM_machine('1002',200000))

# TODO 3 : สร้าง Instance ของ Seller และใส่เครื่อง EDC ใน Seller 

temp = Seller('210','KFC')
temp.add_edc(EDC_machine('2101',temp))
scb.add_seller(temp)

temp = Seller('220',"Tops")
temp.add_edc(EDC_machine('2201',temp))
scb.add_seller(temp)

# TODO 4 : สร้าง method ฝาก โดยใช้ __add__ ถอน โดยใช้ __sub__ และ โอนโดยใช้ __rshift__
# TODO   : ทดสอบการ ฝาก ถอน โอน โดยใช้ + - >> กับบัญชีแต่ละประเภท

# TODO 5 : สร้าง method insert_card, deposit, withdraw และ transfer ที่ตู้ atm และเรียกผ่าน account อีกที
# TODO   : ทดสอบโอนเงินระหว่างบัญชีแต่ละประเภท

# TODO 6 : สร้าง method paid ที่เครื่อง EDC และเรียกผ่าน account อีกที

# TODO 7 : สร้าง method __iter__ ใน account สำหรับส่งคืน transaction เพื่อให้ใช้กับ for ได้ 

# Test case #1 : ทดสอบ การฝาก จากเครื่อง ATM โดยใช้บัตร ATM ของ harry
# ต้องมีการ insert_card ก่อน ค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method deposit จากเครื่อง ATM และเรียกใช้ + จาก account
# ผลที่คาดหวัง :
# Test Case #1
# Harry's ATM No :  12345
# Harry's Account No :  1234567890
# Success
# Harry account before deposit :  20000
# Deposit 1000
# Harry account after deposit :  21000

atm_machine = scb.search_atm_machine('1001')
harry_account = scb.search_account_from_card('12345')
atm_card = harry_account.get_card()
print("Test Case #1")
print("Harry's ATM No : ",atm_card.card_no)
print("Harry's Account No : ",harry_account.account_no)
print(atm_machine.insert_card(atm_card, "1234"))
print("Harry account before deposit : ",harry_account.amount)
print("Deposit 1000")
atm_machine.deposit(harry_account,1000)
print("Harry account after deposit : ",harry_account.amount)
print("")

# Test case #2 : ทดสอบ การถอน จากเครื่อง ATM โดยใช้บัตร ATM ของ hermione
# ต้องมีการ insert_card ก่อน ค้นหาเครื่อง atm เครื่องที่ 2 และบัตร atm ของ hermione
# และเรียกใช้ function หรือ method withdraw จากเครื่อง ATM และเรียกใช้ - จาก account
# ผลที่คาดหวัง :
# Test Case #2
# Hermione's ATM No :  12346
# Hermione's Account No :  0987654321
# Success
# Hermione account before withdraw :  2000
# withdraw 1000
# Hermione account after withdraw :  1000

atm_machine = scb.search_atm_machine('1002')
hermione_account = scb.search_account_from_card('12346')
atm_card = hermione_account.get_card()
print("Test Case #2")
print("Hermione's ATM No : ", atm_card.card_no)
print("Hermione's Account No : ", hermione_account.account_no)
print(atm_machine.insert_card(atm_card, "1234"))
print("Hermione account before withdraw : ",hermione_account.amount)
print("withdraw 1000")
atm_machine.withdraw(hermione_account,1000)
print("Hermione account after withdraw : ",hermione_account.amount)
print("")


# Test case #3 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ที่เคาน์เตอร์
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง
# Test Case #3
# Harry's Account No :  1234567890
# Hermione's Account No :  0987654321
# Harry account before transfer :  21000
# Hermione account before transfer :  1000
# Harry account after transfer :  11000
# Hermione account after transfer :  11000

harry_account = scb.search_account_from_card('12345')
hermione_account = scb.search_account_from_card('12346')
print("Test Case #3")
print("Harry's Account No : ",harry_account.account_no)
print("Hermione's Account No : ", hermione_account.account_no)
print("Harry account before transfer : ",harry_account.amount)
print("Hermione account before transfer : ",hermione_account.amount)
harry_account.transfer("0000", 10000, hermione_account)
print("Harry account after transfer : ",harry_account.amount)
print("Hermione account after transfer : ",hermione_account.amount)
print("")

# Test case #4 : ทดสอบการชำระเงินจากเครื่องรูดบัตร ให้เรียกใช้ method paid จากเครื่องรูดบัตร
# โดยให้ hermione ชำระเงินไปยัง KFC จำนวน 500 บาท ผ่านบัตรของตัวเอง
# ผลที่คาดหวัง
# Hermione's Debit Card No :  12346
# Hermione's Account No :  0987654321
# Seller :  KFC
# KFC's Account No :  0000000321
# KFC account before paid :  0
# Hermione account before paid :  11000
# KFC account after paid :  500
# Hermione account after paid :  10500

hermione_account = scb.search_account_from_account_no('0987654321')
debit_card = hermione_account.get_card()
kfc_account = scb.search_account_from_account_no('0000000321')
kfc = scb.search_seller('KFC')
edc = kfc.search_edc_from_no('2101')

print("Test Case #4")
print("Hermione's Debit Card No : ", debit_card.card_no)
print("Hermione's Account No : ",hermione_account.account_no)
print("Seller : ", kfc.name)
print("KFC's Account No : ", kfc_account.account_no)
print("KFC account before paid : ",kfc_account.amount)
print("Hermione account before paid : ",hermione_account.amount)
edc.paid(debit_card, 500, kfc_account)
print("KFC account after paid : ",kfc_account.amount)
print("Hermione account after paid : ",hermione_account.amount)
print("")

# Test case #5 : ทดสอบการชำระเงินแบบอิเล็กทรอนิกส์ ให้เรียกใช้ method paid จาก kfc
# โดยให้ Hermione ชำระเงินไปยัง Tops จำนวน 500 บาท
# ผลที่คาดหวัง
# Test Case #5
# Hermione's Account No :  0987654321
# Tops's Account No :  0000000322
# Tops account before paid :  0
# Hermione account before paid :  10500
# Tops account after paid :  500
# Hermione account after paid :  10000

hermione_account = scb.search_account_from_account_no('0987654321')
debit_card = hermione_account.get_card()
tops_account = scb.search_account_from_account_no('0000000322')
tops = scb.search_seller('Tops')
print("Test Case #5")
print("Hermione's Account No : ",hermione_account.account_no)
print("Tops's Account No : ", tops_account.account_no)
print("Tops account before paid : ",tops_account.amount)
print("Hermione account before paid : ",hermione_account.amount)
tops.paid(hermione_account,500,tops_account)
print("Tops account after paid : ",tops_account.amount)
print("Hermione account after paid : ",hermione_account.amount)
print("")


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด โดยใช้ for loop 
for tran in hermione_account.transaction:
    print(tran)

