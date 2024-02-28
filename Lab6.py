# Class Code
class Bank:
    def __init__(self):
        self.__user_list = []
        self.__atm_list = []

    def create_user_list(self, user_data, account, atm_card):
        self.__user_list.append((user, account, atm_card))

    def create_atm_list(self, atm):
        self.__atm_list.append(atm)

    @property
    def user_list(self):
        return self.__user_list

    @property
    def atm_list(self):
        return self.__atm_list
    
class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name

    @property
    def name(self):
        return self.__name

class Bank_Account:
    def __init__(self, account_number, balance, owner):
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = int(balance)
        self.__transaction_list = []
        self.__transaction_show_list = []
        
    def __str__(self):
        return "\n".join(self.__transaction_show_list)

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    @property
    def transaction_list(self):
        return self.__transaction_list

    # ฝาก
    def deposit(self, atm_machine, money):
        if money > 0 and atm_machine.limit >= money:
            result1 = f"{self.__owner.name} account before test : {self.balance}"
            account.__balance += money
            atm_machine.limit = money
            atm_machine.money_remaining_deposit = money

            transaction_show_list_detail = f"{self.owner.name} transaction : D-ATM:{atm_machine.machine_number}-{money}"
            self.__transaction_show_list.append(transaction_show_list_detail)
            result2 = f"{self.owner.name} account after test : {self.balance}"
            self.__transaction_list.append(Transaction('Deposit', money, None, atm_machine.machine_number, None))
            
            return f"{result1}\n{result2}"
        return "Error"
    
    # ถอน
    def withdraw(self, atm_machine, money):
        if money > 0 and self.balance >= money and atm_machine.limit >= money and atm_machine.money_remaining >= money:
            result1 = f"{self.owner.name} account before test : {self.balance}"
            self.__balance -= money
            atm_machine.limit = money
            atm_machine.money_remaining_withdraw = money
            
            transaction_show_list_detail = f"{self.owner.name} transaction : W-ATM:{atm_machine.machine_number}-{money}"
            self.__transaction_show_list.append(transaction_show_list_detail)
            result2 = f"{self.owner.name} account after test : {self.balance}" 
            self.__transaction_list.append(Transaction('Withdraw', money, None, atm_machine.machine_number, None))
        
            return f"{result1}\n{result2}"
        return "Error"

    # โอน
    def transfer(self, atm_machine, partner, money):
        if money > 0 and self.balance >= money:
            result1 = F"{self.owner.name} account before test : {self.__balance}"
            self.__balance -= money
            atm_machine.limit = money
            self.__transaction_show_list.append(F"{self.owner.name} transaction : T-ATM:{atm_machine.machine_number}-{money}-{self.__balance}")
            result2 = F"{self.owner.name} account after test : {self.__balance}"
            
            result3 = F"{partner.owner.name} account before test : {partner.__balance}"
            partner.__balance += money
            partner.__transaction_show_list.append(F"{partner.owner.name} transaction : T-ATM:{atm_machine.machine_number}-+{money}-{partner.__balance}")
            result4 = F"{partner.owner.name} account after test : {partner.__balance}"
            
            self.__transaction_list.append(Transaction('Transfer', money, None, atm_machine.machine_number, self.__account_number))
        
            return F"{result1}\n{result2}\n{result3}\n{result4}"
        return "Error"

# เก็บประวัติการทำธุรกรรม
class Transaction:
    def __init__(self, transaction_type, amount, date, machine_number, partner):
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.__date = date
        self.__machine_number = machine_number
        self.__partner = partner

class ATM_card:
    annual_fee = 150
    def __init__(self, card_number, pin, account_number):
        self.__card_number = card_number
        self.__pin = pin 
        self.__account_number = account_number
        
    @property
    def card_number(self):
        return self.__card_number

    @property
    def pin(self):
        return self.__pin

    @property
    def account_number(self):
        return self.__account_number

class ATM:
    def __init__(self, machine_number, money_remaining):
        self.__machine_number = machine_number
        self.__money_remaining = money_remaining
        self.__limit = 40000

    @property
    def machine_number(self):
        return self.__machine_number
    
    @property
    def limit(self):
        return self.__limit
    
    @property
    def money_remaining(self):
        return self.__money_remaining
    
    @limit.setter
    def limit(self, money):
        if self.__limit >= money:
            self.__limit -= money
            
    @money_remaining.setter
    def money_remaining_deposit(self, money):
        self.__money_remaining += money_remaining
            
    @money_remaining.setter
    def money_remaaining_withdraw(self, money):
        if self.__money_remaining >= money:
            self.__money_remaining -= money_remaining

    def insert_card(self, atm_card, pin):
        if atm_card.pin == pin:
            return atm_card.card_number, atm_card.account_number ,"Sucess"
        return None


##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
user_data ={
    '1-1101-12345-12-0':['Harry Potter','1234567890', '12345', 20000],
    '1-1101-12345-13-0':['Hermione Jean Granger','0987654321', '12346', 1000]
}

atm = {
    '1001':1000000,
    '1002':200000
}

bank_instance = Bank()

for user_id, data in user_data.items():
    user = User(user_id, data[0])
    account = Bank_Account(data[1], data[3], user)
    atm_card = ATM_card(data[2], '12345', account.account_number)
    bank_instance.create_user_list(user, account, atm_card)

for atm_number, money_remaining in atm.items():
    bank_instance.create_atm_list(ATM(atm_number, money_remaining))

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 3 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) instance ของ atm_card 3) entered Pin ที่ user input ให้เครื่อง ATM
# TODO     return ถ้าบัตร และ Pin ถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM

# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 2 ตัว คือ 
# TODO     1) instance ของ account 2) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0

#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
print("Test Case #1")
print(bank_instance.atm_list[0].insert_card(bank_instance.user_list[0][2], '12345'))
print("")



# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
print("Test Case #2")
print(bank_instance.user_list[1][1].deposit(bank_instance.atm_list[1], 1000))
print("")

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test Case #3")
print(bank_instance.user_list[1][1].deposit(bank_instance.atm_list[1], -1))
print("")


# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
print("Test Case #4")
print(bank_instance.user_list[1][1].withdraw(bank_instance.atm_list[1], 500))
print("")

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test Case #5")
print(bank_instance.user_list[1][1].withdraw(bank_instance.atm_list[1], 2000))
print("")

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
print("Test Case #6")
print(bank_instance.user_list[0][1].transfer(bank_instance.atm_list[1], bank_instance.user_list[1][1], 10000))
print("")


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500
print("Test Case #7")
print(bank_instance.user_list[1][1])
print("")