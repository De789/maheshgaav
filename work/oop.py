# Belongs to the class, not an instance.
# First argument is cls.
# Can access or modify class-level state.
# Marked with @classmethod.

# class Company():
#     emp="mahesh"
    
#     @classmethod
#     def change_name(cls,new_name):
#         # cls.emp=new_name
#         print(f"new name is {new_name}")

# Company.change_name("Sagar")
# Company.change_name("map")



class Comp:
    def __init__(self,radius):
        self._radius=radius

    @property
    def area(self):
         return 3.14 * self._radius **2
    @area.setter 
    def set_area(self,value):
        self._radius=value
c=Comp(2)
print(c.area)
c.set_area=3
print(c.area)
 