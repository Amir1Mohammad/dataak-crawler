import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


url = "http://forum.dataak.com/member.php"

#cookies = {'mybbuser': '2_b9uUv4HxuJEqmUp5XDzVmvVdpwBTBMUmw7cAscxZJOQwSbk4Sm',
#           'mybb[lastactive]': '1e3c9981d12973456c4c5d5aa4886c17',
#           'mybb[lastvisit]': '1616797043',
#           'mybblang': 'persian',
#           'loginattempts': '1'
#           }

payload = {}

USERNAME = os.getenv('username')
PASSWORD = os.getenv('password')

