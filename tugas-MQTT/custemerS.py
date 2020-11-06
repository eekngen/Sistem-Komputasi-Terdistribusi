import zerorpc
import paho.mqtt.client as mqtt

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

def on_connect(client, userdata, flag, rc):
    print("Connected with result code "+str(rc))

def printTrans(client, obj, msg):
    print(msg.payload)


# binding to RPC server
customer= zerorpc.Client()

# connect to mqtt broker 
customerM = mqtt.Client(client_id="custommerS", clean_session= False)
customerM.connect("127.0.0.1", port= 1883)

# daftar callback function
customerM.on_connect= on_connect
customerM.on_message= printTrans

try:
    # connect to RPC server
    customer.bind("tcp://127.0.1.1:3344")
    
    # subcribe to MQTT publisher
    customerM.subscribe("/seller/print", qos=1)

    # cek koneksi server RPC
    print(customer.test())
    
    #print menu
    print_menu()
    
    #get user input
    cInput = int(input(""))

    # print hasil transaksi menggunakan protokol RCPC
    # print(customer.getInput(cInput, debit))

    #print hasl transaksi menggunakan protokol MQTT
    
except KeyboardInterrupt:
    print("Closing Client")