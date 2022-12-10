import pytest
@pytest.mark.parametrize('task',['test_1_data','test2_data'])
def test_tc01(task):
    assert len(task) == 7
   
