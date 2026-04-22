def prime(number):
    """Return the nth prime number."""
    if number < 1:
        raise ValueError("there is no zeroth prime")

    def is_prime(number_to_check):
        if number_to_check < 2:
            return False
        if number_to_check in (2,3):
            return True
        if number_to_check % 2 == 0 or number_to_check % 3 == 0:
            return False

        first_root = 5
        while first_root * first_root <= number_to_check:
            if number_to_check % first_root == 0 or number_to_check % (first_root + 2) == 0:
                return False
            first_root += 6
        return True

    count = 0
    candidate = 1

    while count < number:
        candidate += 1
        if is_prime(candidate):
            count += 1

    return candidate