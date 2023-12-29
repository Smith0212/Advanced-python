import os
import csv
from collections import defaultdict

def read_product_names():
    product_names = {}
    with open(r"D:\\Sem-5\\adv. python\\Vipul's py\\IA ASSIGNMENT\\All Codes\\Q2\\product_names.csv", mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product_names[row['Product ID']] = row['Product Name']
    return product_names

def process_sales_data(directory):
    total_quantity_sold = defaultdict(int)
    total_months = defaultdict(int)

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                with open(os.path.join(root, file), mode='r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        product_id = row['Product ID']
                        quantity_sold = int(row['Quantity sold'])
                        total_quantity_sold[product_id] += quantity_sold
                        total_months[product_id] += 1

    return total_quantity_sold, total_months

def get_top_5_products(total_quantity_sold):
    sorted_products = sorted(total_quantity_sold.items(), key=lambda x: x[1], reverse=True)
    return sorted_products[:5]

def main():
    data_directory = r"D:\\Sem-5\\adv. python\\Vipul's py\\IA ASSIGNMENT\\All Codes\\Q2\\sales_data.csv"

    product_names = read_product_names()

    total_quantity_sold, total_months = process_sales_data(data_directory)

    top_5_products = get_top_5_products(total_quantity_sold)

    with open('sales_summary.csv', mode='w', newline='') as csvfile:
        fieldnames = ['Product ID', 'Product Name', 'Total Quantity Sold', 'Average Quantity Sold per Month']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for product_id, total_sold in top_5_products:
            product_name = product_names.get(product_id, 'Unknown')
            average_quantity_sold = total_sold / total_months[product_id]
            writer.writerow({
                'Product ID': product_id,
                'Product Name': product_name,
                'Total Quantity Sold': total_sold,
                'Average Quantity Sold per Month': average_quantity_sold
            })

if __name__ == "__main__":
    main()
