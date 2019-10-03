# -*- coding: utf-8 -*-

__author__ = 'Martin Bø'
__email__ = 'martinb@nmbu.no'

#  from hypothesis import given,strategies


def bubble_sort(data1):
    sorted_list = list(data1)
    for i in range(len(sorted_list) - 1):
        for j in range(len(sorted_list) - 1 - i):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j+1],\
                                                     sorted_list[j]

    return sorted_list


def test_empty():
    """Test that the sorting function works for empty list"""
    assert len(bubble_sort([])) == 0


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]


def sorted_is_not_original():
    """Test that the sorting function returns a new object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    assert sorted_data != data


def test_original_unchanged():
    """Test that sorting leaves the original data unchanged."""
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    assert data == [3, 2, 1]
    return sorted_data  # Returns just to avoid pep8 violation


def test_sort_sorted():
    """Test that sorting works on sorted data"""
    sorted_data = [1, 2, 3, 4, 5]
    sorted_list = bubble_sort(sorted_data)

    for small, large in zip(sorted_list[:-1], sorted_list[1:]):
        assert small <= large


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data"""
    sorted_data = [5, 4, 3, 2, 1]
    sorted_list = bubble_sort(sorted_data)

    for small, large in zip(sorted_list[:-1], sorted_list[1:]):
        assert small <= large


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    equal_data = [1, 1, 1, 1, 1]
    sorted_list = bubble_sort(equal_data)

    for small, large in zip(sorted_list[:-1], sorted_list[1:]):
        assert small <= large


def test_sorting():
    """Test sorting for various cases"""
    various_lists = []

    for small, large in zip(various_lists[:-1], various_lists[1:]):
        assert small <= large
