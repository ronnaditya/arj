#! /home/ronnaditya/.venvs/hermes/bin/python3

import os

import numpy as np
import pandas as pd

BASE_DIR = "/home/ronnaditya/Exchange/ARJ/transactions"

file_names = [os.path.join(BASE_DIR, file_name) for file_name in os.listdir(BASE_DIR)]

def aggregate():
    aggregate_transactions = []
    for file_name in file_names:
        with open(file_name, "r") as f:
            read_file = f.read()
        transactions = read_file.split("\n")
        for transaction in transactions:
            elements = transaction.split(" ")
            if elements[-1] != "":
                print(file_name)
                transfer = int(elements[-1])
                name = " ".join(elements[:-1])
                aggregate_transactions.append([file_name.split("/")[-1], name, transfer])

    return aggregate_transactions

def write_aggregate_to_txt(aggregate_transactions):
    for transaction in aggregate_transactions:
        print(transaction)
        transaction[-1] = str(transaction[-1])

    aggregate_string = "\n".join([string for string in [" ".join(transaction) for transaction in aggregate_transactions]])

    with open("aggregate_transactions.txt", "w") as f:
        f.write(aggregate_string)

def net_sales():
    aggregate_transactions = aggregate()

    net = 0
    for transaction in aggregate_transactions:
        net += transaction[-1]
    
    print(net)

if __name__ == "__main__":
    net_sales()
