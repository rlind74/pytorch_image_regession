import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('excel_files/train.xlsx', sheet_name='sheet1', header=0)
    df.to_csv(f'excel_files/train.csv', index=False)