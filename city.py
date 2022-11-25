#Author:Chipo
#Date:11/1/2022
#Purpose:Lab 3

class City:
    def __init__(self,code,name,region,popul,latitude,longitude):
        self.code=code
        self.name=name
        self.region=region
        self.popul=popul
        self.latitude=latitude
        self.longitude=longitude

    def __str__(self):
        return str(self.name)+","+str(self.popul)+","+str(self.latitude)+","+str(self.longitude)