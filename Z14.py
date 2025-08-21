class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"gtxfnm: {str(data)}")

    def send_data(self, data):
        if not self.send_to_pint(data):
            raise Exception("принтер не отвечает")

    def send_to_pint(self, data):
        return True

p = PrintData()
try:
    p.print("123")
except:
    print("принтер не отвечает")