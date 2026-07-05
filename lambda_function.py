import json
import boto3
import urllib.request
import os
from datetime import datetime

# AWS Clients
s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

# Environment Variables
API_KEY = os.environ["API_KEY"]
BUCKET_NAME = os.environ["BUCKET_NAME"]
TABLE_NAME = os.environ["TABLE_NAME"]

table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):

    city = "Delhi"

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = urllib.request.urlopen(url)

    weather = json.loads(response.read().decode("utf-8"))

    # Save Raw JSON to S3
    filename = f"raw/weather_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=json.dumps(weather, indent=4),
        ContentType="application/json"
    )

    # Transform Data
    item = {
        "record_id": datetime.utcnow().strftime("%Y%m%d%H%M%S"),
        "city": weather["name"],
        "temperature": str(weather["main"]["temp"]),
        "humidity": str(weather["main"]["humidity"]),
        "weather": weather["weather"][0]["main"],
        "status": "Hot" if weather["main"]["temp"] >= 35 else "Normal",
        "processed_time": datetime.utcnow().isoformat()
    }

    # Load into DynamoDB
    table.put_item(Item=item)

    print("ETL Completed Successfully")
    print(item)

    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }