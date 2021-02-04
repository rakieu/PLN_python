import tweepy
api_key = "5JS0MMeBCWM6jclIo1apAddGY"
api_secret_key = "sYpfF3tFLVQd9SgPJWbJlLaBFMKRkRH718liI6sqHReswGNB4G"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIR%2FJgEAAAAAu5CMnVwLnEbKg1qMsVSC6QVJN7Y%3DCgyGXUkVfV2xifzG9Wb9BMOi2UIEXv3lvkvxZAuhOvYxTMEoNc"
access_token = "1317112428614832128-EFrWCZoTskTRK8FgsOs2jg2UcHLoVY"
access_token_secret = "5ODzZF5moF2pfYftj4bsYrN0H8ESwQSC9ArUhPTITsril"

autenticacao = tweepy.OAuthHandler(api_key, api_secret_key)
autenticacao.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(autenticacao)


twitter.search(q='map_usp')
resultados = twitter.search(q='map_usp')

for tweet in resultados:
     print(f'Usuário: {tweet.user.screen_name} - Tweet: {tweet.text}')
