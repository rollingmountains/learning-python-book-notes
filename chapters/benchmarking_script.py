import pybench_runner as test

# Actual play in the format the orchestrator accepts
# Plays should be in a record fromat in tuple
test_data_list = [
    (2000, 5, lambda: [x**2 for x in range(100)], "list comprehension"),
    (2000, 5, lambda: list((pow(2, 1000) for x in range(1000))), "builtin generator"),
]
test_data_pythons = [
    (3000, 6, "list((pow(2, 1000) for x in range(1000)))", "builtin generator")
]

pythons = ["/opt/miniconda3/bin/python", "/Users/balapaudel/.pyenv/shims/python"]

# test.runner(test_data_builtin)
if __name__ == "__main__":
    # make request to the orchestrator to run the play and share the play format
    test.runner(test_data_pythons, pythons)
