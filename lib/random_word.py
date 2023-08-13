from secrets import choice
from string import ascii_lowercase, digits


def random_word(length: int) -> str:
    return "".join(choice(ascii_lowercase + digits) for _ in range(length))
