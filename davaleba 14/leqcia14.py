import csv
list=[]
with open('14.csv','r') as file:
    csv_read = csv.reader(file, delimiter=',')
    next(csv_read)

    for row in csv_read:

        if row[0] not in list:
            student={row[0]:row[2]}
            list.append(student)



combined_grades = {}
for person in list:
    for name,grade in person.items():
        if name in combined_grades:
            combined_grades[name].append(int(grade))
        else:
            combined_grades[name] = [int(grade)]


for value in combined_grades:
    average = sum(combined_grades[value])/len(combined_grades[value])
    combined_grades[value] = average

print(combined_grades)


