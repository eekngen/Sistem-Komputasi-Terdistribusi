import zerorpc

# list pulsa yang ditawarkan
itemTag = (10000, 20000, 50000, 100000, 2500000, 1000000)

# set debit customer
debit = 200000

# menu
def print_menu():
    print(
        "===================================\n"
        "\t\tMENU\n"
        "==================================="
    )
    for idx, val in enumerate(itemTag):
        print(idx+1, " - Pulsa Rp ", val, ",-\n", sep="")
    print(
        len(itemTag)+1, " - Exit\n"
        "===================================\n",
        "Enter a choice and press enter: ", sep= "")

try:
    # binding to server
    customer= zerorpc.Client()
    customer.bind("tcp://127.0.1.1:3344")
    # cek koneksi server
    print(customer.test())
    print_menu()
    cInput = int(input(""))
    print(customer.getInput(cInput, debit))
except KeyboardInterrupt:
    print("Closing Client")