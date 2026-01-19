SYMBOLS = {
    "&laquo;": "«",
    "&raquo;": "»",
    "&bull;": "•",
    "&nbsp;": " ",
    "&mdash;": "—",
}


def replace_symbols(text: str) -> str:
    for symbol, replace in SYMBOLS.items():
        text = text.replace(symbol, replace)
    return text
