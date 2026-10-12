from dataclasses import dataclass
@dataclass(frozen=True)
class Case:
    name: str
    expected_status: int = 200

case = Case("create user", 201)
print(case.name, case.expected_status)
