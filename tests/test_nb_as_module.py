"""Rudimentary tests."""
from nb_as_module import nb_as_module


def test_importing_nb1(capsys):
    nb1 = nb_as_module("tests/nb1.ipynb", "nb1")

    assert nb1.__name__ == "nb1", "__name__ does not match name"

    # Test function
    nb1.hello()
    captured = capsys.readouterr()
    result = captured.out.strip() == "Hello, world."
    assert result, f"Output does not match {captured.out}."

    # Test class
    test_instance = nb1.TestClass()
    test_instance()
    captured = capsys.readouterr()
    result = captured.out.strip() == "Hello from TestClass."
    assert result, f"Output does not match {captured.out}."

    # Test docstring
    assert nb1.__doc__ == "Here is my docstring.", "Docstring error."
