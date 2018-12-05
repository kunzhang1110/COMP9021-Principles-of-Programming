def transpose(ls):
    """Return a transposed matrix"""
    transposed_ls = [list(x) for x in zip(*ls)]
    return transposed_ls

ls =