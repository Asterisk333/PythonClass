import pandas as pd


# Bereinigungsfunktion
def clean_row(row):
    try:
        row["discounted_price"] = float(row["discounted_price"].replace("₹", "").replace(",", ""))
        row["actual_price"] = float(row["actual_price"].replace("₹", "").replace(",", ""))
        row["discount_percentage"] = int(row["discount_percentage"].replace("%", ""))

        # Prüfen, ob "rating" ein String ist, bevor .replace() genutzt wird
        if isinstance(row["rating"], str):
            row["rating"] = float(row["rating"].replace("|", "").strip())
        else:
            row["rating"] = float(row["rating"])  # Falls es bereits ein Float ist

        row["rating_count"] = int(row["rating_count"].replace(",", "")) if pd.notnull(row["rating_count"]) else 0
        return row
    except Exception as e:
        print(f"❌ Fehler in Zeile mit product_id {row.product_id}: {e}")
        print(row)  # Problematische Zeile ausgeben
        return None


# clean the whole data
def clean_data(df):
    return df.apply(clean_row, axis=1).dropna().reset_index(drop=True)
