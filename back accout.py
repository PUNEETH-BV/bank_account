class back_accouts(object):
    def __init__(self,name,accout_no,password,balance=0):
        self.name=name
        self.account_no = accout_no
        self.password = password
        self.balance = balance
    
    def deposit(self,amount):
        if not isinstance(amount,int):
            raise TypeError("please enter only integers ")
        elif amount <= 0:
            raise ValueError("please enter amount greater than zero")
        else :
            self.balance += amount
    def withdraw(self,amount):
        if not isinstance(amount,int):
            raise TypeError("please enter only integers ")
        elif amount <= 0:
            raise ValueError("please enter amount greater than zero")
        elif amount > self.balance:
            raise ValueError("insufficient balance")
        else :
            self.balance -= amount
            return self.balance


if __name__ == '__main__':
    new = back_accouts("puneeth",123,"pue@123")
    new.deposit(1000)
    print(new.name)
    print(new.balance)
    print(new.account_no)
    print(new.password)
    new.deposit(500)
    print(new.balance)
    new.withdraw(200)
    print(new.balance)



        
    