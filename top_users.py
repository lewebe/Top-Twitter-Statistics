def top_10_twitter_users(dataset):
    users = {}
    for tweet in dataset:
        user = tweet['user']['username']
        if user in users:
            users[user] += 1
        else:
            users[user] = 0
    sorted_users =sorted(users.items(), key=lambda x: x[1], reverse=True)
    top_10_users = sorted_users[:10]
    return top_10_users