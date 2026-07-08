def transform_product(product_df):
    # Copy the original DataFrame
    df = product_df.copy()

    # Rename columns
    df = df.rename(columns={
        "id": "product_id",
        "title": "product_name",
        "price": "product_price",
        "category": "product_category"
    })

    # Keep only the required columns
    df = df[[
        "product_id",
        "product_name",
        "product_price",
        "product_category",
        "description"
    ]]

    # Convert price to float
    df["product_price"] = df["product_price"].astype(float)

    # Return transformed DataFrame
    return df


def transform_users(user_df):
    # Copy the original DataFrame
    df = user_df.copy()

    # name = {'firstname': ..., 'lastname': ...}
    # Extract first and last names
    df["first_name"] = df["name"].apply(lambda x: x["firstname"])
    df["last_name"] = df["name"].apply(lambda x: x["lastname"])

    # address = {'street': ..., 'city': ..., 'zipcode': ..., ...}
    # Extract address fields
    df["street"] = df["address"].apply(lambda x: x["street"])
    df["city"] = df["address"].apply(lambda x: x["city"])
    df["zipcode"] = df["address"].apply(lambda x: x["zipcode"])

    # Rename columns
    df = df.rename(columns={
        "id": "user_id",
        "email": "user_email"
    })

    # Keep only the required columns
    df = df[[
        "user_id",
        "user_email",
        "username",
        "first_name",
        "last_name",
        "street",
        "city",
        "zipcode"
    ]]

    # Return transformed DataFrame
    return df