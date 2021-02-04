def seguidos_usr(usuario):
get_user_url= "https://api.twitter.com/1.1/friends/list.json?cursor=-1&skip_status=true&include_user_entities=false&screen_name="+usuario
req = oauth_req(GET_USR_URL,TOKEN_ACESSO,CHAVE_ACESSO)
return req
