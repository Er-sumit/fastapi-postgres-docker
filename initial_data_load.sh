curl --location 'http://localhost/account' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "title": "ICICI_5005",
    "type": "CCMAIN",
    "bank_desc": "ICICI Bank Credit Card 5005",
    "billed_due": 10000,
    "unbilled_due": 41936,
    "total_due": 51936,
    "billing_date": 20,
    "available_bal": 133000,
    "due_date": 28,
    "emi_amount": 0,
    "emi_due_count": 0
}'

curl --location 'http://localhost/account' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "id": 2,
    "title": "KOTAK_2230",
    "type": "CCMAIN",
    "bank_desc": "KOTAK Bank Credit Card 2230",
    "billed_due": 16334,
    "unbilled_due": 8504,
    "total_due": 24838,
    "billing_date": 20,
    "available_bal": 125162,
    "due_date": 12,
    "emi_amount": 0,
    "emi_due_count": 0
}'

curl --location 'http://localhost/account' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
  "title": "RENT_BLR",
  "type": "EMI",
  "bank_desc": "House Rent",
  "billed_due": 0,
  "unbilled_due": 0,
  "total_due": 0,
  "due_date": 2,
  "billing_date": 30,
  "available_bal": 0,
  "emi_amount": 30000,
  "emi_due_count": 40
}'


curl --location 'http://localhost/account' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
  "title": "KOTAK_SBA",
  "type": "SBA",
  "bank_desc": "KOTAK Bank Savings Account",
  "billed_due": 0,
  "unbilled_due": 0,
  "total_due": 0,
  "billing_date": 0,
  "available_bal": 180000,
  "due_date": 0,
  "emi_amount": 0,
  "emi_due_count": 0
}'


curl --location --request PUT 'http://localhost/account/1/activation/1' \
--header 'accept: application/json'

curl --location --request PUT 'http://localhost/account/2/activation/1' \
--header 'accept: application/json'

curl --location --request PUT 'http://localhost/account/3/activation/1' \
--header 'accept: application/json'

curl --location --request PUT 'http://localhost/account/4/activation/1' \
--header 'accept: application/json'

curl --location --request PUT 'http://localhost/account/5/activation/1' \
--header 'accept: application/json'
