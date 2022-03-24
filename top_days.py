def top_10_days(dataset):
    dates = {}
    for tweet in dataset:
        date = tweet['date'].split('T')[0]
        if date in dates:
            dates[date] += 1
        else:
            dates[date] = 0
    sorted_dates =sorted(dates.items(), key=lambda x: x[1], reverse=True)
    top_10_days = sorted_dates[:10]
    return top_10_days