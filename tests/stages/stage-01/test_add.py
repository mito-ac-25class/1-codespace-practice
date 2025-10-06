import pytest

@pytest.mark.stage01
def test_add_integers():
    from kadai import add

    assert add(5, 8) == 13 # 5 + 8 = 13 を返すようにしよう