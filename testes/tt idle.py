from TwitterSearch import *
try:

    ts = TwitterSearch(
        consumer_key = '5JS0MMeBCWM6jclIo1apAddGY',
        consumer_secret = 'sYpfF3tFLVQd9SgPJWbJlLaBFMKRkRH718liI6sqHReswGNB4G',
        access_token = '1317112428614832128-EFrWCZoTskTRK8FgsOs2jg2UcHLoVY',
        access_token_secret = '5ODzZF5moF2pfYftj4bsYrN0H8ESwQSC9ArUhPTITsril'
     )

    tso = TwitterSearchOrder()
    tso.set_keywords(['ignorance']) 
    tso.set_language('pt')

    for tweet in ts.search_tweets_iterable(tso):
        print(tweet['text'])

except TwitterSearchException as e:
    print(e)
