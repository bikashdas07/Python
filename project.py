class Bank:
    def _init_(self, name, address, contactno, accnumber, atmno, acc_type, balance):
        self.name = name
        self.address = address
        self.contactno = contactno
        self.accnumber = accnumber
        self.atmno = atmno
        self.type = acc_type
        self.balance = balance
    

    def welcome(self):
        print("\n\t\t\t\xC9\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xBB\n")
        print("\t\t\t\xBA          \xFE\xFE\xFE     \xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE  \xFE         \xFE  \xBA\n")
        print("\t\t\t\xBA         \xFE\xFE\xFE\xFE\xFE         \xFE\xFE\xFE       \xFE\xFE       \xFE\xFE  \xBA\n")
        print("\t\t\t\xBA        \xFE\xFE\xFE \xFE\xFE\xFE        \xFE\xFE\xFE       \xFE\xFE\xFE     \xFE\xFE\xFE  \xBA\n")
        print("\t\t\t\xBA       \xFE\xFE\xFE   \xFE\xFE\xFE       \xFE\xFE\xFE       \xFE\xFE\xFE\xFE   \xFE\xFE\xFE\xFE  \xBA\n")
        print("\t\t\t\xBA      \xFE\xFE\xFE     \xFE\xFE\xFE      \xFE\xFE\xFE       \xFE\xFE \xFE\xFE \xFE\xFE \xFE\xFE  \xBA\n")
        print("\t\t\t\xBA     \xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE     \xFE\xFE\xFE       \xFE\xFE  \xFE\xFE\xFE  \xFE\xFE  \xBA\n")
        print("\t\t\t\xBA    \xFE\xFE\xFE         \xFE\xFE\xFE    \xFE\xFE\xFE       \xFE\xFE   \xFE   \xFE\xFE  \xBA\n")
        print("\t\t\t\xBA   \xFE\xFE\xFE           \xFE\xFE\xFE   \xFE\xFE\xFE       \xFE\xFE       \xFE\xFE  \xBA\n")
        print("\t\t\t\xBA  \xFE\xFE\xFE             \xFE\xFE\xFE  \xFE\xFE\xFE       \xFE\xFE       \xFE\xFE  \xBA\n")
        print("\t\t\t\xBA                                              \xBA\n")
        print("\t\t\t\xC8\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCDSIMULATION\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xCD\xBC\n")
        print("\n")
    def save_users(self,users):
        with open("C:\\Users\\Md Jaffar Hussain\\OneDrive\\Desktop\\coding\\A.txt", "w") as file:
            for user in users:
              file.write(f"Account Holder name: {user.name}\n")
              file.write(f"Account Holder Address: {user.address}\n")
              file.write(f"Contact Number: {user.contactno}\n")
              file.write(f"Account Number: {user.accnumber}\n")
              file.write(f"ATM Number: {user.atmno}\n")
              file.write(f"Account Type: {user.type}\n")
              file.write(f"Account Balance: {user.balance}\n\n")
              print("Information saved Successfully:")
    
    def showdata(self):
        print("\nName:", self.name)
        print("Address:", self.address)
        print("Contact Number:", self.contactno)
        print("Account No:", self.accnumber)
        print("ATM Number:", self.atmno)
        print("Account type:", self.type)
        print("Balance: rs{:.2f}".format(self.balance))
    

    def deposit(self):
        while True:
            try:
                amount = float(input("\nEnter amount to be Deposited: $"))
                if amount > 0:
                    self.balance += amount
                    print("Deposit successful. New balance: ${:.2f}".format(self.balance))
                    break
                else:
                    print("Invalid input. Amount must be positive.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def showbal(self):
        print("\nTotal balance is: ${:.2f}".format(self.balance))

    def withdrawl(self):
        while True:
            try:
                amount = float(input("Enter amount to withdraw: $"))
                if amount > 0 and amount <= self.balance:
                    self.balance -= amount
                    print("Withdrawal successful. Remaining balance: ${:.2f}".format(self.balance))
                    break
                elif amount <= 0:
                    print("Invalid input. Amount must be positive.")
                else:
                    print("Insufficient Balance")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

users = []

while True:
    print("\n__WELCOME\n\n")
    print("Enter Your Choice:")
    print("\t1. Add New Customer Details")
    print("\t2. Show Account Information")
    print("\t3. Deposit Money")
    print("\t4. Show Total balance")
    print("\t5. Withdraw Money")
    print("\t6. Save Information")
    print("\t7. Cancel")

    choice = input()

    if choice == '1':
        name = input("Enter name: ")
        accnumber = input("Enter Account number: ")
        atmno = input("Enter ATM Number: ")
        acc_type = input("Enter Account type: ")
        address = input("Enter Address: ")
        contactno = input("Enter Contact Number: ")
        while True:
            try:
                balance = float(input("Enter Balance: $"))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        user = Bank(name, address, contactno, accnumber, atmno, acc_type, balance)
        users.append(user)
    elif choice == '2':
        for user in users:
            user.showdata()
    elif choice == '3':
        for user in users:
            user.deposit()
    elif choice == '4':
        for user in users:
            user.showbal()
    elif choice == '5':
        for user in users:
            user.withdrawl()
    elif choice == '6':
        for user in users:
            user.save_users(users)
    elif choice == '7':
        break
    else:
        print("\nInvalid choice. Please enter a number from 1 to 6.")