import hashlib

def to_md5(_str: str) -> str:
    return hashlib.md5(_str.encode()).hexdigest()