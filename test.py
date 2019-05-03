from ncm import NCMRouterConfig

# fill these in with your NCM headers
headers = {
    'X-CP-API-ID': 'xxxx',
    'X-CP-API-KEY': 'xxxx',
    'X-ECM-API-ID': 'xxxx',
    'X-ECM-API-KEY': 'xxxx',
    'Content-Type': 'application/json'
}

# replace this payload with whatever you want.  If you put or patch this one it should give you a 409 response.
payload = \
    {
        "configuration": [{
            "example": "this wont work because it ncm wont like it"

        },
            []
        ]
    }


# this is a test get. replace the router IDs in here with some of the router IDs in your NCM account.
NCMTesting = NCMRouterConfig(headers)
result = NCMTesting.get([1111976,695606])

print(result[1111976])
print(result[695606].content)
