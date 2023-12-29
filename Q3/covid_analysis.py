import os
import json

# Function to read COVID-19 data from JSON files
def read_covid19_data(directory):
    covid19_data = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                # print(file)
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    covid19_data.append(data)

    return covid19_data

# Function to calculate and display statistics for each country
def calculate_statistics(data):
    country_statistics = {}

    for record in data:
        country_name = record['country']
        confirmed_cases = record['confirmed_cases']['total']
        deaths = record['deaths']['total']
        recovered = record['recovered']['total']
        active_cases = confirmed_cases - deaths - recovered

        country_statistics[country_name] = {
            'Total Confirmed Cases': confirmed_cases,
            'Total Deaths': deaths,
            'Total Recovered Cases': recovered,
            'Total Active Cases': active_cases
        }

    return country_statistics

# Function to determine the top 5 countries with the highest and lowest confirmed cases
def find_top_countries(country_statistics):
    sorted_countries = sorted(country_statistics.items(), key=lambda x: x[1]['Total Confirmed Cases'], reverse=True)
    top_5_highest = sorted_countries[:5]
    top_5_lowest = sorted_countries[-5:][::-1]
    return top_5_highest, top_5_lowest

# Function to generate and save the summary report
def generate_summary_report(country_statistics, top_5_highest, top_5_lowest):
    summary_report = {
        'Country Statistics': country_statistics,
        'Top 5 Countries with Highest Confirmed Cases': {country: stats['Total Confirmed Cases'] for country, stats in top_5_highest},
        'Top 5 Countries with Lowest Confirmed Cases': {country: stats['Total Confirmed Cases'] for country, stats in top_5_lowest}
    }

    with open('covid19_summary.json', 'w') as json_file:
        json.dump(summary_report, json_file, indent=4)

def main():
    # Directory where COVID-19 data is stored
    data_directory = r"D:\Sem-5\adv. python\Vipuls py\IA ASSIGNMENT\All Codes\Q3"

    # Read COVID-19 data from JSON files
    covid19_data = read_covid19_data(data_directory)
    # print(covid19_data)
    # Calculate statistics for each country
    country_statistics = calculate_statistics(covid19_data)
    print(country_statistics)
    # Determine the top 5 countries
    top_5_highest, top_5_lowest = find_top_countries(country_statistics)

    # Generate and save the summary report
    generate_summary_report(country_statistics, top_5_highest, top_5_lowest)

if __name__ == "__main__":
    main()
