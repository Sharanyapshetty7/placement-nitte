def deposit(amt, ch, Account):
    Account[ch] += amt
    print(f"The amount {amt} is deposited to account number {ch}")

def transfer(t_amt, t_acc, ch, Account):
    if Account[ch] < t_amt:
        print("Not enough balance")
    else:
        Account[ch] -= t_amt
        Account[t_acc] += t_amt
        print(f"Amount {t_amt} transferred to {t_acc} from {ch}")

Account = {101: 1000, 102: 2000, 103: 3000}
ch = int(input("Enter your account number: "))

if ch not in Account:
    print("Account not found")
else:
    while True:
        print("\n--- BANK MENU ---")
        print("1 Check Balance\n2 Deposit\n3 Transfer\n4 Withdraw\n5 Logout")
        a = int(input("Enter choice: "))
        
        match a:
            case 1:
                print("Balance is", Account[ch])
            case 2:
                amt = int(input("Enter amount to deposit: "))
                deposit(amt, ch, Account)
            case 3:
                t_acc = int(input("Enter target account: "))
                if t_acc not in Account:
                    print("Account doesn't exist.")
                else:
                    t_amt = int(input("Enter amount to transfer: "))
                    transfer(t_amt, t_acc, ch, Account)
            case 4:
                w_amt = int(input("Enter amount to withdraw: "))
                if w_amt > Account[ch]:
                    print("Insufficient balance")
                else:
                    Account[ch] -= w_amt
                    print(f"Withdrawn {w_amt}")
            case 5:
                print("Logged out.")
                break
