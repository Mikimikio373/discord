import sys
import os
from discordwebhook import Discord
import yaml

with open('userID.yml', 'rb') as f:
    param = yaml.safe_load(f)

if not os.path.exists('url.yml'):
    sys.exit('threre in no file : \"url.yml\"\nplease ask developer')
with open('url.yml', 'rb') as f:
    yml_url = yaml.safe_load(f)
url = yml_url['url']

post_text = ''
opt1 = 0
usr_name = ''
if len(sys.argv) == 2:
    post_text = sys.argv[1]
elif len(sys.argv) == 4:
    post_text = sys.argv[1]
    if not sys.argv[2] == '-user':
        sys.exit('usage : text [option]\n\t-user username')
    opt1 = 1
    usr_name = sys.argv[3]
else:
    sys.exit('usage : text [option]\n\t-user username')



if opt1 == 1:
    if not usr_name in param:
        print('user name error. all user list bellow')
        for out in param.keys():
            print(out)
        sys.exit()

if opt1 == 1:
    post = '<@{}> \n {}'.format(param[usr_name], post_text)
else:
    post = post_text
discord = Discord(url=url)
discord.post(content=post)
