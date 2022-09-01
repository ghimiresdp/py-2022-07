"""
Visualize this hierarchy in an OOP approach
school
    - classroom
        - grade: int
        - board
            - dimension: tuple(float, float)
            - color [white/black]: str
        - desks: int
        - windows: int
        - chairs: int
    - teacher
        - name
        - subject
            - complexity
            - scope
        - time
    - student
        - roll
        - name
        - majors
            - subject 1
            - subject 2
"""

class Board:
    """
    The board class can save the board details. Example:
    - Black board with 10 X 8 Feet dimension
    """
    dimension: tuple
    color: str

    def __init__(self, dimension: tuple, color: str) -> None:
        self.dimension = dimension
        self.color = color




class School:
    pass
