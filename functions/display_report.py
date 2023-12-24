import pandas as pd
from prettytable import PrettyTable


def display_transactions(user_id, display_type):
    df = pd.read_csv("./data/transaction_data.csv")
    table = PrettyTable()
    if display_type == "withdraw":
        filter_condition = (df["user_id"] == user_id) & (df["transaction_type"] == "withdraw")
        table.field_names = ["Transaction Type", "Transaction Date", "Transaction Amount"]
    elif display_type == "deposit":
        filter_condition = (df["user_id"] == user_id) & (df["transaction_type"] == "deposit")
        table.field_names = ["Transaction Type", "Transaction Date", "Transaction Amount"]
    else:
        filter_condition = (df["user_id"] == user_id)
        table.field_names = ["Transaction Type", "Transaction Date", "Transaction Amount", "Balance"]

    filtered_transactions = df.loc[filter_condition, ["transaction_type", "transaction_date", "transaction_amount"]]
    balance = 0
    has_transactions = False

    for index, row in filtered_transactions.iterrows():
        has_transactions = True
        if row["transaction_type"] == "deposit":
            transaction_amount = f"{row['transaction_amount']}"
            balance += row["transaction_amount"]
        elif row["transaction_type"] == "withdraw":
            transaction_amount = f"({row['transaction_amount']})"
            balance -= row["transaction_amount"]
        else:
            transaction_amount = row["transaction_amount"]

        if display_type == "all":
            balance_str = f"{balance}" if balance >= 0 else f"({-balance})"
            table.add_row([row["transaction_type"], row["transaction_date"], transaction_amount, balance_str])
        else:
            table.add_row([row["transaction_type"], row["transaction_date"], transaction_amount])

    if not has_transactions:
        print("No transactions recorded.")

    if has_transactions:
        print(table)
