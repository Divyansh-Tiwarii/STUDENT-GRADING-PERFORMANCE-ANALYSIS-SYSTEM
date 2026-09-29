from config import PASS_MARK, GRADE_SCALE

def validate_marks(marks):
    if len(marks) != 3:
        raise ValueError('Exactly three subject marks are required.')
    if any(m < 0 or m > 100 for m in marks):
        raise ValueError('Marks must be between 0 and 100.')

def calculate_total(marks):
    validate_marks(marks); return sum(marks)

def calculate_average(marks):
    return calculate_total(marks) / 3

def result_status(marks):
    validate_marks(marks); return 'PASS' if all(m >= PASS_MARK for m in marks) else 'FAIL'

def grade_from_average(average):
    for minimum, grade, point in GRADE_SCALE:
        if average >= minimum: return grade, point
    return 'F', 0

def student_result(marks):
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade, point = grade_from_average(average)
    return {'total': total, 'average': round(average,2), 'result': result_status(marks), 'grade': grade, 'grade_point': point}
