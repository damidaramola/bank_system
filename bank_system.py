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
    
    #display all
    def display(self):
        if not self.wallet:
            return f"No transactions available in your wallet"
        return "\n".join([transaction.display_info() for transaction in self.wallet]) #calls display_info method
    
    #search wallet method
    
    def search(self,query):
        found = [trans for trans in self.wallet if query.lower() in trans.title.lower() or query.lower in trans.type.lower() ] #check if what youre looking for is in current list
        if not found:
            return f"No Transactions!"
        return "\n".join([transaction.display_info() for transaction in found])
        