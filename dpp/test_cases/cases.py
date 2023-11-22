from math import pi


class TestCase:
    """Provide some test cases for a 10x10 map."""

    def __init__(self):
        self.start_pos = [4.6, 2.4, 0]
        self.end_pos = [1.6, 8, -pi / 2]

        self.start_pos2 = [4, 4, 0]
        self.end_pos2 = [4, 8, 1.2 * pi]

        self.obs = [
            [2, 3, 6, 0.1],
            [2, 3, 0.1, 1.5],
            [4.3, 0, 0.1, 1.8],
            [6.5, 1.5, 0.1, 1.5],
            [0, 6, 3.5, 0.1],
            [5, 6, 5, 0.1],
        ]


class Hot6Case:
    def __init__(self, parking_idx, reverse) -> None:
        self.start_pos = [2.8, 5, pi]
        if parking_idx == 1:
            # 1
            self.end_pos = [0.35 + 0.75/2, 1.35/2, -pi / 2]
        elif parking_idx == 2:
            # 2
            self.end_pos = [1.1 + 0.75/2, 1.35/2, -pi / 2]
        elif parking_idx == 3:
            # 3
            self.end_pos = [1.85 + 0.75/2, 1.35/2, -pi / 2]
        elif parking_idx == 4:
            # 4
            self.end_pos = [2.6 + 0.75/2, 1.35/2, -pi / 2]
        else:
            raise ValueError("parking_idx must be 1, 2, 3 or 4")
        
        if reverse:
            self.end_pos[2] *= -1

        self.obs = [
            [0.35, 0, 0.05, 1.35],
            [1.1, 0, 0.05, 1.35],
            [1.85, 0, 0.05, 1.35],
            [2.6, 0, 0.05, 1.35],
            [3.35, 0, 0.05, 1.35],
            [5, 0, 1, 5.3],
            [3.15, 5.4, 1.85, 0.05],
            [3.15, 4.4, 1.85, 0.05],
        ]
