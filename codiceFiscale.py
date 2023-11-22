#import of modules 'comuni' and 'stati' to search the code of the city or of the state
import comuni
import stati

class FiscalCode():

    #constructor    
    def __init__(self, name, surname, birthdate, birthcity, sex):
        self.__name=name
        self.__surname=surname
        self.__birthdate=birthdate
        self.__birthcity=birthcity
        self.__sex=sex
        #array for the vowels
        self.__vowels=['a','e','i','o','u','A','E','I','O','U']
    
    #function to verify if the character is a vowel
    def isVowel(self, x):
        if self.__vowels.index(x) > -1 : return 1
        else: return 0
    
    #function to count the consonants
    def countConsonants(self, x):
        c=0
        for s in x:
            if s not in self.__vowels: c+=1
        return c

    #function to determine the 3 characters of the surname
    def extractSurname(self):
        s = self.__surname
        b = ""
        c = 1
        for x in s:  
            if(x in self.__vowels) == 0 and c<=3:
                c+=1
                b+=x
        if(c<=3):
            for x in s:
                if(x in self.__vowels) == 1 and c<=3:
                    b+=x
                    c+=1
        if(c<=3): b+="x"
        return b.upper()
    
    #function to determine the 3 characters of the name
    def extractName(self):
        s = self.__name
        b = ""
        c = 1
        k = self.countConsonants(s) 
        for x in s:  
            if(x in self.__vowels) == 0 and c<=4: 
                if(k>=4):
                    if(c==1 or c==3 or c==4):
                        b+=x 
                else:
                    b+=x 
                c+=1
        if(c<=3):
            for x in s:
                if(x in self.__vowels) == 1 and c<=3:
                    b+=x
                    c+=1
        if(c<=3): b+="x"
        return b.upper()
    
    #function to determine the 2 digits of birth year, the letter of the birth month and the 2 digits of the birth day
    def extractBirthdate(self):
        bd=self.__birthdate
        sp=bd.split("/") 
        day=sp[0]
        month=self.findMonthLetter(sp[1])
        year=sp[2][2:]
        if(self.__sex=="F"): day=int(day)+40
        day=str(day)
        return str(year+""+month+""+day)

    #function to determine the city code - it calls the array in 'stati' module or the array in 'comuni' module
    def extractBirthcity(self):
        v=0
        for a in comuni.comuniList: 
            if a["nome"] == self.__birthcity:
                v=1
                return a["codiceCatastale"]
                break 
        if(v==0):
            return stati.states[self.__birthcity]["code"]
    
    #function to determin the birth month letter
    def findMonthLetter(self,month):
        arr={
            '01': 'A',	
            '02': 'B',
            '03': 'C',
            '04': 'D',
            '05': 'E',
            '06': 'H',
            '07': 'L',
            '08': 'M',
            '09': 'P',
            '10': 'R',
            '11': 'S',
            '12': 'T'
        }
        return arr[month]

    #function to convert the character in even positions
    def conversionEven(self,c): 
        arr={
            'A':0,
            '0':0,
            'B':1,
            '1':1,
            'C':2,
            '2':2,
            'D':3,
            '3':3,
            'E':4,
            '4':4,
            'F':5,
            '5':5,
            'G':6,
            '6':6,
            'H':7,
            '7':7,
            'I':8,
            '8':8,
            'J':9,
            '9':9,
            'K':10,
            'L':11,
            'M':12,
            'N':13,
            'O':14,
            'P':15,
            'Q':16,
            'R':17,
            'S':18,
            'T':19,
            'U':20,
            'V':21,
            'W':22,
            'X':23,
            'Y':24,
            'Z':25
        } 
        return arr[c]
    
    #function to convert the character in odd positions
    def conversionOdd(self,c): 
        arr={
            'A':1,
            '0':1,
            'B':0,
            '1':0,
            'C':5,
            '2':5,
            'D':7,
            '3':7,
            'E':9,
            '4':9,
            'F':13,
            '5':13,
            'G':15,
            '6':15,
            'H':17,
            '7':17,
            'I':19,
            '8':19,
            'J':21,
            '9':21,
            'K':2,
            'L':4,
            'M':18,
            'N':20,
            'O':11,
            'P':3,
            'Q':6,
            'R':8,
            'S':12,
            'T':14,
            'U':16,
            'V':10,
            'W':22,
            'X':25,
            'Y':24,
            'Z':23
        } 
        return arr[c]

    #function to do the sum of the relative numbers derivated by conversions (even and odd positions)
    def conversion(self):
        i=1
        total=0
        build=self.extractSurname()+self.extractName()+self.extractBirthdate()+self.extractBirthcity()
        for a in build: 
            if (i) % 2 == 0:
                c=self.conversionEven(a) 
            if (i) % 2 == 1:
                c=self.conversionOdd(a) 
            i+=1
            total+=c 
        return total  

    #function to compute the last character of the fiscal code
    def checkDigit(self):
        k = self.conversion()
        m = k % 26 
        arr=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        return arr[m]  

    #function to determine the final ouput
    def theOutput(self):
        return self.extractSurname()+self.extractName()+self.extractBirthdate()+self.extractBirthcity()+self.checkDigit()

#EXAMPLES
fc=FiscalCode("Maria","Verdi","12/12/1991","Milano","F")
print(fc.theOutput()) 
fc2=FiscalCode("Mario","Rossi","10/10/1990","Roma","M")
print(fc2.theOutput()) 
fc3=FiscalCode("Marcella","Bianchi","10/10/1990","ALBANIA","F")
print(fc3.theOutput()) 
fc4=FiscalCode("Andrea","Amigos","10/10/1980","SPAGNA","M")
print(fc4.theOutput()) 