text ="""
Customer ID: ABC123
Product ID: JKL98765
Review date: 2023-07-15
Review rating: 4
Review text: "I really liked this product! It met my expectations and was delivered on time. The only reason I'm giving it 4 stars instead of 5 is that the packaging was slightly damaged."

 
Customer ID: DEF456
Product ID: VWX54321
Review date: 2023-06-10
Review rating: 5
Review text: "Wow, this product is amazing! It's exactly what I needed. I've been using it for a week, and it works flawlessly. Highly recommended!"

Customer ID: GHI789
Product ID: XYZ98765
Review date: 2023-08-01
Review rating: 3
Review text: "The product quality is decent, but I had some issues with the delivery. It arrived a day later than expected, and the customer service response was slow."

Customer ID: JKL321
Product ID: JKL98765
Review date: 2023-07-25
Review rating: 5
Review text: "Excellent product! It's worth every penny. The customer support team was also very helpful in answering my queries. Thumbs up!"

Customer ID: MNO654
Product ID: VWX54321
Review date: 2023-05-12
Review rating: 2
Review text: "Unfortunately, this product didn't meet my expectations. It stopped working after a week of use. Disappointed with the quality."

Customer ID: PQR987
Product ID: JKL98765
Review date: 2023-04-03
Review rating: 4
Review text: "Overall, a good purchase. The product is effective, but the user manual could be more detailed. It took some trial and error to set it up correctly."

Customer ID: STU234
Product ID: XYZ98765
Review date: 2023-03-20
Review rating: 5
Review text: "I'm impressed with this product! It exceeded my expectations. The design is sleek, and it works like a charm. I would buy it again."

Customer ID: VWX876
Product ID: XYZ98765
Review date: 2023-02-18
Review rating: 3
Review text: "It's an average product. Nothing too special about it. It does the job, but I've seen similar products with more features for the same price."

Customer ID: YZA543
Product ID: JKL98765
Review date: 2023-01-05
Review rating: 1
Review text: "Do not recommend! This product broke after only a few days of use. Waste of money."

Customer ID: BCD678
Product ID: VWX54321
Review date: 2023-08-04
Review rating: 5
Review text: "Absolutely love it! This product is fantastic. It's easy to use, and the results are outstanding. I can't imagine my life without it now!"

Product ID: XYZ987
Review date: 2023-08-04
Review rating: 5
Review text: This product is great!

Customer ID: ABC123
Review date: 2023-08-04
Review rating: 5
Review text: This product is great!

Customer ID: ABC123
Product ID: XYZ987
Review date: 08/04/2023
Review rating: 5
Review text: This product is great!

Customer ID: ABC123
Product ID: XYZ987
Review date: 2023-08-04
Review text: This product is great!
"""
texts = text.split("\n\n")
for i in range(len(texts)):
    with open(f"review_folder/review{i}.txt", "w") as f:
        f.write(texts[i].strip())