import numpy as np
import pandas as pd
import logging

# Configure the logging module
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s %(message)s')

# Function to read data from output.csv and create a DataFrame
def create_dataframe():
    try:
        df = pd.read_csv('output.csv')  # Use pd.read_csv to read CSV files
        
        # Check for valid emotions and log an error if not valid
        valid_emotions = ['Positive', 'Negative', 'Neutral']
        invalid_emotions = df[~df['Emotion'].isin(valid_emotions)]
        if not invalid_emotions.empty:
            logging.error("Invalid emotions found in DataFrame: {}".format(invalid_emotions))

        logging.info("Successfully read data from output.csv and created DataFrame.")
        # print(df)

        try:
            df['Emotion'][2] = 'Updated Emotion'  # This generates a warning
            logging.warning("Updated DataFrame directly without using iloc. Changes may not be as expected.")
            
        except Exception as e:
            logging.error(f"Error occurred while updating DataFrame: {str(e)}")

    except Exception as e:
        logging.error(f"Error reading data from CSV and creating DataFrame: {str(e)}")

    return df

# Call the function to create the DataFrame
data_frame = create_dataframe()

# Example: Print the DataFrame
if data_frame is not None:
    print(data_frame)
