import time


class Pupil():
    
    def __init__(self,Surname,Name,Mark):
        self.Surname = Surname
        self.Neme = Name
        self.Mark = Mark

Pupils=[]

def print_class(pupils):
    for pupil in pupils:
        print(pupil.Surname,pupil.Name,"-",pupil.Mark )
    print("\n")

with open("puplis.txt","r",encoding = "utf-8") as file:
    for line in file:
        data = line.split(" ")
        Pupils = Pupil(data[0], data[1], int(data[2]))
        Pupils.append(Pupil)

print_class(Pupils)