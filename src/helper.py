from typing import List, Tuple


class Helper:

    @staticmethod
    def get_max_over_range(arr: List[int], a: int, b: int) -> int:
        return max(arr[a:b])

    @staticmethod
    def get_diffs(values: List[int]) -> List[Tuple[int, int]]:
        diffs = []
        for index, value in enumerate(values):
            first_item = value - values[index - 1] if index > 0 else 0
            second_item = value - values[index + 1] if index < len(values) - 1 else 0
            diffs.append((first_item, second_item))
        return diffs
