import csv

with open("vacancy.csv", encoding="utf-8") as file:
    reader = list(csv.reader(file, delimiter=";"))[1:]
    workTypeCount = {}
    workTypeSalarySum = {}
    workTypeSalaryMean = {}

    for salary, workType, companySize, role, company in reader:
        workTypeCount[workType] = workTypeCount.get(workType, 0) + 1
        workTypeSalarySum[workType] = workTypeSalarySum.get(workType, 0) + int(salary)
        workTypeSalaryMean[workType] = workTypeSalarySum.get(workType, 0) / workTypeCount.get(workType, 0)

    for i in range(len(reader)):
        reader[i].append((int(reader[i][0]) / workTypeSalaryMean[reader[i][1]]) * 100)

with open("vacancy_procent.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow("Salary;Work_Type;Company_Size;Role;Company;percent".split(";"))
    writer.writerows(reader)