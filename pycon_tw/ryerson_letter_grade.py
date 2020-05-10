TABLE = (
    (90, 'A+'),
    (85, 'A'),
    (80, 'A-'),
    (77, 'B+'),
    (73, 'B'),
    (70, 'B-'),
    (67, 'C+'),
    (63, 'C'),
    (60, 'C-'),
    (57, 'D+'),
    (53, 'D'),
    (50, 'D-')
)

def ryerson_letter_grade(pct: int) -> str:
    result = 'F'
    for lower, grade in TABLE:
        if pct >= lower:
            result = grade
            break
    return result