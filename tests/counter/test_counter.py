from src.pre_built.counter import count_ocurrences
# Quase certeza que é occurrences e nao ocurrences


def test_counter():
    path = "data/jobs.csv"

    assert count_ocurrences(path, "python") == 1639

    assert count_ocurrences(path, "Jaguara") == 0

    assert count_ocurrences(path, "pYtHOn") == 1639

    assert count_ocurrences(path, "data engineer") == 1528
