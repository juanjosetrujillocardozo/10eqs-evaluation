import csv

def read_csv(file_path):
    """Reads a CSV file and returns a list of dictionaries."""
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def clean_data(data):
    """Cleans the product data and fixes quality issues."""
    for item in data:
        # Convert price to float, handle missing or malformed values
        try:
            item['our_price'] = float(item['our_price'].replace('$', '')) if item['our_price'] else None
        except ValueError:
            item['our_price'] = None

        # Convert stock to integer or handle 'out of stock'
        if isinstance(item['current_stock'], str) and item['current_stock'].lower() == 'out of stock':
            item['current_stock'] = 0
        elif item['current_stock']:
            try:
                item['current_stock'] = int(item['current_stock'])
            except ValueError:
                item['current_stock'] = 0
    return data
