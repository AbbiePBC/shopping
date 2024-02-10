
from shopping import load_data

def test_load_data():

    # this is just a quick test so brittle - must be run from the root directory
    (evidence, label) = load_data('test/test_input.csv')

    assert len(evidence) == len(label) == 1
    assert len(evidence[0]) == 17
    assert evidence[0] == [0, 0.0, 0, 0.0, 1, 0.0, 0.2, 0.2, 0.0, 0.0, 1, 1, 1, 1, 1, 1, 0]
    assert label[0] == 0
