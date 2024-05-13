class Car:
    def GetOwner(self):
        print("Owner is ",self._Name)
    def SetOwner(self,Name):
        self._Name=Name



def main():
    mycar=Car()
    mycar.SetOwner("Vicky")
    mycar.GetOwner()
    masicar=Car()
    masicar.SetOwner("Ramya")
    masicar.GetOwner()



if __name__ == '__main__':main()