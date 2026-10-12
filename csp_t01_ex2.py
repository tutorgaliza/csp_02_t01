"""
Faker é un paquete que se usa para xerar datos ficticios
de usuarios e así poder facer probas nas nosas aplicacións.

Neste exercicio debes empregar Faker para desenvolver
un programa que cree os datos ficticios de 15 usuarios.
Os datos deben almacenarse nun dicionario, de forma que:

    ● Os usuarios estean identificados por un código comprendido
    entre o número 1 e o 15. Non poderá haber dous usuarios co mesmo código.

    ● Para cada usuario se almacenen os seguintes datos:
        nome, dirección, correo electrónico, teléfono.

    O programa debe mostrar por pantalla os datos
    de todos os usuarios creados.

    Despois, o programa seleccionará aleatoriamente
    a un dos usuarios para mostrar a seguinte mensaxe:

        "O usuario chamado NOME foi o afortunado!"

    Á hora de realizar a tarefa, deberás ter en conta o seguinte:

        ● Debes desenvolver o programa empregando Git e GitHub.
        Podes crear un repositorio público en GitHub coa túa
        conta de usuario para logo compartilo co profesor.

        ● Debes empregar un contorno virtual e xerar
        o ficheiro de dependencias, de forma que cando o profesor clone
        o teu repositorio poida instalar automaticamente todos os paquetes
        necesarios a través dese ficheiro.

    Valorarase positivamente que durante o desenvolvemento do programa
    se fagan varios commits no repositorio.
"""

"""
    métodos:

    print(fake.name())
    print(fake.first_name())
    print(fake.last_name())

    print(fake.email())
    print(fake.user_name())
    print(fake.password())

    print(fake.address())
    print(fake.street_address())
    print(fake.city())
    print(fake.postcode())
    print(fake.country())

    print(fake.phone_number())

    print(fake.company())
    print(fake.job())

    print(fake.date())
    print(fake.date_of_birth())
    print(fake.date_time())

    print(fake.text())
    print(fake.sentence())
    print(fake.word())

    print(fake.random_int(min=1, max=100))
"""

from faker import Faker
import random as rnd


# lo configura para el idioma español de españa
fake = Faker('es_ES')

# nome, dirección, correo electrónico, teléfono.
# las cabeceras con su ancho de columna
# headers = {'Nombre': 30, 'Dirección': 60, 'Email': 30, 'Teléfono': 15}
people = {
    i: (
        fake.name(),
        fake.address().replace('\n', ', '),
        fake.email(),
        fake.phone_number(),
    )
    for i in range(1, 16)
}

# esto sería usando un diccionario de diccionarios
# gasta algo más de memoria al repetir las claves
# people = {
#     i: {
#         'name': fake.name(),
#         'address': fake.address(),
#         'email': fake.email(),
#         'phone_number': fake.phone_number(),
#     }
#     for i in range(1, 16)
# }

# para establecer el ancho de columna de la cabecera
# print(''.join([format(header, f'{width}') for header, width in headers.items()]))
print('*' * 60)
print(f'{"USUARIOS":^60}')
print('*' * 60)

for code, person in people.items():
    print(f'Usuario {code}:')
    for feature in person:
        print(f'\t{feature}')

# sorteo previo casting to a tuple or list
# print(f'O usuario chamado {rnd.choice(tuple(people.values()))[0]} foi o afortunado!')

# sorteo usando la clave del diccionario para generar el número aleatoriamente
print(f'O usuario chamado {people[rnd.randint(1, len(people))][0]} foi o afortunado!')