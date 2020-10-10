import Liblary

if __name__ == "__main__":
    user = Liblary.LIbrary()
    new = "sameer"

    user.add_user(new)
    user.display()
    user.lend_book("Rich dad, Poor dad", "sameer")
    print(user.lib_users)
    user.display()
    
