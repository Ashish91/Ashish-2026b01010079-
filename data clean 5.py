import pandas as pd
import numpy as np

# =====================================
# STEP 1: LOAD DATASET
# =====================================

df = pd.read_csv("ecommerce_customer_behavior_dataset_messy.csv")

print("Original Dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)


# =====================================
# STEP 2: UNDERSTAND DATASET
# =====================================

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# =====================================
# STEP 3: REMOVE EXTRA SPACES
# =====================================

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()


# =====================================
# STEP 4: HANDLE MISSING VALUES
# =====================================

# Convert common missing-value strings into NaN

df.replace(
    ["NAN", "nan", "None", ""],
    np.nan,
    inplace=True
)

# Remove rows without Order_ID

df.dropna(subset=["Order_ID"], inplace=True)


# =====================================
# STEP 5: REMOVE DUPLICATES
# =====================================

# Standardize IDs before checking duplicates

df["Order_ID"] = df["Order_ID"].str.upper()

df["Customer_ID"] = df["Customer_ID"].str.upper()

df.drop_duplicates(subset=["Order_ID"], inplace=True)


# =====================================
# STEP 6: CLEAN GENDER COLUMN
# =====================================

df["Gender"] = df["Gender"].str.strip().str.lower()

df["Gender"] = df["Gender"].replace({
    "m": "Male",
    "male": "Male",
    "f": "Female",
    "female": "Female"
})

df["Gender"] = df["Gender"].replace({
    "other": "Other"
})


# =====================================
# STEP 7: CLEAN CITY COLUMN
# =====================================

df["City"] = df["City"].str.strip().str.title()


# =====================================
# STEP 8: CLEAN PRODUCT CATEGORY
# =====================================

df["Product_Category"] = (
    df["Product_Category"]
    .str.strip()
    .str.title()
)


# =====================================
# STEP 9: CLEAN PAYMENT METHOD
# =====================================

df["Payment_Method"] = (
    df["Payment_Method"]
    .str.strip()
    .str.title()
)


# =====================================
# STEP 10: CLEAN DEVICE TYPE
# =====================================

df["Device_Type"] = (
    df["Device_Type"]
    .str.strip()
    .str.title()
)


# =====================================
# STEP 11: CONVERT DATE COLUMN
# =====================================

df["Date"] = pd.to_datetime(
    df["Date"],
    format="%d-%m-%Y",
    errors="coerce"
)


# =====================================
# STEP 12: CONVERT NUMERIC COLUMNS
# =====================================

numeric_columns = [
    "Age",
    "Unit_Price",
    "Quantity",
    "Discount_Amount",
    "Total_Amount",
    "Session_Duration_Minutes",
    "Pages_Viewed",
    "Delivery_Time_Days",
    "Customer_Rating"
]

for col in numeric_columns:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )


# =====================================
# STEP 13: HANDLE INVALID VALUES
# =====================================

# Invalid ages

df.loc[
    (df["Age"] < 1) | (df["Age"] > 100),
    "Age"
] = np.nan

# Invalid prices

df.loc[
    df["Unit_Price"] < 0,
    "Unit_Price"
] = np.nan

# Invalid quantities

df.loc[
    df["Quantity"] <= 0,
    "Quantity"
] = np.nan

# Invalid discount

df.loc[
    df["Discount_Amount"] < 0,
    "Discount_Amount"
] = np.nan

# Invalid customer rating

df.loc[
    ~df["Customer_Rating"].between(1, 5),
    "Customer_Rating"
] = np.nan


# =====================================
# STEP 14: FILL MISSING NUMERIC VALUES
# =====================================

for col in numeric_columns:

    df[col] = df[col].fillna(
        df[col].median()
    )


# =====================================
# STEP 15: FILL MISSING CATEGORICAL VALUES
# =====================================

categorical_columns = [
    "Customer_ID",
    "Gender",
    "City",
    "Product_Category",
    "Payment_Method",
    "Device_Type"
]

for col in categorical_columns:

    df[col] = df[col].fillna("Unknown")


# =====================================
# STEP 16: CLEAN BOOLEAN COLUMN
# =====================================

df["Is_Returning_Customer"] = (
    df["Is_Returning_Customer"]
    .astype(str)
    .str.strip()
    .str.lower()
)

df["Is_Returning_Customer"] = (
    df["Is_Returning_Customer"].replace({
        "true": True,
        "false": False
    })
)

df["Is_Returning_Customer"] = (
    df["Is_Returning_Customer"].fillna(False)
)


# =====================================
# STEP 17: FIX TOTAL AMOUNT
# =====================================

# Calculate total amount

calculated_amount = (
    df["Unit_Price"] * df["Quantity"]
    - df["Discount_Amount"]
)

# Fill missing total amounts

df["Total_Amount"] = df["Total_Amount"].fillna(
    calculated_amount
)


# =====================================
# STEP 18: FINAL DATA CLEANING
# =====================================

df.drop_duplicates(inplace=True)

df.reset_index(drop=True, inplace=True)


# =====================================
# STEP 19: CHECK CLEANED DATA
# =====================================

print("\n========== CLEANED DATA ==========")

print(df.head())

print("\nFinal Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFinal Information:")
df.info()


# =====================================
# STEP 20: SAVE CLEANED DATASET
# =====================================

df.to_csv(
    "ecommerce_customer_behavior_cleaned.csv",
    index=False
)

print("\n================================")
print("DATA CLEANING COMPLETED!")
print("Cleaned Dataset Successfully Saved!")
print("================================")