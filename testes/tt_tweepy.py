# acessar https://apps.twitter.com para criar uma nova aplicação
# cada aplicação tem suas próprias chaves

import tweepy
import re

# acessar a aba "Keys and Access Tokens"
# passa o Consumer Key e o Consumer Secret
auth = tweepy.OAuthHandler('46pvnSwIVylfWepbPsP4433wL', 'xWDPHaUkk0ub93qj1DaYgJcO8QtkPUhNFIE7uBAvzbSVLLpLzR')

# define o token de acesso
# para criar basta clicar em "Create my access token"
# passa o "Access Token" e o "Access Token Secret"
auth.set_access_token('1952916806-9WbU9ROPLd4aVPprQZqWJhaW4RSXrBw4oK8A4Ow',
		'gW5iuYPtrTxVhPmQxBemsKz6jCAOqbYx1fT0ewKHFyAkG')

# cria um objeto api
api = tweepy.API(auth)

# obtém tweets de um dado usuário
def obter_tweets(usuario, limite=10):
	resultados = api.user_timeline(screen_name=usuario, count=limite, tweet_mode='extended')
	tweets = [] # lista de tweets inicialmente vazia
	for r in resultados:
		# utiliza expressão regular para remover a URL do tweet
		# http pega o início da url
		# \S+ pega os caracteres não brancos (o final da URL) 
		tweet = re.sub(r'http\S+', '', r.full_text)
		tweets.append(tweet.replace('\n', ' ')) # adiciona na lista
	return tweets # retorna a lista de tweets

# escreve os tweets em um arquivo 'tweets.txt'
tweets = obter_tweets(usuario='jairbolsonaro', limite=100)
with open('tweets.txt', 'w') as f:
	f.write('\n'.join(tweets))
