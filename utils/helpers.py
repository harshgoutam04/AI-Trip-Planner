from datetime import datetime


def calculate_nights(start_date, end_date):

    if isinstance(start_date, str):
        start_date = datetime.strptime(
            start_date,
            "%Y-%m-%d"
        )

    if isinstance(end_date, str):
        end_date = datetime.strptime(
            end_date,
            "%Y-%m-%d"
        )

    return max(
        (end_date - start_date).days,
        1
    )


def parse_price(price: str):

    price = (
        price.replace("₹", "")
        .replace(",", "")
        .replace("–", "-")
        .replace("—", "-")
        .strip()
    )

    if "-" in price:
        low, high = price.split("-")
        return (int(low) + int(high)) // 2

    return int(price)