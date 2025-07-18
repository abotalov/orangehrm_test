import factory

from common.models import Employee


class EmployeeFactory(factory.Factory):
    class Meta:
        model = Employee

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    employee_id = factory.Faker("bothify", text="??????????")
