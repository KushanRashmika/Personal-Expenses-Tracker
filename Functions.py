import re

def parse_amount(text: str) -> float:
    pattern = rf"[^A-Za-z0-9{re.escape(".")}]"
    try:
        return float(re.sub(pattern, "", text))
    except ValueError:
        raise ValueError("Invalid Input")

def format_money(amount: float) -> str:
    return f"${amount:.2f}"

def is_same_month(date_a, date_b) -> bool:
    date_a = date_a.split("/")[1]
    date_b = date_b.split("/")[1]
    return date_a == date_b