
class Car:
    def __init__(self,**kwargs):
         self.Data=kwargs
    def GetOwner(self):
        print("Owner Name ",self.Data["Name"])
        print("Car Model ",self.Data["Model"])
        print("Year ",self.Data["Year"])
    def Set_Model(self,Model):
        self.Data["Model"]=Model
    def Get_Model(self):
        print("Car Model ",self.Data["Model"])




def main():
    mycar=Car(Name="Mouli",Model="camer 2018",Year=2015)
    mycar.GetOwner()
    nanocar =Car(Name="Masi",Model="sony x",Year=2023)
    nanocar.GetOwner()
    #jen model set
    nanocar.Set_Model("2016")
    nanocar.Get_Model()



if __name__ == '__main__':main()