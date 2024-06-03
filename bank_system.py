"class based banking system project"

class Transaction:
    #what properties is each transaction going to have?
    def __init__(self,title,amount,type, note=""):
        self.title = title 
        self.amount = amount
        self.type = type
        self.note = note
    
    def display_info(self):
        return f"Transaction:\n Expense:{self.title}\n Amount:{self.amount}\n Type:{self.type}\n Note:{self.note}"    
    
    
class Bank:
    def __init__(self):
        self.wallet = [] # initialize your wallet
    #add   
    def add_transaction(self,transaction): 
        self.wallet.append(transaction)
        
    #remove an existing transaction
    def del_transaction(self,title):
        for trans in self.wallet:
            if trans.title == title:
                self.wallet.remove(trans)
                return f"{title} has been removed!"
        return f"{title} is not found..."    
    
        