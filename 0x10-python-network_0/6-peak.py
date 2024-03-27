#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Finds a peak (local maximum) in a list of unsorted integers.

    Args:
        list_of_integers: A list of integers.

    Returns:
        An integer representing a peak in the list.
    """

    if len(list_of_integers) < 3:
        return None  # List must have at least 3 elements for a peak

    def find_peak_helper(left, right):
        """
        Helper function to find a peak recursively using binary search.

        Args:
            left: Index of the leftmost element in the current sublist.
            right: Index of the rightmost element in the current sublist.

        Returns:
            An integer representing a peak in the sublist.
        """

        if left == right:
            return list_of_integers[left]  # Single element is its own peak

        mid = (left + right) // 2

        # Check if middle element is a peak
        if (
            list_of_integers[mid] > list_of_integers[mid - 1]
            and list_of_integers[mid] > list_of_integers[mid + 1]
        ):
            return list_of_integers[mid]

        # If middle element is not a peak, search in the appropriate half
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            return find_peak_helper(left, mid - 1)
        else:
            return find_peak_helper(mid + 1, right)

    return find_peak_helper(0, len(list_of_integers) - 1)
