import unittest


def is_valid_password(password):
    return (
        len(password) >= 8
        and any(char.isdigit() for char in password)
        and any(char.isupper() for char in password)
    )


class test_password(unittest.TestCase):
    def setUp(self):
        self.password = "purrumurriaO1"
        
    def test_is_valid_password(self):
        self.assertTrue(len(self.password) >= 8, "La contraseña no tiene más de 8 caracteres")

    def test_upper(self):
        self.assertTrue(
            any(char.isupper() for char in self.password),
            "La contraseña no utiliza mayusculas y minusculas",
        )

    def test_digit(self):
        self.assertTrue(
            any(char.isdigit() for char in self.password),
            "La contraseña no utiliza numeros",
        )


if __name__ == "__main__":
    unittest.main()
