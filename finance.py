def create_account(accounts, name, account_type):
    # Generamos el account_id como un autoincremento basado en la longitud de la lista de cuentas
    account_id = len(accounts)
    # Creamos la cuenta como una lista que contiene el account_id, el nombre, el tipo de cuenta y una lista vacía para las transacciones
    account = [account_id, name, account_type, []]
    # Agregamos la cuenta a la lista de cuentas
    accounts.append(account)
    # Retornamos el account_id generado
    return account_id

def add_transaction(accounts, account_id, description, amount):
    # Buscamos la cuenta por el account_id en la lista de cuentas
    for account in accounts:
        if account[0] == account_id:
            # Agregamos la transacción (descripción y monto) a la lista de transacciones de la cuenta
            account[3].append([description, amount])
            # Salimos del bucle una vez que se ha agregado la transacción
            break

def get_account_balance(accounts, account_id):
    # Inicializamos la variable balance en 0
    balance = 0
    # Buscamos la cuenta por el account_id en la lista de cuentas
    for account in accounts:
        if account[0] == account_id:
            # Si encontramos la cuenta, sumamos o restamos el monto de cada transacción según el tipo de cuenta
            for transaction in account[3]:
                if account[2] == "ingreso":
                    balance += transaction[1]
                elif account[2] == "egreso":
                    balance -= transaction[1]
            # Salimos del bucle una vez que se ha calculado el saldo
            break
    # Retornamos el saldo de la cuenta
    return balance

def get_total_balance(accounts):
    # Inicializamos la variable total_balance en 0
    total_balance = 0
    # Iteramos sobre todas las cuentas
    for account in accounts:
        # Obtenemos el saldo de la cuenta actual
        balance = get_account_balance(accounts, account[0])
        # Sumamos el saldo de la cuenta al saldo total
        total_balance += balance
    # Retornamos el saldo total
    return total_balance