# NOTE EVERYTHING IS CASE SENNSITIVE
x= ("Hello") #text can be written inside ""
y= ('''i am under the wottar
please help me, here too much raining 
udududududu''') # ''' can be also used to write paragraphs
z=(12435345)   #we used integer here
a=(8737) 
print(x,y,z/a)  # , gives a space, + do not provide space but just combines two things, / divides integers and other normal maths calc
print(type(x)) #  we get to know the type of x, whether its string, integer, float i.e. decimal, boolean means (true or false), none text ko none type 
#float means decimal, string means text
print(type(z)) # no NAME can start with a number like 1Joe, also small and capital letters are different like a and A
print("the value of 125+569 is", 125+569)
a += 1000 # += se a ki jo bhi integer value hai isme add kar sakte  hai += ke aage wala number, in this case its 1000, same way -=, *=, /=
print (a)
b=(14>7) #>< ya => =< se hum question pooch sakte hai ki konsa bada hai konsa chota, wo print hoga ki true hai ki 14 >7 and vice versa
print(b) # == means ki agar x=x where x is any integer then true print hoga else nope, not equal means !=

#YOU CAN TYPE 'PTHON' in terminal to do calculations, print something or things which are not very necessary


print("########################################################################################################################################################################1")
bool1=  True
bool2= False
print("agar bool1 aur bool2 me and lagaya to agar dono true to true else false---", (bool1 and bool2))
print("agar or aa gaya to dono me se ek true to true else false---", (bool1 or bool2))
print("agar not aa gaya aur phir koi ek select kiya bool1 ya bool2, to uske andar ki value ka ulta print hoga, like false ka true and vice versa---", (not bool2))
print("########################################################################################################################################################################2")
c= "1234" #yeh jo cheez hai wo "" ke andar hhai so its not an integer but it is considered as a text which cant be used for calculations
c= int(c) #this will consider c as integer
print (c+5)
print(type(c))
#same if we want decimal then instead of int add float
print("########################################################################################################################################################################3")
d= "123.45"
d= float(c)
print(type(d))
a1 = input ("The name of the person who got rejected from art school") #input function se aap question pooch sakte ho, 
#phir terminal me uska answer type karo uske baad hi aage ka code kaam karega
print(a1) #jo output aayega to bhale hi number ho but it will be considered as string, although uska type change kar sakte hai, jaise upar float/integer kiya hai string ko
#agar average nikalna hai to normal maths wala formula lagana hai iska koi code nahi hota
print("########################################################################################################################################################################4")
e= input("e ki value daalo for average") #note yeh abhi strong me haiinko integer me convert karo phir run karo
f= input("f ki value daalo for average")
e= int(e)
f= int(f)
avg= (e+f)/2
print ("the avg of e and f is", avg)
print("########################################################################################################################################################################5")
print ("the remainder of 14/7 is", 14%7) #this will give remainder and not the whole divide
g= c+d
print (g) #yeh bhi valid hota hai
g= "Jassi"
print(g[0]) #Jassi me J=0, a=1 and so on, iss code se 0 position i.e. J print hoga
print(g[4])
print(g[0:4]) #isse 0 se 3 (NOT 4) tak ke alphabets print honge
print(g[:4]) #isse : ke pehle 0 consider kiya jaayega
print([g]) #isse : ke baad last string consider kiya jaayega, in  this case its i of Jassi
print(g[2:4])
print(g[-1]) #this will give the last character of any string, -1 stands for i in Jassi and -5 for J
print(g[-4:-1]) #is same as [1:4]
print(g[1:3:5]) #this will only give words that are at 1 3 and 5 position
print(g[0::2]) #by this 0th term and terms which are in multiple of 2 will be printed
print("########################################################################################################################################################################6")
h= ("pablo Escobar was a criminal  with amazing life story")
print(len(h)) #this will print the number of characters or we can say will tll the length of the line g
print(h.endswith("Drug dealer")) #yeh batayega ki jo end line hai wo ISS LINE ME LIKHE WORD SE MILTI HAI YA NAHI, if nnot then it will show false
print(h.endswith("story")) #this will be printed as true
print(h.count("o")) #this will tell the number of o or any character you put, ki uss line me aise kitne words hai
print(h.count("amazing")) #we can count words too
print(h.capitalize()) #this will capitalize the first letter of the whole sentence
print(h.find("amazing")) #yeh batayega ki wo word uss sentence me hai ya nahi, if yes then at what position (SIRF FIRST LETTTER KI OCCURENCE/POSITION KE BATAYEGA), if no then -1 will be shown
print(h.find("Vladimir Lenin")) #it will show -1 as it is not there in the sentence
print(h.find("  ")) # we can find space too
print(h.replace("Escobar", "El Gavirio Escobar")) #yeh replace karega ek word ko doosre se
print("########################################################################################################################################################################7")
i= "Line 1 \n Line 2" #\n will make a new line
print(i)
j="Line 1 \t line 2" #this will give a tab (arre wo bada wala space jo tab dabane se aata hai)
print(j)
k= "Mein Kamph is a \' book on life of hitler" #this will give single quote i.e '
l="Line 1 \\ Line 2" #this will give one \
print("########################################################################################################################################################################8")
m= [1,2,3,4]
print(m[0]) #it will print 1 ie the 0th digit
print(m[1]) #it will give  2
m[0]=100 # humne let kiya ki 0th term 100 hai
print(m[0])
n=[45 , "Hiroshima", "Nagasaki", "Robert J.", True] #it is also valid
o= [2,5,1,20,12,15]
print(o)
o.sort() #it will arrange it  in ascending order
print(o)
o.reverse() #it will reverse the table
print(o)
o.append(2) #it will PUT 2 at the last digit OF SORTED TABLE
print(o)
o.insert(2,5) # it will PUT 5 AT 2nd DIGIT OF SORTED TABLE
print(o)
o.pop(2) #it will remove the 2nd index and tell the number being removed, wo latest print hue hue table se remove hota hai, in this case insert(2,5) se 2nd digit i.e. 5 hata hai
print(o) 
o.remove(20) #it will remove 20 from list
print(o)
o.clear() #this will empty the set
print(o)
#o.union({2,5}) UNDERSTAND THIS and BELOW GREEN PART
#print(o)
#o.intersection({2,5})
#print(o)
print("########################################################################################################################################################################9")
p=(6,5,4,3,3,2,1)
p=() #this is a tuple, it cant be changed as above '[]' wala
print(p)
p=(6) #this is invalid tuple
print(p)
p=(6,) #this is valid tuple
print(p)
p=(5,3,3,1) #multiple elements of a tuple
print(p)
print(p.count(3)) #it will count number of 3s in the table
print(p.index(3)) #it will tell the first occurence of the number you chose, here its 3, it wont tell the position or number of occurence
print("########################################################################################################################################################################10")
q1 =input("world leaders, No. 1 :-")
q2= input("world leaders, No. 2 :-")
q3=input("world leaders, No. 3 :-")
q4=input("world leaders, No. 4 :-")
q5=input("world leaders, No. 5 :-")
q= [q1,q2,q3,q4,q5] #if entering any number and want it to be proicessed then you need to make them an integer before processing
print(q)
print("########################################################################################################################################################################11")
dictionary= { "Father of atomic bomb": "Robert J. Oppenheimer" ,  #by this we can make a dictionary or word and meaning code
             "biggest stock market scammer in india" : "harshad Mehta" , #remember to put : and , in and after every definition
             "Cricket scores" : [100,200,300], #we can use numbers too
            "dictionary2": {'greatest boxer': 'Muhammed Ali'} #we can add dictionary inside a present dictionary
             }
print(dictionary['Father of atomic bomb']) 
print(dictionary['Cricket scores'])
print(dictionary['dictionary2']['greatest boxer']) #this needs to be crammed on how to retrieve date from a dictionary present inside another dictionary
dictionary['Cricket scores'] = [50,100,150] # we can edit the data of dictionary
print(dictionary['Cricket scores'])
dictionary.items() #ASK THIS
dictionary.keys() #ASK THIS
print("########################################################################################################################################################################12")
book= {"Pankha": "Fan",
       "Dabba": "Box"}
print("You can ask teh meaning of the following words", book.keys())
r=input("Enter the hindi word \n")
print("the meaning of your word is", book[r])
print("########################################################################################################################################################################13")
s = input("Enter the number-")
s =int(s)
if(s > 10): #these are if elif and else statement
    print("The number you entered is greater than 10")
elif(s<10): #there can be many elif
    print("The number you entered is less than 10")
elif(s<0):
    print("The number you entered is less than 0 i.e. in negative")
else:
    print("The number you entered is equal to 10")
print("########################################################################################################################################################################14")
t= int(input("Enter your age-"))
if(t>30 and t<14): #dono condition must satisfy
    print("You cant work with us")
elif (t>0):
    print("You need atleast 10 years of experience")
elif(t==30 or t==14):  #== to satisfy one =, same for >= and <=
    print("you can work with us")
else:
    print("You are hired")
print("########################################################################################################################################################################15")
u= int(input("Enter your age-"))
if(u>14 or u<30):
    print("You can work with us")
else:
    print("You cant work with us")
v= None
if (a is None): # is is also used
    print("Yes")
else:
    print("No")
print("########################################################################################################################################################################16")
w= [1,2,3,4,5] 
print(2 in w) #there is 2 in 2 so it will print true
print(9 in w) #it will give false
print("########################################################################################################################################################################17")
#A-Z we used all alphabets so below this there will be a2 (NOT A1 AS IT  IS USED)... a100 then b1, b2...b100
a2= int(input("enter the 1st number"))
a3= int(input("Enter 2nd number"))
a4=int(input("enter 3rd number"))
a5=int(input("eter 4th number"))
a6=int(input("enter 5th number"))
print(max(a2,a3,a4,a5,a6)) #this will print the max number from a2 a3 a4 a5 a6
print(min(a2,a3,a4,a5,a6)) #this will print the min number from a2 a3 a4 a5 a6
print("########################################################################################################################################################################18")
a7=int(input("Enter first sub marks"))
a8=int(input("enter second sub marks"))
a9=int(input("enter third sub marks"))
if (a7<33 or a8<33 or a9<33):
    print("Bhai tu fail ho gaya drop lele ab")
elif (a7+a8+a9)/3 <40:
    print("Tu ab bhi fail hai, jaa drop le ab")
else:
    print("Pass ho gaya party de")
print("########################################################################################################################################################################19")
text= input("Enter the text to detect spam messages \n") #you can write like, "for best deals on groceries, buy now", it will detect that buy now is prese nt in the text and will report it as scam
if ("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
else:
    spam=False
if(spam):
    print("this is spam")
else:
    print("this is not spam")
print("########################################################################################################################################################################20")
#loops
#a10= 5
#while a10<10: #till the time value of i is less than 10, there will be a loop
 #   print("Yes")
a11=0
while a11 <10:
    print("Yes", str(a11)) #this will print the below line's numbers
    a11=a11+ 1 #this will add one number in a11 till it exceeds 10
a12= input("Name the person who got rejected from art school 1. Hitler 2. Stalin 3. Churchill:- ")
if a12==("Hitler"):
   print("You are correct")
else:
   print("You are not human")
fruits = ['Apple', 'banana', 'Watermelon', 'Grapes']
a13 = 0
while a13<len(fruits): #this will print the elements of fruits starting from apple
 print(fruits[a13])
 a13=a13+1 #this will make a list of all fruits
 if a13== 2:
   break #it is used to stop any loop at any particular time like when we reach banana then loop must break
print("########################################################################################################################################################################21")
fruits = ['Apple', 'banana', 'Watermelon', 'Grapes']
a13 = 0
while a13<len(fruits): #this will print the elements of fruits starting from apple
 a13=a13+1 #this will make a list of all fruits
 if a13== 2:
   print(fruits[a13])
   continue   #there is some other use of it, but as far as ik, continue skips the number placed at a13==, but in my case, it is printing the number to be skipped 😂
for a14 in range(10):
    if i==5:
     continue   #this will skip 5 in counting from 1 to 10
print("########################################################################################################################################################################22")
a15 = int(input("Enter any number"))
a16=int(input("Enter any number"))
if a15<=a16:
   pass   #it is when you dont want to give any output for this condition
else:
   print("this statement hasnt passed")
print("########################################################################################################################################################################23")
num= int(input("Enter number"))
for a17 in range(1,11): #range can be any, this means that from this to this the numbers will be entered in code, we can use input instead of range too, depends on question
   print(f"{num} X {a17}={num*a17}") #f means formula, {} means we can put things inside "" which will be a part of code, other than that we simply used multiplication of formula
print("########################################################################################################################################################################24")
a18=["Jaspreet", "Mayank", "Jaswinder", "Ayush"]
for name in a18: #name can be used without defining it
   if name.startswith("J"): #it helps filter names starting with J
      print("Hello", name) 
a19=["123457", "25237", "630467230"]
for name in a19:
   if name.endswith("7"):
      print("you are correct", a19, "is the number ending with 7")
print("########################################################################################################################################################################25")
#understand this code, to detect whether number entered by user is prime or not
number = int(input("Enter the number: "))
prime = True
for i in range(2, number):
   if (num%i == 0):
      prime = False
      break
if prime:
   print("This number is Prime")
else:
   print("This number is not Prime")
#learn to find factorial via this concept
print("########################################################################################################################################################################26")
#in a set [45,65,25,15,35,65], we done need to do 45+65+25..., instead we can do 
a20= [45,65,25,15,35,65]
print(sum(a20))
print("########################################################################################################################################################################27")
def greet(office_head): #def will define something
   print("Hello", office_head) #office head can be any so we just named it
office_head= input("Name the office head---")
greet(office_head)
print("########################################################################################################################################################################28")
def add(a, b):
  return a + b #return statement will calc but wont give output until print is used
print(add(3, 5))
#UNDERSTAND CHAPTER 8, FUNCTIONS AND RECURSION
print("UNDERSTAND CHAPTER 8, FUNCTIONS AND RECURSION")
print("########################################################################################################################################################################29")
def func_name(a21, a22):
   return a21+a22
no=int(input("enter 1st number"))
no1=int(input("Enter 2nd number"))
variable=func_name(no,no1)
print(variable) #+point is that if we need the sum of 100s of numbers we just need to do variable=func_name(no,no1) where no= 1st number, no1=2nd number, however, in this case
#we have used input function so we can directly input number we want
print("########################################################################################################################################################################30")
a23= "Ocygen" #we need to correct the word given
a23_new= a23.replace('c','x') #enter incorret word at first then correct word
print(a23_new)
print("########################################################################################################################################################################31")
#HOW TO FIND n!
print("########################################################################################################################################################################32")
print("I ahve made a game of stone,paper & scissors, check it out on testone file")
print("########################################################################################################################################################################33")
a24 = open('text.txt', 'r') # open will open the file which is in bracket i.e. text.txt, 'r' means the fill will be used to read, 
data = a24.read() #the file will be read here, if 'r' is not mentioned then it will take it as read i.e. 'r'
print(data) 
a24.close #WE NEED TO CLOSE THE FILE BEFORE PROCEEDING ELSE TI WILL GIVE ERROR
print("########################################################################################################################################################################34")
a25= open('text.txt', 'r')
data1= a25.read(2) #this will print the first 2 words/digits of the 'text' file
print(data1)
a25.close
print("########################################################################################################################################################################35")
a26 = open('text.txt', 'r') 
data3 = a26.readline() #this will read the first line of txt file, if you want yto make it read th end line then you have to retype this thing again BEFORE CLOSING
print(data3) 
a24.close
print("########################################################################################################################################################################36")
a27= open('NEW FILE.txt', 'w') #even if file dosent exist it will create the new file, 'w' is used to write to the file
a27.write("This is a new file which is created from JAS 1 file") #If we edit thiis then it iwll overrride the whole file to avoid this we do append
a27.close #the more times you do .write that many times it will get printed
print("########################################################################################################################################################################37")
a28= open('NEW FILE.txt', 'a')
data4 = a28.write(" \n THIS IS THE NEWLY ADDED TEXT HAHA") #The more times you run the code, it will get printed!!!
a28.close
print("########################################################################################################################################################################38")
print("+ is used to update the text in the file")
a29= open('text,txt')
a30= a29.read()
if 'file' in a30: #this is used to fina a word in other file
   print("File word is present in text.txt")
else:
   print("File word is not present in text.txt")
a29.close()
print("########################################################################################################################################################################39")
a32=["Hi", "will"] # we can do this with a single word too
with open  ("text.txt") as a31: #if we use with we need not to close the file, i just diid it for precaution
   content = a31.read()
content = content.replace(a32, "**THIS TEXT IS CHANGED**") #this will replace the word with the new word
with open ("text.txt", "w") as a31:
    a31.write(content)
    a31.close()
print("########################################################################################################################################################################40")
#Object Oriented Programming(OOP)
#FORGET EVERYTHING YOU HAVE DONE TO LEARN OOP, IT DO THE SAME THINGS BUT IN A SIMPLIFIED/ORGANISED MANNER
print("FORGET EVERYTHING YOU HAVE DONE TO LEARN OOP, IT DO THE SAME THINGS BUT IN A SIMPLIFIED/ORGANISED MANNER")
import datetime # this will be used below for knowing whether a given date is weekday or not

class Employee: #we created a class named employee, self means defining itself
    increment = 2 #ab humne kya kara hai ki, hume kisi ki salary ko 2x karna hai

    def __init__(self, fname, lname, salary): #def __init__(self) is mandatory mentioning, followed by details we need of person
        self.fname = fname #self. is reqd, fname here we defined stands for first name
        self.lname = lname #last name
        self.salary = salary

    def increase(self):
        self.salary = self.salary * Employee.increment  # this will search in employee class, we mentioned increment under employee so we must use this
 # self.salary= self.salary * self.increment # self.increment means we are searching in def __init...
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    @classmethod
    def from_string(cls, emp_str): #cls means class, emp_str means emp_str_1 and emp_str_2
        first, last, salary = emp_str.split('-') #we have to retrieve info seperated by - below
        return cls(first, last, int(salary)) #we need theese things

    @staticmethod
    def is_workday(day):
        # Monday is 0, Tuesday is 1, ..., Sunday is 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

emp_str_1 = 'Harry-Jackson-40000' #Emp1 and emp_str_1 are not related
emp_str_2 = 'Rohan-Das-40000'

Emp_1= Employee('Harry', 'Jackson', 40000) #Now we need not to do a= Harry, b= Jackson Salary=40000, but we can do this form
Emp_2= Employee('Rohan', 'Das', 40000) #same here

class Developer(Employee): #this wll take data of Employee class under the name of developer class
   increment = 3 #ab humne kya kara hai ki, hume kisi ki salary ko 3x karna hai but this will be done only for developer harry/rohan not employee harry/rohan
   def __init__(self, fname, lname, salary, prog_lang):
      super().__init__(fname, lname, salary) #super will inherit the data of fname, lname, salary from the above data, we need to now just know prog_lang
      self.prog_lang = prog_lang    
dev_1= Developer('Harry', 'Jackson', 40000, 'Python')
dev_2= Developer('Rohan', 'Das', 40000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)

class Salary:
    company = "Bharat Gas"
    salary = 5000
    salarybonus = 2000

    @property
    def totalsalary(self):
        return self.salary + self.salarybonus

    @totalsalary.setter
    def totalsalary(self, val):
        self.salarybonus = val - self.salary

a33= Salary() #we just used it to tell that a33 is salary class

a33.totalsalary= 6000 #we set total salary as 6000, now as per .setter, it will calc how much bonus was given

print(a33.salarybonus)

print(a33.totalsalary) #now we printed total salary of salary class

print(Emp_1.fullname()) #by this  we just need to mention Emp1 or Emp2 to get the name

print(Emp_1.fname, Emp_2.fname) #Emp_1 is Emp_1 defined in 2nd last line, fname refers to the data we input in __init__(self,fname...)

print(Emp_1.salary) #salary before increment

Emp_1.increase() #we increaseed salary here

print(Emp_1.salary) #this will print increaseed salary

new_emp_1 = Employee.from_string(emp_str_1)  #we just mentioned the thing which we can type to print the data we want like we do c= a+b where a and b were already defined

print(new_emp_1.salary) #this will print salary
print(emp_str_1)

print(new_emp_1.fullname()) #by this  we just need to mention Emp1 or Emp2 to get the name

print(new_emp_1.fname)  # Accessing the first name of Employee 1

print(new_emp_1.salary)  # Salary before increment

new_emp_1.increase()  # Increase salary

print(new_emp_1.salary)  # Salary after increment

my_date = datetime.date(2023, 9, 26)

print(Employee.is_workday(my_date))

#from playsound import playsound
#playsound('C:\\Users\\mayda\\Music\\Dreamer.mp3') #remember to place it at end as until the song ends the code beneath the song wont proceed