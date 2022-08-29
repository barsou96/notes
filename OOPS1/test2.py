class Person :

    def __init__(sudh,name,surname , emailid, year_of_birth):
        sudh.name1 = name
        sudh.surname = surname
        sudh.emailid = emailid
        sudh.year_of_birth = year_of_birth

    def age(sudh , current_year ):
        return current_year - sudh.year_of_birth

anuj_var  = Person("anuj" , "bhandari" , "anuj@gmail.com" , 1994)
sudh = Person("sudhanshu " , "kumar" , "sudhanshu@gmail.com" , 2344)
gargi = Person("gargi" , "xyz" , "gargi@gmail.com" , 2342)
print(anuj_var.name1)
print(sudh.name1)
print(sudh.name1 + sudh.surname)
print(gargi.surname)
print(sudh.emailid)
print(type(sudh))
print(sudh.age(2022))
print(anuj_var.age(2022))
