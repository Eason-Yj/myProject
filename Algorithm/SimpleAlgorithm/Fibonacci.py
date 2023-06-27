"""
斐波那契数列
"""


def fibonacci_recursion(n):
    """
    递归
    Parameters
    ----------
    n

    Returns
    -------

    """
    if n == 1:
        return 1
    if n == 2:
        return 1

    res = fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)
    return res


def fibonacci_for(n):
    """
    循环
    Parameters
    ----------
    n

    Returns
    -------

    """
    res = []
    a = 1
    b = 1
    for i in range(n):
        if i < 2:
            res.append(1)
        else:
            a, b = b, a + b
            res.append(b)

    return res


def fibonacci_for2(n):
    """
    循环
    Parameters
    ----------
    n

    Returns
    -------

    """
    res = []
    a = 1
    b = 1
    for i in range(n):
        if i < 2:
            res.append(1)
        else:
            current = a + b
            a = b
            b = current
            res.append(current)

    return res


print(fibonacci_for(8))
print(fibonacci_for2(8))
