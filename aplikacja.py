import http.client
import json

api_key = "klucz"

host = "api.openai.com"
path = "/v1/chat/completions"

def send_prompt(prompt):

    data = json.dumps({
        "model": "gpt-4",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 1
    })

    connection = http.client.HTTPSConnection(host)
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    connection.request("POST", path, body=data, headers=headers)

    response = connection.getresponse()
    if response.status == 200:
        response_data = response.read().decode("utf-8")
        return json.loads(response_data)["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Błąd API: {response.status}, {response.read().decode('utf-8')}")