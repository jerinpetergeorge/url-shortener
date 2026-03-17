import secrets
import string

BASE62_ALPHABET = string.digits + string.ascii_letters
SHORT_CODE_LENGTH = 7


def generate_short_code(length: int = SHORT_CODE_LENGTH) -> str:
    """
    Generate a cryptographically secure random Base62 short code.
    Retries are handled in the model's save() method.
    """
    return "".join(secrets.choice(BASE62_ALPHABET) for _ in range(length))
