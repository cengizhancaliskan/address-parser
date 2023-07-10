from dataclasses import dataclass


@dataclass
class AddressModel:
    """Class for detailed address."""
    street: str
    house_number: str  # some house numbers include letter(s)

    def __str__(self):
        return f'{{"street": "{self.street}", "housenumber": "{self.house_number}"}}'
