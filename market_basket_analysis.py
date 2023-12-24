
import pandas as pd

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

# Group data by 'Member_number' and 'Date'
file_path = '/Users/sameedahmed/Documents/Market Basket Analysis/Groceries_dataset.csv'
groceries_data = pd.read_csv(file_path)
grouped_data = groceries_data.groupby(['Member_number', 'Date'])['itemDescription'].apply(list)

print(groceries_data.head())


# List of transactions
transactions = grouped_data.tolist()

# Initializing TransactionEncoder
encoder = TransactionEncoder()
transactions_encoded = encoder.fit(transactions).transform(transactions)

# Converting to a DataFrame for Apriori Algorithm
df_transactions = pd.DataFrame(transactions_encoded, columns=encoder.columns_)

# Applying Apriori Algorithm to find frequent itemsets with a minimum support threshold (e.g., 0.01)
frequent_itemsets = apriori(df_transactions, min_support=0.01, use_colnames=True)

# Output the first few frequent itemsets
print(frequent_itemsets.head())