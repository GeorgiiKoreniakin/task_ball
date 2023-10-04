"""Test modul"""

import pytest

from ball import degree

test_data = (
    ((10, 3, 5, 1), 33.46),
    ((15, 6, 2), 257.33),
    ((5, 3, 10), 214.86),
)


@pytest.mark.parametrize('source, expected', test_data)
def test_ball(source: tuple[float], expected: float):
    assert degree(*source) == expected