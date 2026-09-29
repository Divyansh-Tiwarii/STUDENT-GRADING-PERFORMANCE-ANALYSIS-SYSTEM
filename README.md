# Grading & Performance Analysis of Students

## Background
This program is an enhanced, more organized and well structured program from the existing student's program on three subjects' grades.

## Program features
- Student registration number and name
- Three subjects marks entry
- Sum, total and average
- Pass/Fail based on 50 marks for each subject
- Grade and grade point
- Search, update and deletion of students
- Class table and ranking
- Maximum pass/ fail subjects analysis
- Students failing in exactly one subject
- Students failing in two or more subjects
- Students scoring 100 in exactly two subjects
- Permanent data storage using SQLite
- Input validation
- Unit testing

## Running the code
Use Python 3.10+

```bash
python main.py
```

Testing code:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

HTML, CSS and JavaScript is not used in this application.

## Original code logic maintained
Original program computed sum, average and pass/fail along with performance analysis of subjects and special case. In this program above calculations are converted to modules and database handling, CRUD and grading is added.