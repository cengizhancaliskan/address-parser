import regex as re

from model import AddressModel


class AddressParser:
    regex = r"^\s*(?:(?:(?<A_Addition_to_address_1>.*?),\s*)?(?:No\.\s*)?(?<A_House_number_1>\p{N}+[a-zA-Z]?(?:\s*[-\/\p{P}]\s*\p{N}+[a-zA-Z]?)*)\s*,?\s*(?<A_Street_name_1>(?:[a-zA-Z]\s*|\p{N}\p{L}{2,}\s\p{L})\S[^,#]*?(?<!\s))\s*(?:(?:[,\/]|(?=#))\s*(?!\s*No\.)(?<A_Addition_to_address_2>(?!\s).*?))?|(?:(?<B_Addition_to_address_1>.*?),\s*(?=.*[,\/]))?(?!\s*No\.)(?<B_Street_name>\S\s*\S(?:[^,#](?!\b\p{N}+\s))*?(?<!\s))\s*[\/,]?\s*(?:\sNo\.)?\s+(?<B_House_number>\p{N}+\s*-?[a-zA-Z]?(?:\s*[-\/\p{P}]?\s*\p{N}+(?:\s*[-a-zA-Z])?)*|[IVXLCDM]+(?!.*\b\p{N}+\b))(?<!\s)\s*(?:(?:[,\/]|(?=#)|\s)\s*(?!\s*No\.)\s*(?<B_Addition_to_address_2>(?!\s).*?))?)\s*$"

    # Parse parses raw address and try to extract as street and number
    def parse(self, address: str):
        matches = re.search(self.regex, address)
        matched_address = [s for s in matches.groups() if s is not None]
        parsed_address = AddressModel("", "")
        if len(matched_address) == 2:
            if matched_address[0].isdigit():
                parsed_address = AddressModel(matched_address[1], matched_address[0])
            else:
                parsed_address = AddressModel(matched_address[0], matched_address[1])
        elif len(matched_address) > 2:
            parsed_address = AddressModel(" ".join(matched_address[0:-1]), matched_address[-1])

        return parsed_address
