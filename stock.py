# Import necessary libraries
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
import datetime

# Prompt the user for stock tickers and date range
tickers = input("Enter a list of stock tickers, separated by commas (e.g. MSFT, AAPL, GOOG): ")
tickers = tickers.split(",")
start_date = input("Enter the start date for the data (e.g. 2015-01-01): ")
end_date = input("Enter the end date for the data (leave blank for current date): ")

# If the end date is not specified, use the current date
if not end_date:
    end_date = datetime.datetime.now().strftime("%Y-%m-%d")

# Retrieve stock data from Yahoo Finance
data = {}
for ticker in tickers:
    stock = yf.Ticker(ticker)
    data[ticker] = stock.history(start=start_date, end=end_date)

# Create a line graph showing the closing price over time for each stock
sns.lineplot(x="Date", y="Close", data=data[tickers[0]])
for ticker in tickers[1:]:
    sns.lineplot(x="Date", y="Close", data=data[ticker])

# Add a legend and title to the graph
plt.legend(tickers)
plt.title("Stock Performance Comparison")
plt.show()

# Print summary statistics for each stock
for ticker in tickers:
    df = data[ticker]
    print("-------------------------------------------------")
    print("Statistics for {}:".format(ticker))
    print("  Mean closing price: {:.2f}".format(df["Close"].mean()))
    print("  Standard deviation: {:.2f}".format(df["Close"].std()))
    print("  Maximum closing price: {:.2f}".format(df["Close"].max()))
    print("  Minimum closing price: {:.2f}".format(df["Close"].min()))