def remove_duplicates(tuples):
    unique = []
    for t in tuples:
        if t not in unique:
            unique.append(t)
    return unique