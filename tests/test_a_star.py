from a_star import a_star


def test_a_star():
    assert a_star("Lugoj") == [
        "Lugoj",
        "Mehadia",
        "Dobreta",
        "Craiova",
        "Pitesti",
        "Bucharest",
    ]
    assert a_star("Arad") == [
        "Arad",
        "Sibiu",
        "Rimnicu Vilcea",
        "Pitesti",
        "Bucharest",
    ]
    assert a_star("Oradea") == [
        "Oradea",
        "Sibiu",
        "Rimnicu Vilcea",
        "Pitesti",
        "Bucharest",
    ]
