import random

# List of unique names
unique_names = [
    "Alice Johnson", "Bob Smith", "Charlie Brown", "David Wilson", "Eva Davis",
    "Frank White", "Grace Adams", "Henry Lee", "Ivy Turner", "Jack Brown",
    "Karen Moore", "Leo Martinez", "Mia Clark", "Noah Taylor", "Olivia Davis",
    "Paul Anderson", "Quinn Harris", "Ruby Allen", "Samuel Hall", "Taylor Wright",
]

# List of unique reviews
unique_reviews = [
    "A small review for the audio-to-text website.",
    "Here's a brief review of the audio conversion service. I wanted to share my thoughts on this amazing tool.",
    "I wanted to share my thoughts on this amazing tool.",
    "Incredible website for audio-to-text conversion!",
    "This website makes audio summarization a breeze. This website makes audio summarization a breeze. Incredible website for audio-to-text conversion!",
    "Another unique review text goes here.",
    "This is a different review from the others.",
    "A completely new review for the website. A completely new review for the website. Another unique review text goes here.",
    "Yet another unique review to add variety.",
    "One more unique review to complete the list. One more unique review to complete the list. One more unique review to complete the list. One more unique review to complete the list.",
]

# URL photos
unique_photos = [
    'https://pbs.twimg.com/profile_images/1618293589888405515/qk2Dg9_M_400x400.jpg',
    'https://pyxis.nymag.com/v1/imgs/252/564/8b856d9ed647147de9b09b2b98fdf10e64-19-zayn-malik.rsquare.w330.jpg',
    'https://pyxis.nymag.com/v1/imgs/7b9/0c9/e39af5ad3ca943bba884a46a48716a442b-23-harry-styles.rsquare.w700.jpg',
    'https://pyxis.nymag.com/v1/imgs/f2f/831/37dc5e7979551c90fc7e0e50785525ea57-liam-payne.rsquare.h600.jpg',
    'https://i.pinimg.com/564x/1a/a3/82/1aa3827582d219565103bdfe28207222.jpg',
    'https://cdn.cliqueinc.com/posts/178729/inside-jessica-alba-closet-178729-1449259711-square.700x0c.jpg',
    'https://pyxis.nymag.com/v1/imgs/058/a62/c7d8e690f8c75ce233b87740957fb08654-17-oprahwinfrey.rsquare.w700.jpg',
    'https://i.pinimg.com/474x/dd/06/79/dd06792985078bc23cd1a67a14b476c8.jpg',
    'https://pbs.twimg.com/profile_images/1651024037034995712/qFTCCPa6_400x400.jpg',
    'https://images.ctfassets.net/1wryd5vd9xez/4DxzhQY7WFsbtTkoYntq23/a4a04701649e92a929010a6a860b66bf/https___cdn-images-1.medium.com_max_2000_1_Y6l_FDhxOI1AhjL56dHh8g.jpeg',
    'https://images.ctfassets.net/1wryd5vd9xez/6imn4PsoUBr6I9Hs8jWxk4/b28965e1afec63588266cf42ba5178ae/https___cdn-images-1.medium.com_max_2000_1_7hkI-ZKsglnbjxCRV1bMZA.png',
    'https://images.squarespace-cdn.com/content/v1/559b2478e4b05d22b1e75b2d/1545073697675-3728MXUJFYMLYOT2SKAA/Nesbit.jpg',
]

# List of social media icons
social_media_list = ['twitter', 'pinterest', 'facebook', 'linkedin', 'instagram', 'google']

# Random ratings
ratings = [3, 4, 5]

# Number of pairs you want to generate
num_pairs = 25  # You can change this number to generate more pairs if needed

# Create a list of dictionaries with random pairs of names and reviews
review_list = []
for _ in range(num_pairs):
    name = random.choice(unique_names)
    review = random.choice(unique_reviews)
    social_media = random.choice(social_media_list)
    photo = random.choice(unique_photos)
    rating = random.choice(ratings)
    pair_dict = {"name": name, "photo": photo, "review": review, "social_media": social_media, "rating": rating}
    review_list.append(pair_dict)