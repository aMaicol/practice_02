mail = input("Ingrese su correo: ").strip()

if mail.count("@") != 1:
    valid = False
else:
    user, domain = mail.split("@")

    last_dot = domain.rfind(".")

    valid = (
        len(user) > 0
        and not mail.startswith((".", "@"))
        and not mail.endswith((".", "@"))
        and last_dot > 0
        and len(domain[last_dot + 1 :]) >= 2
    )

print("El email es válido." if valid else "El email no es válido.")
