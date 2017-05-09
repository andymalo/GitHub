"""
Test d'utilisation d'Elastic Search avec Python
"""

import requests
res = requests.get('http://localhost:9200')
print(res.content)