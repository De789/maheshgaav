# Belongs to the class, not an instance.
# First argument is cls.
# Can access or modify class-level state.
# Marked with @classmethod.

class Company():
    emp="mahesh"
    
    @classmethod
    def change_name(cls,new_name):
        # cls.emp=new_name
        print(f"new name is {new_name}")

Company.change_name("Sagar")
Company.change_name("map")

