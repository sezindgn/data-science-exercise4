"""Merge sort implementation with a before/after visualization."""

import matplotlib.pyplot as plt


def merge_sort(values):
    """Sort a list in place using the merge sort algorithm.

    The list is recursively split in half until each sublist has at
    most one element (already sorted by definition). The sublists are
    then merged back together in sorted order.
    """
    if len(values) <= 1:
        return

    mid = len(values) // 2
    left = values[:mid]
    right = values[mid:]

    merge_sort(left)
    merge_sort(right)

    _merge(values, left, right)


def _merge(values, left, right):
    """Merge two sorted lists (left, right) back into `values`.

    Repeatedly takes the smaller of the two current front elements
    from `left`/`right` and appends it to `values`, until one of the
    two sublists is exhausted. Any remaining elements are appended
    in order.
    """
    left_index = 0
    right_index = 0
    merged_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            values[merged_index] = left[left_index]
            left_index += 1
        else:
            values[merged_index] = right[right_index]
            right_index += 1
        merged_index += 1

    while left_index < len(left):
        values[merged_index] = left[left_index]
        left_index += 1
        merged_index += 1

    while right_index < len(right):
        values[merged_index] = right[right_index]
        right_index += 1
        merged_index += 1



def plot_values(values, title):
    """Display a bar chart of the given values with a descriptive title."""
    plt.bar(range(len(values)), values)
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()


if __name__ == "__main__":
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    plot_values(my_list, "Before Sorting")
    merge_sort(my_list)
    plot_values(my_list, "After Sorting")