from SOLID.SRP.goodEx.user import User

class UserRepo:
    def __init__(self, db, user, password):
        self.db = db
        self.user = user
        self.password = password
        
    def save_to_database(self, user:User):
        print(f"{user.name}  is getting save to db")
        
    def delete_from_database(self, user:User):
            print(f"{user.name}  is getting delete to db")