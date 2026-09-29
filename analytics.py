from grading import student_result

def records(rows):
    out=[]
    for r in rows:
        marks=[r['subject1'],r['subject2'],r['subject3']]
        out.append({'reg_no':r['reg_no'],'name':r['name'],'marks':marks,**student_result(marks)})
    return out

def class_statistics(rows):
    data=records(rows)
    if not data: return {'count':0,'passed':0,'failed':0,'average':0,'topper':None,'max_fail_subjects':[],'max_pass_subjects':[],'failed_exactly_one':0,'failed_two_or_more':0,'perfect_two_or_more':[]}
    passed=sum(x['result']=='PASS' for x in data)
    averages=[x['average'] for x in data]
    fail_counts=[sum(x['marks'][i] < 50 for x in data) for i in range(3)]
    pass_counts=[sum(x['marks'][i] > 50 for x in data) for i in range(3)]
    max_fail=max(fail_counts); max_pass=max(pass_counts)
    return {'count':len(data),'passed':passed,'failed':len(data)-passed,'average':round(sum(averages)/len(averages),2),
            'topper':max(data,key=lambda x:x['average']),'max_fail_subjects':[i+1 for i,v in enumerate(fail_counts) if v==max_fail],
            'max_pass_subjects':[i+1 for i,v in enumerate(pass_counts) if v==max_pass],
            'failed_exactly_one':sum(sum(m<50 for m in x['marks'])==1 for x in data),
            'failed_two_or_more':sum(sum(m<50 for m in x['marks'])>=2 for x in data),
            'perfect_two_or_more':[x['reg_no'] for x in data if sum(m==100 for m in x['marks'])>=2]}
