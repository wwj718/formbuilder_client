# formbuilder_client
client for [formbuilder](https://github.com/Kinto/formbuilder)

you can use the client to [get your data back](https://github.com/Kinto/formbuilder#how-can-i-get-my-data-back)

# install
`pip install formbuilder_client`

# usage

```python
from formbuilder_client import Client
client = Client(kintoUrl="http://localhost:8888/v1/",adminToken="xxx") 
response = client.get_response()
data = response.json()
print(data)
```

about kintoUrl,userToken,adminToken,  look at [How can I get my data back?](https://github.com/Kinto/formbuilder#how-can-i-get-my-data-back)


