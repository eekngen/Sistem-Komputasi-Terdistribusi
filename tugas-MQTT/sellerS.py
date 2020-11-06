import zerorpc

# harga pulsa
itemTag = (12000, 22000, 51000, 100000, 2500000, 1000000)

# mebuat dictionary dari tuple itemTag
def menuS(arg):
    menu = {}
    for idx, val in enumerate(itemTag):        
        menu[idx+1] = val
    return menu.get(arg, "Input salah")
 
class TestSellerServer(object):
    def test(self):
        return "YEP"
    def getInput(self, arg, debit):
        if menuS(arg) == "Input salah":
            return menuS(arg)
        else:
            sellerClient = zerorpc.Client("tcp://127.1.0.1:3344")
            return sellerClient.getTrans(menuS(arg), debit)
        
try:
    # as server
    sellerServer = zerorpc.Server(TestSellerServer())
    # binding ip and port for custemerS.py connection
    sellerServer.connect("tcp://127.0.1.1:3344")
    sellerServer.run()

except KeyboardInterrupt:
    print("Closing Server")