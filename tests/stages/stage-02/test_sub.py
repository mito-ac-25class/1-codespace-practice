import pytest

@pytest.mark.stage02
def test_sub_integers():
    from kadai import sub

    assert sub(11, 3) == 8 # 11 - 3 = 8 を返すようにしよう