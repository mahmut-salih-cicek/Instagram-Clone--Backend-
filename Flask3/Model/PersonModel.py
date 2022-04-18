



class PersonModel:

    email = ""
    realName = ""
    password = ""
    userName = ""

    def __init__(self,email,realname,password,userName):
        self.email = email
        self.realName = realname
        self.password = password
        self.userName = userName