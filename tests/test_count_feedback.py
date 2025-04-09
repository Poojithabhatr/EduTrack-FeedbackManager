from count_feedback import count_feedback

def test_count_feedback():
    data = [{"name": "A"}, {"name": "B"}, {"name": "C"}]
    assert count_feedback(data) == 3
