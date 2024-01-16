def test_load_multi_values(pytester):
    # create the test code file
    test_file_path = pytester.copy_example("example_test_load_multi_values_tester.py")
    test_file_path.rename("test_load_multi_values_tester.py")

    # create the data file
    pytester.copy_example("data_load_multi_values_tester.yaml")

    result = pytester.runpytest("-k", "test_load_multi_values_tester", "--param-from-files")

    result.assert_outcomes(passed=2)
