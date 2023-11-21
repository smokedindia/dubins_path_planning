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
    def __init__(self) -> None:
        self.start_pos = [4.8, 8.35, pi]
        # 1
        self.end_pos = [1.205, 1.5, pi / 2]
        # 2
        # self.end_pos = [2.455, 1.5, pi / 2]
        # 3
        # self.end_pos = [3.705, 1.5, pi / 2]
        # 4
        # self.end_pos = [4.955, 1.5, pi / 2]

        self.obs = [
            [0.58, 0, 0.1, 2.2],
            [1.83, 0, 0.1, 2.2],
            [3.08, 0, 0.1, 2.2],
            [4.33, 0, 0.1, 2.2],
            [5.58, 0, 0.1, 2.2],
            [6.5, 0, 3, 9.3],
            [5.25, 7.5, 1.25, 0.1],
            [5.25, 9.2, 1.25, 0.1],
        ]
