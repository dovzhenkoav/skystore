import random


def get_random_code():
    code = int(f'{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}')
    return code
