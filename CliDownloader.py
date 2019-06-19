import os
import requests
from requests.packages.urllib3.util.retry

import tqdm from tqdm, trange
url = input("Enter The Downloading URL of the file")
r = requests.get(url, stream = True)
chunk_size = 256
total_size = int(r.headers['Content-Length']) //256
