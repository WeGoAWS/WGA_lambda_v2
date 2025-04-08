from llm2_prompt import build_llm2_prompt
from nova_client import call_nova
import json

def lambda_handler(event, context):
    body = json.loads(event["body"])
    user_question = body.get("question")
    query_result = body.get("result")

    prompt = build_llm2_prompt(user_question, query_result)
    answer = call_nova(prompt)

    return {
        "statusCode": 200,
        "body": json.dumps({"answer": answer})
    }