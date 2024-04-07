import pandas as pd


def process(df):
    df['start'] = pd.to_datetime(df['timestamp'], unit='s')

    df['end'] = df['start'] + pd.to_timedelta(df['billing_period'] - 1, unit='D')

    start_february = "2024-02-01"
    end_february = "2024-02-29"

    # найти кто входит в периуд
    hwo_in_periud = df[(df['start'] < pd.to_datetime(end_february)) & (df['end'] > pd.to_datetime(start_february))]

    # разница между большим левым концом и меньшим правым
    def min_rigth(x):
        return min(x, pd.to_datetime(end_february))

    def max_left(x):
        return max(x, pd.to_datetime(start_february))

    hwo_in_periud['days_in_febr'] = (hwo_in_periud['end'].map(min_rigth) - hwo_in_periud['start'].map(
        max_left)).dt.days + 1

    hwo_in_periud['pay_in_febr'] = hwo_in_periud['billing_total_price_usd'] / hwo_in_periud['billing_period'] * \
                                   hwo_in_periud['days_in_febr']

    a = hwo_in_periud[['user_id', 'pay_in_febr']].groupby('user_id').sum()['pay_in_febr']

    return a.nlargest(3).sum().round(2)