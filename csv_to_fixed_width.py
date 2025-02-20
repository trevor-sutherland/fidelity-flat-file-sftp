import pandas as pd

def csv_to_fixed_width(input_csv, output_file, column_widths):
    # Read the CSV into a DataFrame
    df = pd.read_csv(input_csv)

    # Open the output file to write the fixed-width lines
    with open(output_file, 'w') as file:
        # Loop through each row in the dataframe
        for _, row in df.iterrows():
            fixed_width_line = ""
            
            # For each column, format it to fit the defined width
            for col, width in zip(df.columns, column_widths):
                value = str(row[col]).strip()
                fixed_width_line += value.ljust(width)[:width]  # Pad or truncate the value
            file.write(fixed_width_line + '\n')

# Example usage
column_widths = [10, 15, 5]  # Define width for each column
csv_to_fixed_width('input.csv', 'output.txt', column_widths)
