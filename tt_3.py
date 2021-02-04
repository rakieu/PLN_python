#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import tweepy
 
# Pegando a consulta por parâmetro
consulta = sys.argv[1:]
 
#Autenticações
consumer_key = '5JS0MMeBCWM6jclIo1apAddGY'
consumer_secret = 'sYpfF3tFLVQd9SgPJWbJlLaBFMKRkRH718liI6sqHReswGNB4G'
access_token = '1317112428614832128-EFrWCZoTskTRK8FgsOs2jg2UcHLoVY'
access_token_secret = '5ODzZF5moF2pfYftj4bsYrN0H8ESwQSC9ArUhPTITsril'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
#Coletando tweets
class CustomStreamListener(tweepy.StreamListener):
 
  def on_status(self, tweet):
    #Quando receber algum status, esta função pode manipular o objeto tweet. Exemplos:
    print (tweet.author.screen_name)
    print (tweet.text.encode('utf-8'))
    api.create_favorite(tweet.id)
 
    return True
 
  def on_error(self, status_code):
      print ("Erro com o código:", status_code)
      return True # Não mata o coletor
 
  def on_timeout(self):
      print ("Tempo esgotado!")
      return True # Não mata o coletor
 
#Criando o coletor com timeout de 60 seg
streaming_api = tweepy.streaming.Stream(auth, CustomStreamListener(), timeout=60)
streaming_api.filter(follow=None, track=consulta, languages=["pt"])