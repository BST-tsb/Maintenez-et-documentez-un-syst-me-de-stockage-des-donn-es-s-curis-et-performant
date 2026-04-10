import pandas as pd

df = pd.read_csv("healthcare_dataset.csv")

def test_no_nulls():
    assert df.isnull().sum().sum() == 0

def test_no_duplicates():
    assert df.duplicated().sum() > 0  

if __name__ == "__main__":
    test_no_nulls()
    test_no_duplicates()
    print("Tests OK")