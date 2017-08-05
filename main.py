import fileinput


class Addressbook:
    def __init__(self, Name="", Number="", Address=""):
        self._Name = Name
        self.Number = Number
        self.Address = Address

    def GetName(self):
        return (self._Name)

    def GetNumber(self):
        return (self.Number)

    def GetAddress(self):
        return (self.Address)

    def NewAddressbook(self, name, number, address):

        out = open("testfile.txt", "a")
        out.write(name + "@")
        out.write(number + "@")
        out.write(address + "\n")

        out.close()

    def UpdateAddressbook(self, OldStr, NewStr):
        for line in fileinput.input('testfile.txt', inplace=True):
            print(line.rstrip().replace(OldStr, NewStr))

    def DisplayAll(self):
        readFile = open("testfile.txt", "r")

        lines = readFile.readlines()

        details = [str(e.strip()) for e in lines]

        for i in range(0, len(details)):
            str_obj = details[i]
            data = str_obj.split("@")

            print(str(i) + " ) Name: " + data[0] + " Number: " + data[1] + " Address: " + data[2])
        readFile.close()

    def DeleteOnIndex(self, Number):
        readFile = open("testfile.txt", "r")

        lines = readFile.readlines()

        details = [str(e.strip()) for e in lines]

        del details[int(Number)]  # delete regarding element

        # rewrite the textfile from list contents/elements:
        with open("testfile.txt", "w") as textobj:
            for n in details:
                textobj.write(n + "\n")


def main():
    while (True):
        print("1) Add Address")
        print("2) Display All Addresses")
        choice = input("Enter Number of choice : ")
        address_Obj = Addressbook()
        if (int(choice) == 1):
            while (True):
                name = input("Enter New Name: ")
                number = input("Enter New Number: ")
                address = input("Enter New Address: ")
                address_Obj.NewAddressbook(name, number, address)
                char_choice = input("If Do you want to add again (y/n)? : ")
                if (str(char_choice) == "n"):
                    break

        elif (int(choice) == 2):
            while (True):
                address_Obj.DisplayAll()

                Number = input("Enter number to update it : ")

                name = input("Enter New Name: ")
                number = input("Enter New Number: ")
                address = input("Enter New Address: ")

                newstr = name + "@" + number + "@" + address
                readFile = open("testfile.txt", "r")
                lines = readFile.readlines()
                details = [str(e.strip()) for e in lines]
                oldstr = details[int(Number)]
                readFile.close()

                address_Obj.UpdateAddressbook(oldstr, newstr)

                char_choice = input("If Do you want to display again (y/n)? : ")
                if (str(char_choice) == "n"):
                    break

        char_choice = input("If Do you want to select again (y/n)? : ")
        if (str(char_choice) == "n"):
            break


if __name__ == '__main__': main()
