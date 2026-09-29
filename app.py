from database import Database
from grading import student_result
from analytics import records, class_statistics

class StudentGradingSystem:
    def __init__(self): self.db=Database()
    def read_marks(self):
        marks=[]
        for i in range(1,4):
            while True:
                try:
                    m=int(input(f'ENTER MARKS {i}: '))
                    if 0<=m<=100: marks.append(m); break
                    print('Marks must be 0-100.')
                except ValueError: print('Enter a valid integer.')
        return marks
    def add_student(self):
        try:
            reg=int(input('ENTER REG NO.: ')); name=input('ENTER STUDENT NAME: ').strip()
            if not name: raise ValueError('Name cannot be empty.')
            self.db.add(reg,name,self.read_marks()); print('Student added successfully.')
        except Exception as e: print('Error:',e)
    def update_student(self):
        try:
            reg=int(input('ENTER REG NO. TO UPDATE: ')); row=self.db.get(reg)
            if not row: print('Student not found.'); return
            name=input(f'ENTER NAME [{row["name"]}]: ').strip() or row['name']
            self.db.update(reg,name,self.read_marks()); print('Student updated successfully.')
        except Exception as e: print('Error:',e)
    def delete_student(self):
        try:
            reg=int(input('ENTER REG NO. TO DELETE: ')); self.db.delete(reg); print('Delete operation completed.')
        except ValueError: print('Invalid registration number.')
    def show_student(self):
        try:
            reg=int(input('ENTER REG NO.: ')); row=self.db.get(reg)
            if not row: print('Student not found.'); return
            r=student_result([row['subject1'],row['subject2'],row['subject3']])
            print(f"\n{row['reg_no']} | {row['name']} | {row['subject1']} | {row['subject2']} | {row['subject3']} | Total {r['total']} | Avg {r['average']} | {r['grade']} | {r['result']}")
        except ValueError: print('Invalid registration number.')
    def show_all(self):
        data=records(self.db.all())
        if not data: print('No students available.'); return
        print('\nREG NO | NAME | M1 | M2 | M3 | TOTAL | AVG | GRADE | RESULT')
        print('-'*80)
        ranked=sorted(data,key=lambda x:x['average'],reverse=True)
        for rank,x in enumerate(ranked,1): print(f"{x['reg_no']} | {x['name'][:15]} | {x['marks'][0]} | {x['marks'][1]} | {x['marks'][2]} | {x['total']} | {x['average']:.2f} | {x['grade']} | {x['result']} | Rank {rank}")
    def analytics(self):
        s=class_statistics(self.db.all())
        if not s['count']: print('No students available.'); return
        print('\n--- CLASS ANALYTICS ---')
        print('Total students:',s['count']); print('Passed:',s['passed']); print('Failed:',s['failed']); print('Class average:',s['average'])
        print('Topper:',s['topper']['reg_no'],s['topper']['name'],s['topper']['average'])
        print('Maximum failures in subject(s):',s['max_fail_subjects']); print('Maximum passes in subject(s):',s['max_pass_subjects'])
        print('Failed in exactly one course:',s['failed_exactly_one']); print('Failed in two or more courses:',s['failed_two_or_more'])
        print('Students with 100 in 2 or more courses:',s['perfect_two_or_more'])
    def run(self):
        while True:
            print('\n===== STUDENT GRADING & PERFORMANCE SYSTEM =====')
            print('1. Add student\n2. Update student\n3. Delete student\n4. Search student\n5. Display all + rank\n6. Class analytics\n7. Exit')
            choice=input('ENTER CHOICE: ').strip()
            if choice=='1': self.add_student()
            elif choice=='2': self.update_student()
            elif choice=='3': self.delete_student()
            elif choice=='4': self.show_student()
            elif choice=='5': self.show_all()
            elif choice=='6': self.analytics()
            elif choice=='7': print('Thank you.'); break
            else: print('Invalid choice.')

if __name__=='__main__': StudentGradingSystem().run()
