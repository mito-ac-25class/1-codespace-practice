import pytest

@pytest.mark.stage04
def test_add_integers():
    from kadai import div

    assert div(7, 2) == 3.5