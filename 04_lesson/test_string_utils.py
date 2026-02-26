import pytest
from string_utils import StringUtils


class TestStringUtils:
    def setup_method(self):
        self.utils = StringUtils()


    # Тесты для capitalize
    def test_capitalize_normal(self):
        assert self.utils.capitalize("skypro") == "Skypro"
        assert self.utils.capitalize("test") == "Test"
        assert self.utils.capitalize("123abc") == "123abc"


    def test_capitalize_empty(self):
        assert self.utils.capitalize("") == ""


    def test_capitalize_uppercase(self):
        assert self.utils.capitalize("SKYPRO") == "Skypro"


    # Тесты для trim
    def test_trim_normal(self):
        assert self.utils.trim("   skypro") == "skypro"
        assert self.utils.trim("    test    ") == "test    "


    def test_trim_no_spaces(self):
        assert self.utils.trim("skypro") == "skypro"


    def test_trim_only_spaces(self):
        assert self.utils.trim("    ") == ""


    # Тесты для contains
    def test_contains_positive(self):
        assert self.utils.contains("SkyPro", "S") == True
        assert self.utils.contains("SkyPro", "P") == True


    def test_contains_negative(self):
        assert self.utils.contains("SkyPro", "U") == False
        assert self.utils.contains("SkyPro", "u") == False


    def test_contains_empty(self):
        assert self.utils.contains("", "a") == False


    def test_contains_empty_symbol(self):
        assert self.utils.contains("test", "") == True


    # Тесты для delete_symbol
    def test_delete_symbol_normal(self):
        assert self.utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert self.utils.delete_symbol("SkyPro", "Pro") == "Sky"


    def test_delete_symbol_not_found(self):
        assert self.utils.delete_symbol("SkyPro", "X") == "SkyPro"


    def test_delete_symbol_empty(self):
        assert self.utils.delete_symbol("", "a") == ""


    def test_delete_symbol_empty_symbol(self):
        assert self.utils.delete_symbol("test", "") == "test"

    # Негативные тесты для всех методов
    def test_invalid_types(self):
        invalid_values = [None, 123, [1, 2, 3], {"key": "value"}, True, 3.14]