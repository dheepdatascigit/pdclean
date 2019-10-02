import pytest
from pdtools import pdtools

def test_extractnum_pnum():
	test_str = "xyz share was 98.14 and yesterday was 97.3 and day before was 98 dollars"
	assert pdtools.extract_num(test_str, select_logic='first') == 98.14
	assert pdtools.extract_num(test_str, select_logic='sum') == 293.44
	assert round(pdtools.extract_num(test_str, select_logic='mean'), 2) == 97.81
	assert len(pdtools.extract_num(test_str)) == 3
	assert 97.34 not in pdtools.extract_num(test_str) 

def test_extractnum_nnum():
	test_str = "todays weather was -40.30 but yesterday for +10.30 so it had 20 degres change"
	assert pdtools.extract_num(test_str, select_logic='first') == -40.3
	assert round(pdtools.extract_num(test_str, select_logic='sum')) == -10
	assert round(pdtools.extract_num(test_str, select_logic='mean'), 2) == -3.33
	assert len(pdtools.extract_num(test_str)) == 3, "passed"
	assert 97.34 not in pdtools.extract_num(test_str) 
