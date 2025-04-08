from llm1_prompt import build_llm1_prompt
from nova_client import call_nova
import json

def lambda_handler(event, context):
    body = json.loads(event["body"])
    user_question = body.get("question")

    prompt = build_llm1_prompt(user_question)
    sql_query = call_nova(prompt)

    return {
        "statusCode": 200,
        "body": json.dumps({"sql": sql_query})
    }