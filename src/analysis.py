import os
import requests
from utils import read_csv, clean_data

def fetch_market_data(product_name):
    """Simulates fetching market data for products."""
    simulated_market_data = {
        "Organic Coffee Beans (1lb)": 12.99,
        "Premium Green Tea (50 bags)": 8.49,
        "Masala Chai Mix (12oz)": 10.49,
        "Yerba Mate Loose Leaf (1lb)": 13.49,
        "Hot Chocolate Mix (1lb)": 7.99,
        "Earl Grey Tea (100 bags)": 11.49,
        "Espresso Beans (1lb)": 16.49,
        "Chamomile Tea (30 bags)": 6.49,
        "Matcha Green Tea Powder (4oz)": 19.49,
        "Decaf Coffee Beans (1lb)": 15.49,
        "Mint Tea (25 bags)": 7.99,
        "Instant Coffee (8oz)": 11.49,
        "cold brew concentrate": 13.49,
    }
    return simulated_market_data.get(product_name, None)

def generate_insight(product_data):
    """Generates insights by comparing product prices with market prices."""
    insights = []
    for product in product_data:
        market_price = fetch_market_data(product['product_name'])
        if market_price:
            if product['our_price'] > market_price:
                insights.append(
                    f"{product['product_name']} is overpriced by ${product['our_price'] - market_price:.2f}. Consider reducing the price."
                )
            elif product['our_price'] < market_price:
                insights.append(
                    f"{product['product_name']} is underpriced by ${market_price - product['our_price']:.2f}."
                )
            else:
                insights.append(
                    f"{product['product_name']} is priced competitively at ${product['our_price']:.2f}."
                )
        else:
            insights.append(
                f"No market data available for {product['product_name']}. Cannot provide pricing insight."
            )
    return insights

def main(csv_path):
    product_data = read_csv(csv_path)
    clean_product_data = clean_data(product_data)
    insights = generate_insight(clean_product_data)

    with open('report.md', 'w') as report:
        report.write("### Insights\n")
        report.write("\n".join(insights))
        print("Report generated successfully!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python src/analysis.py data/products.csv")
    else:
        main(sys.argv[1])