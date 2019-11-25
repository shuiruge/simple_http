
def get_batches(size, xs):
    """Converts the iterable `xs` to an iterable of batches, with size `size`.

    Args:
        size: Integer.
        xs: Iterable of objects.

    Returns:
        Iterable of lists of objects.
    """
    batch = []
    for x in xs:
        batch.append(x)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch
