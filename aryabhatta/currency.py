import requests

API_URL = "https://api.freecurrencyapi.com/v1/latest"
API_KEY = "fca_live_nlmeaeqh5ssQPEycgowJ8hKr6HafgfClbZ6eK4DE"  # your key

def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    """
    Fetch live exchange rate from FreeCurrencyAPI.
    Example: get_exchange_rate("USD", "INR")
    """
    params = {
        "apikey": API_KEY,
        "base_currency": from_currency,
        "currencies": to_currency
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    return data["data"][to_currency]

def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Convert currency using live rates.
    Example: convert_currency(100, "USD", "INR")
    """
    rate = get_exchange_rate(from_currency, to_currency)
    return amount * rate

# 🧪 Example usage
if __name__ == "__main__":
    usd_to_inr = convert_currency(100, "USD", "INR")
    print(f"100 USD = {usd_to_inr:.2f} INR")

    eur_to_gbp = convert_currency(50, "EUR", "GBP")
    print(f"50 EUR = {eur_to_gbp:.2f} GBP")
