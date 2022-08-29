class Person :

    def __init__(self,name,surname , emailid, year_of_birth):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth

anuj_var  = Person("anuj" , "bhandari" , "anuj@gmail.com" , 1994)
sudh = Person("sudhanshu" , "kumar" , "sudhanshu@gmail.com" , 2344)
gargi = Person("gargi" , "xyz" , "gargi@gmail.com" , 2342)
print(anuj_var.name)
print(gargi.surname)
print(sudh.emailid)
print(type(sudh))