import json
subj = {}
with open('6-0.txt', 'r') as f:
    for line in f:
        subj, lesson, practise, lab = line.split()
        subj[subj] = int(lesson) + int(practise) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')
