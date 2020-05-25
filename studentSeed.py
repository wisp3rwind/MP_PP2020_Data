def studentSeed(name):
    """
    Returns the random seed associated with the students name to reproduce the same number again
    by adding the ord() from each char in the name.
    Its not bijective, but should be sufficient.

    Args:
    name (string): students name

    Returns:
    seed (integer): the generated random seed

    """
    seed = 0
    for char in name:
        seed += ord(char)
    return seed
