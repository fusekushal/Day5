"""Pydantic is the most widely used data validation library for Python.Data validation is the process of ensuring that data meets certain criteria or constraints in order to be considered accurate, consistent, and useful. It's like checking whether the information you receive or work with makes sense and fits within the expected boundaries.
In the context of software development, including web applications and APIs like those created with FastAPI, data validation is crucial to ensure that the data input by users or received from external sources is valid and safe for further processing. Data validation helps prevent errors, vulnerabilities, and unexpected behavior in your application.
 """
from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    department: str
