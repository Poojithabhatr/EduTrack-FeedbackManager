from search_feedback import search_feedback

def test_search_feedback():
    data = [{"name": "A", "feedback": "Good"}, {"name": "B", "feedback": "Nice"}]
    assert search_feedback(data, "A") == [{"name": "A", "feedback": "Good"}]
