from pydantic import BaseModel, EmailStr,Field
from typing import Optional


class Student(BaseModel):
    name: str = 'arvind'
    age: Optional[int] = None
    email: EmailStr
    cgpa: Optional[float] = Field(None, ge=0.0, le=10.0, description="CGPA must be between 0.0 and 10.0")

# new_student = Student(**{"name": "Alice", "age": 20})
new_student = {'age': '20','email' :'abc@gmail.com'}

student = Student(**new_student)

dict_student = dict(student)

print(dict_student)
print(dict_student['age'])