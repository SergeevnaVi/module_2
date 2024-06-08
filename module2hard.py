import random

first_insert = random.randint(3, 20)


def generate_password(first_insert):
    second_insert = []
    for i in range(1, 21):
        if i == first_insert:
            continue
        for j in range(1, 21):
            if i != j and first_insert % (i + j) == 0:
                second_insert.append((i, j))

    result_part = []

    for i, j in second_insert:
        result_part.append(f'{i}{j}')

    result = ''.join(result_part)
    return result


result = generate_password(first_insert)
print(f'Число из первой вставки: {first_insert}')
print(f'Нужный пароль - {result}')
