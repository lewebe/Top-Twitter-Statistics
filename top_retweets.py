def top_10_retweeted_tweets(dataset):
    sorted_dataset = sorted(dataset, key=lambda d: d['retweetCount'], reverse=True)
    top_10_tweets = []
    for i in range(0,10):
        top_10_tweets.append(sorted_dataset[i]['content'])
    return top_10_tweets