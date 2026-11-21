data was taken by kaggle
project description
This project cleans a messy e-commerce customer behavior dataset and prepares it for further analysis. The dataset includes order and customer IDs, customer demographics, product categories, payment methods, device types, purchase amounts, discounts, browsing activity, delivery times, customer ratings, and returning-customer status.

The script loads the CSV file and checks its first rows, dimensions, data types, missing values, and duplicate records. It then standardizes text fields, handles missing and invalid values, converts dates and numeric columns to suitable data types, and checks the cleaned data. Finally, it saves the result as ecommerce_customer_behavior_cleaned.csv.
downland from kaagle


FUNCTIONS AND METHODS USED

This project uses Python with the pandas and NumPy libraries.

- pd.read_csv() loads the CSV dataset into a pandas DataFrame.
- df.head() displays the first rows of the dataset.
- df.shape reports the number of rows and columns.
- df.info() shows column names, data types, and non-missing value counts.
- df.isnull().sum() counts missing values in each column.
- df.duplicated() identifies duplicate rows.
- df.drop_duplicates() removes duplicate records.
- df.select_dtypes() selects text columns for cleaning.
- .str.strip() removes extra spaces from text.
- .str.lower() converts text to lowercase.
- .str.title() standardizes capitalization in names and categories.
- df.replace() replaces inconsistent missing-value labels and standardizes category values.
- df.dropna(subset=["Order_ID"]) removes records without an order ID.
- pd.to_datetime() converts the Date column to a date format. Invalid dates become missing values.
- pd.to_numeric() converts selected columns to numbers. Invalid entries become missing values.
- df.loc[] identifies values that break the project’s rules, such as ages outside 1 to 100 or ratings outside 1 to 5.
- .between() checks whether values fall within a specified range.
- .fillna() fills missing numeric values with the column median and categorical values with "Unknown".
- .astype(str) temporarily converts the returning-customer values to text for standardization.
- df.reset_index(drop=True) resets the row index after cleaning.
- df.to_csv() saves the cleaned data to a new CSV file.
- np.nan represents missing or invalid values.


PLATFORMS AND TOOLS

The code is written in Python. It uses pandas to load, clean, and transform tabular data, and NumPy to represent missing values. It reads and writes CSV files.

The script does not identify the platform used to run it. It could be run in Google Colab, Jupyter Notebook, or a local Python environment, but the code alone does not confirm that Google Colab was used.


MOTIVE FOR EXPLORATORY DATA ANALYSIS

The initial dataset checks support exploratory data analysis (EDA) by showing the dataset’s size, structure, data types, missing values, and duplicate records. These checks help identify data quality issues before studying customer behavior.

Cleaning makes later analysis more reliable. Once categories are consistent and dates and numeric values are usable, the data can help answer questions such as:

- Which product categories are purchased most often?
- How do orders vary by city or device type?
- How are discounts related to spending?
- How do returning customers behave?

This script prepares the dataset for EDA. It does not itself calculate these trends or create charts.
