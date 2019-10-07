# -*- coding: utf-8 -*-

__author__ = 'Martin Bø'
__email__ = 'martinb@nmbu.no'

import pytest
import numpy as np


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return:  Median of data
    """

    sorted_data = sorted(data)
    num_elements = len(sorted_data)
    if num_elements == 0:
        raise ValueError
    if num_elements % 2 == 1:
        return sorted_data[num_elements // 2]
    else:
        return ((sorted_data[num_elements // 2 - 1] + sorted_data[
            num_elements // 2]) / 2)


def test_median_of_singleton():
    """Test if the function returns the median of a list with 1 element"""
    assert median([4]) == 4


def test_list_with_odd_number_of_elements():
    """Test if the function works for a list with odd number of elements"""
    data = [1, 3, 2]
    assert median(data) == np.median(data)


def test_list_with_even_number_of_elements():
    """Test if the median function works for a list with even number of
     elements"""
    data = [1, 3, 5, 99]
    assert median(data) == np.median(data)


def test_list_with_ordered_elements():
    """Test the median function on a list which is already sorted"""
    data = [1, 2, 3, 4, 5, 6]
    assert median(data) == np.median(data)


def test_list_with_reverse_ordered_elements():
    """Test the median function on a list in reverse order"""
    data = [6, 5, 4, 3, 2, 1]
    assert median(data) == np.median(data)


def test_list_with_unordered_elements():
    """Test the median function on a list with unordered elements"""
    data = [3, 6, 2, 1, 5, 4]
    assert median(data) == np.median(data)


def test_median_of_empty_list_valueerror():
    """Test the median function if it returns a value error when inserting  an
    empty list"""
    with pytest.raises(ValueError):
        median([])


def test_median_leaves_original_data_unchanged():
    """Test the median function if it changes the original list or input"""
    data = [4, 2, 3]
    original = data
    median(data)
    assert data is original


def test_median_works_for_tuple_and():
    """ Test the median function if it works for tuples"""
    #  Spør om denne på øving
    data = (4, 3, 5, 7, 8, 1, 82, -5)
    assert median(data) == np.median(data)
