import pytest

def test_tc01():
   if '10' == '10':
      pytest.fail("Failng the tc..!!")

def test_tc04():
   if '10' != '10':
      pytest.fail("Failng the tc")
   pytest.skip("Skipping the TC using pytest")
   pytest.xfail("Skipping the TC using pytest")



#pytest -v -s -m "Marker_name"
