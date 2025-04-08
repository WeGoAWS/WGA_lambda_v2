# 프롬프트 db to llm2

import json

def build_llm2_prompt(user_input, query_result):
    return [
        {
            "role": "system",
            "content": "You are an assistant that provides clear and accurate natural language explanations based on database query results."
        },
        {
            "role": "user",
            "content": f'''
Task:
Generate a human-readable answer based on the original user question and the SQL query result.

Original User Question:
{user_input}

SQL Query Result (as JSON):
{json.dumps(query_result, indent=2)}

Instructions:
- Be specific using the data.
- Use concise, professional language.
- Do not ask user for clarification.
'''
        }
    ]
