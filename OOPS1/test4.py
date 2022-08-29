class Person:

    def age(self, current_year , year_of_birth):
        return current_year - year_of_birth

    def email_id_input(self, email_id ):
        print("take an mail id from a person and print it " , email_id)

    def ask_name(self):
        name = input("tell me your name")
        return name

    def ask_dob(self):
        dob = input("tell me your date of birth")
        return dob

sudh = Person()
anuj = Person()
gargi = Person()
hitesh = Person()
krish = Person()

sudh.email_id_input("sudhanshu@ineuron.ai")
sudh.ask_name()

print(hitesh.ask_dob())
