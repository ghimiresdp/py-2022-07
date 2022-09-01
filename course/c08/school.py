
__all__ = [
    'FULL_TIME',
    'PART_TIME',
    'Student',
    # 'enroll'
]

FULL_TIME = 1
PART_TIME = 0


class Student:

    def __init__(self, name, roll) -> None:
        self.name = name
        self.roll = roll

    def __str__(self) -> str:
        return self.name


def enroll():
    print("Enrolled to the school")
