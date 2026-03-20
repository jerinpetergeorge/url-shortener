import secrets
import string

from .settings import CODE_LENGTH

BASE62_ALPHABET = string.digits + string.ascii_letters


def generate_short_code(length: int = CODE_LENGTH) -> str:
    """
    Generate a cryptographically secure random Base62 short code.
    Retries are handled in the model's save() method.
    """
    return "".join(secrets.choice(BASE62_ALPHABET) for _ in range(length))
