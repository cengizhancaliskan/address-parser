from unittest import TestCase

from address_parser import AddressParser


class AddressParserTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(AddressParserTest, self).__init__(*args, **kwargs)
        self.address_parser = AddressParser()

    def parses_address_data(self, test_data):
        for input, expected in test_data:
            self.assertEqual(
                expected,
                str(self.address_parser.parse(input))
            )

    def test_simple_cases(self):
        test_data = (
            ('Winterallee 3', f'{{"street": "Winterallee", "housenumber": "3"}}'),
            ('Musterstrasse 45', f'{{"street": "Musterstrasse", "housenumber": "45"}}'),
            ('Blaufeldweg 123B', f'{{"street": "Blaufeldweg", "housenumber": "123B"}}'),
        )
        self.parses_address_data(test_data)

    def test_complicated_cases(self):
        test_data = (
            ('Am Bächle 23', f'{{"street": "Am Bächle", "housenumber": "23"}}'),
            ('Auf der Vogelwiese 23 b', f'{{"street": "Auf der Vogelwiese", "housenumber": "23 b"}}'),
        )
        self.parses_address_data(test_data)

    def test_complex_cases(self):
        test_data = (
            ('4, rue de la revolution', f'{{"street": "rue de la revolution", "housenumber": "4"}}'),
            ('200 Broadway Av', f'{{"street": "Broadway Av", "housenumber": "200"}}'),
            ('Calle Aduana, 29', f'{{"street": "Calle Aduana", "housenumber": "29"}}'),
            ('Calle 39 No 1540', f'{{"street": "Calle 39", "housenumber": "No 1540"}}'),
        )
        self.parses_address_data(test_data)


if __name__ == '__main__':
    unittest.main()
