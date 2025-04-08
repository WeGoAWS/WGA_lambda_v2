import json
import os
import requests


NOVA_ENDPOINT = "모델 endpoint" # https://bedrock-runtime.{region}.amazonaws.com/model/anthropic.claude-3-sonnet-20240229/invoke
REGION = os.environ.get("AWS_REGION", "us-west-1")

headers = {
    "Content-Type": "application/json",
    "X-Amz-Target": "AmazonBedrockRuntime.InvokeModel",
}

def call_nova(prompt):
    body = {
        "messages": prompt,
        "max_tokens": 1000,
        "temperature": 0, # temperature를 낮게 하여 무작위성을 줄이고 사실 기반 질의응답에 특화되게 설정정
    }

    response = requests.post(
        url=NOVA_ENDPOINT.format(region=REGION),
        headers=headers,
        data=json.dumps(body)
    )

    return response.json()["content"]
