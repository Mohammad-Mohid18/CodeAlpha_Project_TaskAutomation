import pandas as pd
import statistics
from datetime import datetime


def display_menu():
    print("\n" + "=" * 50)
    print("📊 CSV DATA CLEANER".center(50))
    print("=" * 50)
    print(" 1. Fill empty cells with mean")
    print(" 2. Fill empty cells with median")
    print(" 3. Fill empty cells with mode")
    print(" 4. Exit")
    print("=" * 50)
    choice = input(" Choose your option (1-4): ")
    return choice

def read_csv(filename):
    return pd.read_csv(filename)

def save_csv(filename, data):
    data.to_csv(filename, index=False)

def main():
    print("\n" + "✨ CSV DATA CLEANER AUTOMATION ✨".center(60))
    filename = input("\n Enter CSV filename (e.g., data.csv): ").strip()

    try:
        df = read_csv(filename)
    except FileNotFoundError:
        print("\n ⚠️  File not found. Please try again.")
        return

    while True:
        if df.isnull().sum().sum() == 0:
            print("\n ✅ No empty cells found in the file!")
            break

        print(f"\n Found {df.isnull().sum().sum()} empty cells to fill")
        choice = display_menu()

        filled = False

        for cols in df.columns:
            if df[cols].dtype in ['float64', 'int64']:
                if choice == '1':
                    df[cols].fillna(df[cols].mean(), inplace=True)
                    filled = True
                elif choice == '2':
                    df[cols].fillna(df[cols].median(), inplace=True)
                    filled = True
                elif choice == '3':
                    mode = df[cols].mode()[0]
                    df[cols].fillna(mode, inplace=True)
                    filled = True
                elif choice == '4':
                    print("\n" + "=" * 50)
                    print(" Operation cancelled ".center(50))
                    print("=" * 50)
                    return
                else:
                    print("\n ⚠️  Invalid choice. Please try again.")
                    continue

        if filled:
            print("\n ✅ Filled empty cells successfully!")

        output_filename = f"cleaned_{datetime.now().strftime('%Y%m%d_%H%M')}_{filename}"
        save_csv(output_filename, df)
        print(f"\n 💾 Saved cleaned file as: {output_filename}")
        print("=" * 50)
        break


main()
