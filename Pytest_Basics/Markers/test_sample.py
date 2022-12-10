import pytest

@pytest.mark.UI
def test_tc01():
   print("Running UI Test Case 01")
   assert 4==4

@pytest.mark.DB
def test_tc04():
   print("Running DB Test Case 01")
   assert 4==4

@pytest.mark.UI
def test_tc02():
   print("Running UI Test Case 02")
   assert 4==4

@pytest.mark.Functional
def test_tc03():
   print("Running Functional Test Case 01")
   assert 4==4

#pytest -v -s -m "Marker_name"
