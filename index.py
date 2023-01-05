from bank.bank import Bank

if __name__ == '__main__':
    a = [['name1', 12413, 'savings', 167],
         ['name2', 1434, 'current', 15],
         ['name2', 13413, 'savings', 12]]

    account = []

    for line_item in a:
        _acc = Bank().create_account(line_item[0], line_item[2], line_item[3], line_item[1])
        account.append(_acc)

    for i in account:
        i: Bank
        print(i.account_info())
        