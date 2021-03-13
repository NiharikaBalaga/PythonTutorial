import pandas as pd


class RailwayForm:
    formType = "RailwayForm"

    def printData(self, age):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
        print(age)


harrysApplication = RailwayForm()
harrysApplication.name = "Harry"
harrysApplication.train = "Rajdhani Express"
# harrysApplication.printData()
harrysApplication.printData(23)

harrysApplication.name = "Dinesh"
harrysApplication.train = "Chennai Express"
harrysApplication.printData(20)
