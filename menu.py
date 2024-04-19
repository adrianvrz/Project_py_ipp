from finance import create_account,add_transaction,get_account_balance,get_total_balance

def main():
    # Inicializamos la lista de cuentas
    accounts = []
    # Mostramos el menú principal
    while True:
        
        print("1. Crear cuenta")
        print("2. Agregar transacción")
        print("3. Consultar saldo de cuenta")
        print("4. Consultar saldo total")
        print("5. Salir")

        option = int(input("\nSeleccione una opción: "))

        if option == 1:
            name = input("Ingrese el nombre de la cuenta: ")
            account_type = input("Ingrese el tipo de cuenta (ingreso/egreso): ")
            
            account_id = create_account(accounts, name, account_type)
            
            print(f"\nCuenta creada con éxito. ID de cuenta: {account_id}\n")

        elif option == 2:
            account_id = int(input("Ingrese el ID de la cuenta: "))
            description = input("Ingrese la descripción de la transacción: ")
            amount = float(input("Ingrese el monto de la transacción: "))
            
            add_transaction(accounts, account_id, description, amount)
            
            print("\nTransacción agregada con éxito\n")

        elif option == 3:
            account_id = int(input("Ingrese el ID de la cuenta: "))
            balance = get_account_balance(accounts, account_id)
            
            print(f"\nSaldo de la cuenta: {balance}\n")

        elif option == 4:
            total_balance = get_total_balance(accounts)
            
            print(f"\nSaldo total: {total_balance}\n")

        elif option == 5:
            print("\n¡Hasta luego!")
            break

        else:
            print("\nOpción inválida. Intente de nuevo.\n")

if __name__ == "__main__": 
    main()