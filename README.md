# 10EQS Evaluation

## Project Overview

This project helps a small business owner track their product pricing against market conditions. The tool processes product data, integrates market data from an external source, and generates actionable insights.
## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd 10eqs-evaluation
2. **Install dependencies**:  
   Make sure you have Python installed (version 3.7 or higher). Then, run:  
   ```bash
   pip install -r requirements.txt
3. **Set up environment variables**:  
   - Copy the `.env.example` file to `.env`:  
     ```bash
     cp .env.example .env
     ```  
   - Open the `.env` file and add any necessary API keys (if applicable).
4. **Run the analysis**:  
   To process the data and generate insights, execute:  
   ```bash
   python src/analysis.py data/products.csv
## Output

- **`report.md`**: This file is generated automatically and contains the insights from the data analysis. It includes:
  - Products that are overpriced or underpriced compared to the market.
  - Recommendations for price adjustments.
## Example of `report.md`

The `report.md` file is automatically created and provides insights like:

### Insights

- Organic Coffee Beans (1lb) is overpriced by $2.00. Consider reducing the price.
- Premium Green Tea (50 bags) is overpriced by $0.50. Consider reducing the price.
- Masala Chai Mix (12oz) is underpriced by $0.50.
- Yerba Mate Loose Leaf (1lb) is underpriced by $0.50.
- Hot Chocolate Mix (1lb) is priced competitively at $7.99.
- Earl Grey Tea (100 bags) is overpriced by $0.50. Consider reducing the price.
- Espresso Beans (1lb) is overpriced by $0.50. Consider reducing the price.
- Chamomile Tea (30 bags) is overpriced by $0.50. Consider reducing the price.
- Matcha Green Tea Powder (4oz) is overpriced by $0.50. Consider reducing the price.
- Decaf Coffee Beans (1lb) is overpriced by $0.50. Consider reducing the price.
- Mint Tea (25 bags) is underpriced by $0.50.
- Instant Coffee (8oz) is overpriced by $0.50. Consider reducing the price.
- cold brew concentrate is overpriced by $0.50. Consider reducing the price.
## Known Issues

- The tool assumes all product names in the external API match exactly with the CSV data.
- The external data source must provide prices in the same currency as the `products.csv`.
## External Data Source

The tool uses the **OpenFoodFacts API** to fetch product pricing data. For more details, visit [OpenFoodFacts API documentation](https://world.openfoodfacts.org/data).

## Time Spent

- Setting up the project: 10 minutes
- Writing the utility functions: 15 minutes
- Integrating external data: 15 minutes
- Testing and debugging: 10 minutes
- Documentation: 10 minutes
- **Total: 60 minutes**
