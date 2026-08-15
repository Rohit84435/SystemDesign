from SOLID.SRP.goodEx.user import User
from SOLID.SRP.goodEx.userRepository import UserRepo

user_obj = User("Rohit kumar", 25, "rohit23@gmail.com")
userRep = UserRepo("admin","root", "zusdf")

user_obj.get_user_info()

userRep.save_to_database(user_obj)