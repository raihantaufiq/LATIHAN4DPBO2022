class Job:

    def __init__(self, nip, companyName, position):
    #konstruktor
        self.__nip = nip
        self.__companyName = companyName
        self.__position = position

    #set
    def setNIP(self, nip):
        self.__nip = nip

    def setCompanyName(self, companyName):
        self.__companyName = companyName

    def setPosition(self, position):
        self.__position = position

    #get
    def getNIP(self):
        return self.__nip

    def getCompanyName(self):
        return self.__companyName

    def getPosition(self):
        return self.__position

    #methods
    def showDetail(self):
        print("NIP : " + self.getNIP())
        print("Company Name : " + self.getCompanyName())
        print("Position : " + self.getPosition())
