# Local Gateway

## How to use
1. Install the project requirements with `pip install -r requirements.txt`
2. Create a json file like this model:
```
[
    {
        "route_prefix": "/some_route*",
        "destination_host": "http://127.0.0.1:3001"
    },
    {
        "route_prefix": "/another_route*",
        "destination_host": "http://127.0.0.1:3002"
    },
    ...
    {
        "route_prefix": "*",
        "destination_host": "https://www.google.com"
    }
]
```
- The ordering of the routes matter, it will try to match the ones in the top first
- The slice of the route captured by the wildcard (*) will be appended at the end of the "destination_host" to make the request

3. Run `python main.py {your config file path}` in the terminal
