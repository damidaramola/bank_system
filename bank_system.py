import json

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
        
    #remove an existing transaction using the title
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
       
    # save wallet info in json file
    def save_file(self,filename="wallet.json"):
        data = [{'Expense':transaction.title,'Amount':transaction.amount,'Type':transaction.type,'Note':transaction.note} for transaction in self.wallet]
        with open(filename,"w") as file:
            json.dump(data,file)
            
    # load file back into format so python can read it
    def load_file(self,filename="wallet.json"):
        try:
            with open(filename,"r") as file:
                data = json.load(file)
                self.wallet = [Transaction(trans['title'], trans['amount'],trans['type'],trans['note'])for trans in data]
        except FileNotFoundError:
            print('File Not Found')      
    
def main():
    wallet = Bank()

    while True:
        print("\n===== Personal Banking System =====")
        print("1.Add a Transaction")
        print("2.Remove a Transaction")
        print("3.Display all Transactions")
        print("4.Search for a transaction")
        print("5.Save Transaction to file")
        print("6.Load Transactions for file")
        print("7.Exit")
        choice = int(input("Enter your choice (1-7): "))
        
        if choice == 1:
            title = input("Enter the title: ")
            amount = float(input("Enter the amount: "))
            type = input("Expense or Deposit: ")
            transaction= Transaction(title,amount,type)
            wallet.add_transaction(transaction)
            print(f"\n {title} added successfully")
        
        elif choice == 2:
            title = input("Enter the title: ")
            print(wallet.remove_transaction(title))
        

        elif choice == 3:
            print(wallet.display())
            
        elif choice == 4:
            query = input("Enter query")
            print(wallet.search(query))
        
        elif choice == 5:
            wallet.save_file()
            print("saved file as json")
            
        elif choice == 6:
            wallet.load_file()
            print('Load file as json')
        
        elif choice == 7:
            print('Exiting the program.Goodbye!')
            break
        else:
            print("invalid choice.Please try again")
                
if __name__ in "__main__":
    main()                
    
            
        