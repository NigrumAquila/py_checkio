def frequency_sorting(numbers):
    return sorted(sorted(numbers), key=numbers.count, reverse=True)