from pydantic import BaseModel,EmailStr,Field
from typing import Optional

# class Student(BaseModel):
#     name:str

# new_student={'name':'bella'}

# student=Student(**new_student)

# print(student)



#IF SETTING THE DEFAULT VALUES
# class Student(BaseModel):
#     name:str ='nitish'

# new_student={}

# student=Student(**new_student)
# print(student)




#IF SETTING THE OPTIONAL VALUES:
class Student(BaseModel):
    name:str
    age:Optional[int]=None

new_student={'name':'bella',
             'age':24}

student=Student(**new_student)
print(student)


#TYPE COERCING
# class Student(BaseModel):
#     name:str
#     age:Optional[int]=None

# new_student={'name':'bella',
#              'age':'24'}

# student=Student(**new_student)
# print(student)


#EMAIL
# class Student(BaseModel):
#     name:str
#     age:Optional[int]=None
#     email:EmailStr

# new_student={'name':'bella',
#              'age':'24',
#              'email':'avc@gmail.com'}


# student=Student(**new_student)
# print(student)


# #FIELD
# class Student(BaseModel):
#     name:str
#     age:Optional[int]=None
#     email:EmailStr
#     cgpa:float=Field(gt=0, lt=10,default=5,description="Decimal value representing the cgpa of the student")

# new_student={'name':'bella',
#              'age':'24',
#              'email':'avc@gmail.com',
#              'cgpa':12}   #this will give an error


# student=Student(**new_student)
# print(student)



class Student(BaseModel):
    name:str
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0, lt=10,default=5,description="Decimal value representing the cgpa of the student")

new_student={'name':'bella',
             'age':'24',
             'email':'avc@gmail.com',
            }   


student=Student(**new_student)


student_dict= dict(student)
print(student_dict['age'])

student_json=student.model_dump_json()
print(student_json)