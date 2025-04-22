import re

class UKPostcodeValidator:
    """
    A class to validate and format UK postcodes according to Royal Mail rules.
    """

    POSTCODE_REGEX = re.compile(
        r'^(GIR 0AA|'
        r'(?:(?:[A-PR-UWYZ][0-9][0-9]?|'
        r'[A-PR-UWYZ][A-HK-Y][0-9][0-9]?|'
        r'[A-PR-UWYZ][0-9][A-HJKPSTUW]|'
        r'[A-PR-UWYZ][A-HK-Y][0-9][ABEHMNPRVWXY]))\s?[0-9][ABD-HJLNP-UW-Z]{2})$',
        re.IGNORECASE
    )

    @staticmethod
    def is_valid(postcode: str) -> bool:
        normalized = UKPostcodeValidator._normalize(postcode)
        return bool(UKPostcodeValidator.POSTCODE_REGEX.fullmatch(normalized))

    @staticmethod
    def format(postcode: str) -> str:
        normalized = UKPostcodeValidator._normalize(postcode)
        if not UKPostcodeValidator.is_valid(normalized):
            raise ValueError(f"Invalid UK postcode: {postcode}")
        return f"{normalized[:-3]} {normalized[-3:]}".upper()

    @staticmethod
    def _normalize(postcode: str) -> str:
        return postcode.replace(" ", "").strip().upper()
