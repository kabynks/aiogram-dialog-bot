import pandas as pd

### Обработка признаков, будет изменена по условия хакатона
def features(df:pd.DataFrame) -> pd.DataFrame:
    df = df[df.columns[:-1]]
    return df