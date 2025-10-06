import pytest

@pytest.mark.stage03
def test_add_integers():
    from kadai import mul

    assert mul(4, 6) == 24