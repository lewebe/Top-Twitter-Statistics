def top_10_hashtags(dataset):
    hashtags = {}
    for tweet in dataset:
        content = tweet['content'].split(' ')
        for word in content:
            word = word.replace('\n',"")
            if "#" in word:
                if word in hashtags:
                    hashtags[word] += 1
                else:
                    hashtags[word] = 0
    sorted_hashtags =sorted(hashtags.items(), key=lambda x: x[1], reverse=True)
    top_10_hashtags = sorted_hashtags[:10]
    return top_10_hashtags