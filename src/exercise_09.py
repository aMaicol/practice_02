students = [
    {"name": " Ana García ", "grade": "8", "status": "aprobado"},
    {"name": "pedro lópez", "grade": "4", "status": "DESAPROBADO"},
    {"name": "MARÍA FERNÁNDEZ", "grade": "10", "status": "Aprobado"},
    {"name": "ana garcía", "grade": "9", "status": "aprobado"},
    {"name": None, "grade": "7", "status": "aprobado"},
    {"name": "Luis Martínez ", "grade": None, "status": "aprobado"},
    {"name": " carlos RUIZ", "grade": "6", "status": "aprobado"},
    {"name": "PEDRO LÓPEZ ", "grade": "3", "status": "desaprobado"},
    {"name": " ", "grade": "5", "status": "aprobado"},
    {"name": "María Fernández", "grade": "7", "status": "APROBADO"},
    {"name": "Sofía Torres", "grade": "9", "status": "Aprobado"},
    {"name": " sofía torres ", "grade": "8", "status": "aprobado"},
    {"name": "Carlos Ruiz", "grade": "6", "status": "APROBADO"},
    {"name": "Roberto Díaz", "grade": "absent", "status": "ausente"},
    {"name": "roberto díaz", "grade": "", "status": "Ausente"},
    {"name": None, "grade": None, "status": None},
    {"name": "Laura Méndez", "grade": "7", "status": "aprobado"},
    {"name": " laura méndez", "grade": "8", "status": "Aprobado"},
    {"name": "GABRIELA RÍOS", "grade": "5", "status": "aprobado"},
    {"name": "gabriela ríos ", "grade": "4", "status": "Desaprobado"},
]

students_clean = {}

for student in students:
    name = student.get("name")
    grade = student.get("grade")
    status = student.get("status")

    if not name or not name.strip():
        continue

    if not grade or not str(grade).isdigit():
        continue

    name = name.strip().title()
    grade = int(grade)
    status = status.strip().title()

    if name not in students_clean or grade > students_clean[name]["grade"]:
        students_clean[name] = {"name": name, "grade": grade, "status": status}

students_list = list(students_clean.values())
students_list.sort(key=lambda x: x["name"])

print("Registros limpios de alumnos:\n")
print(f"{'Nombre':<20} {'Nota':<5} {'Estado'}")
print("-" * 50)

for student in students_list:
    print(f"{student['name']:<20} {student['grade']:<5} {student['status']}")

print(f"\nTotal de alumnos válidos: {len(students_list)}")
