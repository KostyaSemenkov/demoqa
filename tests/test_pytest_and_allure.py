import pytest


@pytest.mark.skip(reason='Причина пропуска')
def test_skip():
    assert True


@pytest.mark.xfail(condition=True, reason='причина, по которой тестовая функция помечена как xfail')# если тест упадет то пометится как скипт, если пройдет то как тест пройден, в обоих случаях в отчете добавится тег ожидаемый сбой
def test_xfail_1():
    assert False


@pytest.mark.xfail(condition=True, reason='причина, по которой тестовая функция помечена как xfail')
def test_xfail_2():
    assert True


@pytest.mark.skipif(condition='2 + 2 != 5') # пропускает если условие True
def test_skip_by_triggered_condition():
    pass


@pytest.mark.parametrize('param', [1, 2, 3, 4, 6])
def test_parametrize(param):
    assert (param % 2) == 0