import pandas as pd

def daily_sales(transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions.copy()
    df["date"] = df["datetime"].dt.date

    out = (
        df.groupby("date", as_index=False)
          .agg(
              transactions=("transaction_id", "nunique"),
              net_sales_vnd=("net_amount_vnd", "sum"),
              gross_profit_vnd=("gross_profit_vnd", "sum"),
              avg_basket_qty=("basket_qty", "mean"),
          )
    )
    out["gross_margin"] = out["gross_profit_vnd"] / out["net_sales_vnd"]
    return out.sort_values("date")


def peak_hours(transactions: pd.DataFrame, stores: pd.DataFrame) -> pd.DataFrame:
    df = transactions.merge(stores[["store_id", "area_type"]], on="store_id", how="left")

    out = (
        df.groupby(["area_type", "hour"], as_index=False)
          .agg(
              transactions=("transaction_id", "nunique"),
              net_sales_vnd=("net_amount_vnd", "sum"),
              avg_basket_qty=("basket_qty", "mean"),
          )
          .sort_values(["area_type", "net_sales_vnd"], ascending=[True, False])
    )
    return out


def category_mix(lines: pd.DataFrame) -> pd.DataFrame:
    out = (
        lines.groupby("category", as_index=False)
             .agg(
                 net_sales_vnd=("net_amount_vnd", "sum"),
                 gross_profit_vnd=("gross_profit_vnd", "sum"),
                 qty=("quantity", "sum"),
             )
    )
    out["gross_margin"] = out["gross_profit_vnd"] / out["net_sales_vnd"]
    return out.sort_values("net_sales_vnd", ascending=False)


def promo_impact(transactions: pd.DataFrame) -> pd.DataFrame:
    out = (
        transactions.groupby("promo_type", as_index=False)
                    .agg(
                        transactions=("transaction_id", "nunique"),
                        avg_basket_qty=("basket_qty", "mean"),
                        avg_net_sales_vnd=("net_amount_vnd", "mean"),
                        avg_profit_vnd=("gross_profit_vnd", "mean"),
                    )
                    .sort_values("transactions", ascending=False)
    )
    out["avg_margin"] = out["avg_profit_vnd"] / out["avg_net_sales_vnd"]
    return out
