import random
import string


def random_str(panjang: int) -> str:
    hasil_str = "".join(random.choice(string.ascii_letters)
                        for i in range(panjang))
    return hasil_str
