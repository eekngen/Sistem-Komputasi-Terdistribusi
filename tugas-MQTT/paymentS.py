import zerorpc


def getTran(harga, debit):
    pay = debit - harga
    if pay > -1:
        return "Transaksi Berhasil\nSisal Saldo:  %s" % pay
    else:
        return "Transaksi Gagal\nSaldo yang anda miliki kurang untuk melakukan transaksi ini"

# binding ip and port to become a server
class TestingRPC(object):
    def test(self, arg):
        return "%s YESS" % (arg)
    def getTrans(self, harga, debit):
        return "%s" % getTran(harga, debit)

try:
    paymentServer = zerorpc.Server(TestingRPC())
    paymentServer.bind("tcp://127.1.0.1:3344")
    paymentServer.run()

# interrupt hendler
except KeyboardInterrupt:
    print("Closing Server")