from Job import Job

class Person:

    def __init__(self, nik, name, gender, job):
    #konstruktor
        self.__nik = nik
        self.__name = name
        self.__gender = gender
        self.__job = job

    #set
    def setNIK(self, nik):
        self.__nik = nik

    def setName(self, name):
        self.__name = name

    def setGender(self, gender):
        self.__gender = gender

    def setJob(self, job):
        self.__job = job

    #get
    def getNIK(self):
        return self.__nik

    def getName(self):
        return self.__name

    def getGender(self):
        return self.__gender

    def getJob(self):
        return self.__job

    #methods
    def sleep(self):
        print(self.getName() + " is sleeping...")

    def showDetail(self):
        print("NIK : " + self.getNIK())
        print("Name : " + self.getName())
        if self.getGender():#TRUE=Male, False=Female
            print("Gender : Male")
        else:
            print("Gender : Female")
        print("----- Job Info -----")
        self.__job.showDetail()

