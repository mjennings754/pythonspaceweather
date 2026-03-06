<h2>pythonspaceweather</h2>
<h3>Usage</h3>
<p>An API key is needed to use the API, you can get it from: <a href="https://sws-data.sws.bom.gov.au/register">BOM API REGISTER</a></p>

```
api_key = os.getenv("API_KEY")


def get_k_index():
    request_type = "get-k-index"
    url = f"https://sws-data.sws.bom.gov.au/api/v1/{request_type}"
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    requestBody = {
        'api_key': api_key,
```
<h3>Output</h3>

```
K Index (geomagnetic activity (short-term)): 0 (Very quiet)
Valid time: 2026-03-06 09:00:00
A Index (geomagnetic activity (long-term)): 2 (Quiet)
Valid time: 2026-03-05 00:00:00
```

<p>Feel free to add any suggestions/improvements through a PR</p>