def infer_email(name, company):
    """
    Infer a realistic business email format.
    Example: Sarah Kim @ NeoLiver Bio → sarah.kim@neoliverbio.com
    """
    first, last = name.lower().split(" ")[:2]
    domain = company.lower().replace(" ", "").replace(",", "")
    return f"{first}.{last}@{domain}.com"


def enrich_leads(df):
    """
    Enrich raw leads with inferred emails
    and normalized location fields.
    """

    # Infer emails
    df["Email"] = df.apply(
        lambda row: infer_email(row["Name"], row["Company"]),
        axis=1
    )

    # Normalize person vs HQ location
    df["Is_Remote"] = df["Person_Location"].str.contains("Remote")

    return df
