import pytest
from main import findHighestConsecutive


def test_find_highest_consecutive_letter_with_one_consecutive_letter():
    input_str = "aabbbbcccddee"
    expected_output = "b : 4"
    assert findHighestConsecutive(input_str) == expected_output


def test_find_highest_consecutive_letter_with_multiple_consecutive_letters():
    input_str = "aabbbbcccddddeeee"
    expected_output = "b : 4"
    assert findHighestConsecutive(input_str) == expected_output


def test_find_highest_consecutive_letter_with_no_consecutive_letters():
    input_str = "abcdefg"
    expected_output = "a : 1"
    assert findHighestConsecutive(input_str) == expected_output


def test_find_highest_consecutive_letter_with_empty_input_str():
    input_str = ""
    expected_output = "None : 0"
    assert findHighestConsecutive(input_str) == expected_output
