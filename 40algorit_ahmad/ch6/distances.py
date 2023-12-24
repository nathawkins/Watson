'''
Library for distance metrics.
Author: Nat Hawkins
Date (YYYY-MM-DD): 2023-12-23
'''

# Imports ----------------------------------------------------------------------
from typing import Iterable

# Functions --------------------------------------------------------------------
def euclideanDistance(x: Iterable, y: Iterable) -> float:
    '''
    Calculates the euclidean distance between two points.
    
    Given two iterables x and y of length N, calculates the euclidean distance
    as $d(x,y) = (\sum_{i = 1}^{N} (x_{i} - y_{i})^{2})^{1/2}$.
    
    Parameters
    ----------
    - x (Iterable): Iterable object of length N
    - y (Iterable): Iterable object of length N

    Returns
    -------
    float: Euclidean distance between x and y
    
    Raises
    ------
    TypeError: x and/or y are not Iterables
    ValueError: x and y are of unequal length

    Doctests
    --------
    >>> euclideanDistance((0,0), (3,4))
    5.0
    >>> round(euclideanDistance((0,0,0), (1,1,1)), 3)
    1.732
    >>> euclideanDistance(3, [1,2])
    Traceback (most recent call last):
        ...
    TypeError: Expecting x and y of type Iterable, received x (<class 'int'>) and y (<class 'list'>).
    >>> euclideanDistance([1,2], [3,4,5])
    Traceback (most recent call last):
        ...
    ValueError: Length of x and y do match. 2 != 3.
    '''
    # Input objects not the correct type
    if not (isinstance(x, Iterable) and isinstance(y, Iterable)):
        raise TypeError(f"Expecting x and y of type Iterable, received x ({type(x)}) and y ({type(y)}).")
    
    # Input lengths do not match
    if len(x) != len(y):
        raise ValueError(f"Length of x and y do match. {len(x)} != {len(y)}.")
    
    return sum((x_i - y_i)**2 for x_i, y_i in zip(x, y))**(1/2)



def manhattanDistance(x: Iterable, y: Iterable) -> float:
    '''
    Calculates the manhattan distance between two points.
    
    Given two iterables x and y of length N, calculates the manhattan distance
    as $d(x,y) = \sum_{i = 1}^{N} |x_{i} - y_{i}|$.
    
    Parameters
    ----------
    - x (Iterable): Iterable object of length N
    - y (Iterable): Iterable object of length N

    Returns
    -------
    float: Manhattan distance between x and y
    
    Raises
    ------
    TypeError: x and/or y are not Iterables
    ValueError: x and y are of unequal length

    Doctests
    --------
    >>> manhattanDistance((0,0), (3,4))
    7.0
    >>> round(manhattanDistance((0,0,0), (1,1,1)), 3)
    3.0
    >>> manhattanDistance(3, [1,2])
    Traceback (most recent call last):
        ...
    TypeError: Expecting x and y of type Iterable, received x (<class 'int'>) and y (<class 'list'>).
    >>> manhattanDistance([1,2], [3,4,5])
    Traceback (most recent call last):
        ...
    ValueError: Length of x and y do match. 2 != 3.
    '''
    # Input objects not the correct type
    if not (isinstance(x, Iterable) and isinstance(y, Iterable)):
        raise TypeError(f"Expecting x and y of type Iterable, received x ({type(x)}) and y ({type(y)}).")
    
    # Input lengths do not match
    if len(x) != len(y):
        raise ValueError(f"Length of x and y do match. {len(x)} != {len(y)}.")
    
    return float(sum(abs(x_i - y_i) for x_i, y_i in zip(x, y)))



def cosineDistance(x: Iterable, y: Iterable) -> float:
    '''
    Calculates the cosine distance between two points.
    
    Given two iterables x and y of length N, calculates the cosine distance
    as $d(x,y) = 1 - (\sum_{i = 1}^{N} x_{i} y_{i})/(||x|| ||y||)$.
    
    Parameters
    ----------
    - x (Iterable): Iterable object of length N
    - y (Iterable): Iterable object of length N

    Returns
    -------
    float: Cosine distance between x and y in the range [0, 2]
    
    Raises
    ------
    TypeError: x and/or y are not Iterables
    ValueError: x and y are of unequal length
    ZeroDivisionError: ||x|| = 0 or ||y|| = 0

    Doctests
    --------
    >>> round(cosineDistance((1,2), (3,4)), 3)
    0.016
    >>> round(cosineDistance((1,2,3), [4,5,6]), 3)
    0.025
    >>> cosineDistance(3, [1,2])
    Traceback (most recent call last):
        ...
    TypeError: Expecting x and y of type Iterable, received x (<class 'int'>) and y (<class 'list'>).
    >>> cosineDistance([1,2], [3,4,5])
    Traceback (most recent call last):
        ...
    ValueError: Length of x and y do match. 2 != 3.
    >>> cosineDistance([0,0], [2,1])
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Cosine distance undefined for zero-magnitude iterable. ||x|| = 0.0, ||y|| = 2.24.
    '''
    # Input objects not the correct type
    if not (isinstance(x, Iterable) and isinstance(y, Iterable)):
        raise TypeError(f"Expecting x and y of type Iterable, received x ({type(x)}) and y ({type(y)}).")
    
    # Input lengths do not match
    if len(x) != len(y):
        raise ValueError(f"Length of x and y do match. {len(x)} != {len(y)}.")
    
    # Calculate magnitudes
    mag_x = (sum(x_i**2 for x_i in x))**(1/2)
    mag_y = (sum(y_i**2 for y_i in y))**(1/2)
    if mag_x == 0 or mag_y == 0:
        raise ZeroDivisionError(f"Cosine distance undefined for zero-magnitude iterable. ||x|| = {round(mag_x, 2)}, ||y|| = {round(mag_y, 2)}.")
    
    return 1 - sum(x_i * y_i for x_i, y_i in zip(x, y))/(mag_x * mag_y)

if __name__ == '__main__':
    import doctest
    doctest.testmod()