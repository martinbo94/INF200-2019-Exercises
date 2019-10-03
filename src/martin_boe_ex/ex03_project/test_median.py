# -*- coding: utf-8 -*-

__author__ = 'Martin Bø'
__email__ = 'martinb@nmbu.no'

import pytest


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return:  Median of data
    """

    sorted_data = sorted(data)
    num_elements = len(sorted_data)

    if num_elements % 2 == 1:
        return sorted_data[num_elements // 2]
    else:
        return ((sorted_data[num_elements] // 2 - 1) + sorted_data[
            num_elements // 2]) / 2


def test_median_of_singleton():
    assert median([4]) == 4


def test_list_with_odd_number_of_elements():
    assert median([1, 3, 2])


def test_list_with_even_number_of_elements():
    assert median([1, 3, 2, 99])


def test_list_with_ordered_elements():
    assert median([1, 2, 3, 4, 5, 6])


def test_list_with_reverse_ordered_elements():
    assert median([6, 5, 4, 3, 2, 1])


def test_list_with_unordered_elements():
    assert median([3, 6, 2, 1, 5, 4])


def test_median_raise_value_error_on_empty_list():
    with pytest.raises(ValueError):
        median([])
