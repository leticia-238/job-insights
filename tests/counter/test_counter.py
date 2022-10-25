from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("src/jobs.csv", "front end") == 13
    assert count_ocurrences("src/jobs.csv", "Front END") == 13
