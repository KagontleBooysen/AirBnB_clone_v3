#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()  # returns the dictionary __objects
# ex: {'BaseModel.12121212': <BaseModel object>}
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_1_Model"
my_model.my_number = 89
my_model.bool = True
my_model.save()  # calls save() method of FileStorage
# it damps to json file in the following way:

print(my_model)  # prints the string representation of my_model as follows:


print("--------------------------------")
# print(my_model.id)
