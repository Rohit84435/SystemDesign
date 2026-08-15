class User:
    def __init__(self,name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
    def get_user_info(self):
        print(f"This is {self.name} and my age is {self.age}")

    
    def is_adult(self)->bool:
        return self.age > 18
    
    def save_to_db(self):
        print(f"{self.name} is getting save to db")
    
    def delete_user_to_db(self):
            print(f"{self.name} is getting deleted from db")