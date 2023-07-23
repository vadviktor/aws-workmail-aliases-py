from string import ascii_lowercase, digits
from secrets import choice


def random_word(length=16) -> str:
    return "".join(choice(ascii_lowercase + digits) for _ in range(length))
