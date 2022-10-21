from enum import Enum
"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class Commission(Enum):
    NONE = 0
    CONTRACT = 1
    BONUS = 2


class Employee:
    pay = 0
    message = ""
    def __init__(self, name, monthly:bool=False, salary:int=0, hours:int=0, 
                 hourly_rate:int=0, commission:Commission=Commission.NONE, contracts:int=0, 
                 contract_rate:int=0, bonus:int=0):
        
        self.name = name
        self.pay += (hours * hourly_rate,salary)[monthly]
        self.message += "works on a "
        self.message += [f"contract of {hours} hours at {hourly_rate}/hour",
                         f"monthly salary of {salary}"][monthly]
        
        if commission != Commission.NONE:
            self.pay += (contracts * contract_rate, bonus)[commission.value-1]
            
            self.message += " and receives a "
            self.message += (f"commission for {contracts} contract(s) at {contract_rate}/contract",
                         f"bonus commission of {bonus}")[commission.value-1]
        
        self.message += f".  Their total pay is {self.pay}."

    def get_pay(self):
        return self.pay

    def __str__(self):
        return f"{self.name} {self.message}"


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', monthly=True, salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hours=100, hourly_rate=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', monthly=True, salary=3000, commission=Commission.CONTRACT, contracts=4, contract_rate=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours=150, hourly_rate=25, commission=Commission.CONTRACT, contracts=3, contract_rate=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', monthly=True, salary=2000, commission=Commission.BONUS, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours=120, hourly_rate=30, commission=Commission.BONUS, bonus=600)
