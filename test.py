from ncm import RouterConfig

# fill these in with your NCM headers
headers = {
    'X-CP-API-ID': 'your cp api id here',
    'X-CP-API-KEY': 'your cp api key here',
    'X-ECM-API-ID': 'your ecm api id here',
    'X-ECM-API-KEY': 'your ecm api key here',
    'Content-Type': 'application/json'
}

# replace this payload with whatever you want.  If you put or patch this one it should give you a 409 response.
payload = \
    {
        "configuration": [{
            "example": "this wont work because ncm wont like it"

        },
            []
        ]
    }


# this is a test get. replace the router IDs in here with some of the router IDs in your NCM account.
NCMTesting = RouterConfig(headers)
result = NCMTesting.get([1111976,695606])

print(result[1111976])
print(result[695606].content)
