def verify_input(user_input: str) -> bool:
    # Intentionally flawed validation (lab behavior)
    if user_input.lower() in ["http", "https"]:
        return False
    return True

