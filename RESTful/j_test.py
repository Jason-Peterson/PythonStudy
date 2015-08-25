# __author__ = 'Jason'

# oauth_redirect_uri = []
# redirect_uri = 'http://localhost:5000/helloworld'
# oauth_redirect_uri.append(redirect_uri)
# print oauth_redirect_uri
j_dict = {
    'kk': 1234
}
j_dict['jason'] = 'hello'
print j_dict.get('jason')
print j_dict
j_dict.pop('kk')
print j_dict