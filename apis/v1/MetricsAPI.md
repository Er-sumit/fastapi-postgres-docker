Documentation for the APIs defined in your route_metrics.py file, along with sample `curl` commands for each endpoint:

---

## **1. Get Total Assets**
**Endpoint**: `GET /metric/assets`  
**Response Model**: `SingleMetricValue`  
**Description**: Fetches the total value of assets.

### Sample `curl` Command:
```bash
curl -X GET http://localhost:8000/metric/assets
```

### Example Response:
```json
{
  "value": 1000000
}
```

---

## **2. Get Total Liabilities**
**Endpoint**: `GET /metric/liabilities`  
**Response Model**: `SingleMetricValue`  
**Description**: Fetches the total value of liabilities.

### Sample `curl` Command:
```bash
curl -X GET http://localhost:8000/metric/liabilities
```

### Example Response:
```json
{
  "value": 500000
}
```

---

## **3. Get Asset-Liability Ratio**
**Endpoint**: `GET /metric/asset_liabilities_ratio`  
**Response Model**: `AssetLiabilityRatio`  
**Description**: Fetches the ratio of assets to liabilities, along with additional metrics.

### Sample `curl` Command:
```bash
curl -X GET http://localhost:8000/metric/asset_liabilities_ratio
```

### Example Response:
```json
{
  "value": "1000 / 500",
  "ratio": "2:1",
  "liabilities_value": 500000,
  "assets_value": 1000000,
  "metric_ratio": 2.0,
  "metric_percent": 200.0
}
```

---

## **4. Get Quarterly Liability Metrics**
**Endpoint**: `GET /metric/liabilities/qtly`  
**Response Model**: `DictMetric`  
**Description**: Fetches liability metrics for the nearest quarter.

### Sample `curl` Command:
```bash
curl -X GET http://localhost:8000/metric/liabilities/qtly
```

### Example Response:
```json
{
  "data": {
    "Q1": 100000,
    "Q2": 150000,
    "Q3": 200000,
    "Q4": 250000
  }
}
```

---

## **5. Flake8 Handler (Placeholder)**
**Endpoint**: `GET /metric/liabilities/qtlys`  
**Response Model**: None  
**Description**: Placeholder endpoint that raises an HTTP 200 OK exception.

### Sample `curl` Command:
```bash
curl -X GET http://localhost:8000/metric/liabilities/qtlys
```

### Example Response:
```json
{
  "detail": "OK"
}
```

---

### Notes:
1. Replace `http://localhost:8000` with `http://localhost` if you are running the server on port 80.
2. Ensure the database and dependencies are properly configured for the endpoints to return meaningful data.
3. The response examples are placeholders and may vary based on your actual database values.

Let me know if you need further assistance!