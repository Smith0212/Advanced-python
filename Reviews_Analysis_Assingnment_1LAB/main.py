import os
import re
import pandas as pd
import numpy as np

valid_review_count = 0
invalid_review_count = 0

def extract_info_from_review_text(review_text):
    #creating pattern to match the review text in the file
    pattern = r"Customer ID: (\w+)\nProduct ID: (\w+)\nReview date: (\d{4}-\d{2}-\d{2})\nReview rating: (\d)\nReview text: (.+)"
    #using search function of re module to match the pattern and storing the matching text of regular expression to match var in sequence.
    match = re.search(pattern, review_text)
    if match:
        customer_id, product_id, review_date, rating, review_text = match.groups() #store the matching text in sequence.
        #returning the list of matching text
        return [
            customer_id,
            product_id,
            review_date,
            int(rating),
            review_text
        ]
    else:
        return None

def main():
    
    valid_review_count = 0
    invalid_review_count = 0

    #making to forme DataFrame
    all_reviews = {
        'CustomerID': [],
        'ProductID': [],
        'ReviewDate': [],
        'Rating': [],
        'ReviewText': []
    }

    #scanning all files in review_folder
    for filename in os.listdir("review_folder"):
        if filename.endswith(".txt"):
            with open(os.path.join("review_folder", filename), 'r') as file:
                reviews = file.read()

            # print(reviews)  
            #storing list written by extract_info_from_review_text function
            review_info = extract_info_from_review_text(reviews)
            # print(review_info)

            #if the review is not matching the pattern 
            if review_info == None:
                invalid_review_count += 1
                print("Invalid review!")

            #if the review is matching the pattern#
            #appending the list elements to the dictionary
            if review_info :
                valid_review_count += 1
                all_reviews['CustomerID'].append(review_info[0])
                all_reviews['ProductID'].append(review_info[1])
                all_reviews['ReviewDate'].append(review_info[2])
                all_reviews['Rating'].append(review_info[3])
                all_reviews['ReviewText'].append(review_info[4])
    
    #making DataFrame from dictionary
    df = pd.DataFrame(all_reviews)
    print(df)

    print("\n")
    
    #calculating average ratings by using groupby function o/p is in series format
    avg_ratings = df.groupby('ProductID')['Rating'].mean()
    print(avg_ratings)

    print("\n")

    #converting series to dictionary using to_dict function of pandas
    avg_ratings_dict = avg_ratings.to_dict()
    print(avg_ratings_dict)

    print("\n")

    #sorting the dictionary by using sorted function of python
    sorted_ratings = sorted(avg_ratings_dict.items(), key = lambda item : item[1], reverse = True)
    #displaying top 3 products with highest average ratings
    top_3_ratings = sorted_ratings[:3]
    print(top_3_ratings)
    
    #writing the output to source.txt file
    with open("source.txt", "w") as f:
        f.write("Total number of reviews scan :" + str(len(df)) + "\n")
        f.write("Total number of valid reviews :" + str(valid_review_count) + "\n")
        f.write("Total number of invalid reviews :" + str(invalid_review_count) + "\n")
        f.write("Top 3 products with highest average ratings :" + str(top_3_ratings) + "\n")

if __name__ == "__main__":
    main()
