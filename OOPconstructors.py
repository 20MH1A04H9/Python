class Car:
    def __init__(self,Name):
         self._Name=Name
    def GetOwner(self):
        print("Owner is ",self._Name)




def main():
    mycar=Car("Mouli")
    mycar.GetOwner()
    car1=Car("Vicky")
    car1.GetOwner()



if __name__ == '__main__':main()