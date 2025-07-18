from pydantic import BaseModel


class Employee(BaseModel):
    first_name: str
    last_name: str
    employee_id: str

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
