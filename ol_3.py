import csv

def find_roles(companyName: str = "") -> list:
    """Описание функции find_roles.

    Описание аргументов:
    companyName – название компании, в которой будут искаться вакансии

    """

    listOfRoles = []

    with open("vacancy.csv", encoding="utf-8") as file:
        reader = list(csv.reader(file, delimiter=";"))[1:]

        for salary, workType, companySize, role, company in reader:
            if companyName in company:
                listOfRoles.append([role, salary])
            else:
                pass

    return listOfRoles

while True:
    companyName = input()

    if companyName == "None":
        break
    else:
        pass

    companyRoles = find_roles(companyName)
    if len(companyRoles) == 0:
        print("К сожалению, ничего не удалось найти")
    else:
        for roleName, roleSalary in companyRoles:
            print(f"В {companyName} найдена вакансия: {roleName}. З/п составит: {roleSalary}")