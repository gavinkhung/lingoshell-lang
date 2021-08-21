import importlib.resources
import json

try:
    with importlib.resources.open_text("lingoshell", "keywords.json") as f:
        KEYWORDS = json.load(f)
except Exception:
    print("Runtime Error: Could not find saved languages. Will use EN.")
    KEYWORDS = [
        "VAR",
        "AND",
        "OR",
        "NOT",
        "IF",
        "ELIF",
        "ELSE",
        "FOR",
        "TO",
        "STEP",
        "WHILE",
        "METHOD",
        "THEN",
        "END",
        "RETURN",
        "CONTINUE",
        "BREAK",
    ]

try:
    with importlib.resources.open_text("lingoshell", "language_keywords.json") as f:
        LANGUAGE_KEYWORDS = json.load(f)
except Exception:
    print("Runtime Error: Could not find saved languages. Will use EN.")
    LANGUAGE_KEYWORDS = {
        "en": {
            "VAR": "VAR",
            "AND": "AND",
            "OR": "OR",
            "NOT": "NOT",
            "IF": "IF",
            "ELIF": "ELIF",
            "ELSE": "ELSE",
            "FOR": "FOR",
            "TO": "TO",
            "STEP": "STEP",
            "WHILE": "WHILE",
            "METHOD": "METHOD",
            "THEN": "THEN",
            "END": "END",
            "RETURN": "RETURN",
            "CONTINUE": "CONTINUE",
            "BREAK": "BREAK",
        }
    }


def translate_file(filename, output_filename, base_language, target_language):
    with open(filename, "r") as file:
        text = file.read()
    if len(text) == 0:
        print(f'RUNTIME ERROR: file "{filename}" is empty')
        return

    base_language_keywords = LANGUAGE_KEYWORDS[base_language]
    target_language_keywords = LANGUAGE_KEYWORDS[target_language] 

    for base_language_key in base_language_keywords:
        text = text.replace(base_language_keywords[base_language_key], target_language_keywords[base_language_key])

    with open(output_filename, 'a+') as f:
        f.write(text)
        print(text)
    