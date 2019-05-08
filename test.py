from ncm import RouterConfig

# fill these in with your NCM headers
headers = {
    'X-CP-API-ID': '80780c4c',
    'X-CP-API-KEY': '0c384093805172f14a99670d96b8f190',
    'X-ECM-API-ID': 'de622bc9-3fdc-452d-88b7-4cefc1463b5b',
    'X-ECM-API-KEY': 'c1630ff4f2a0f765919bec5005e13bb90d9f7b39',
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
