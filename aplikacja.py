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
        
    
def read_article(file_path):
    with open(file_path, "r", encoding = "utf-8") as file:
        return file.read()
    
def save_html(file_path, content):
    with open(file_path,"w", encoding = "utf-8") as file:
        file.write(content)




def main():
    article = read_article("artykul.txt")
    
    prompt = """
    W podanym niżej artykule dodaj odpowiednie tagi HTML do strukturyzacji treści i wstaw pomiędzy nie tekst z artykułu. We wszystkich miejscach, gdzie warto wstawić grafiki wstaw tag <img> z atrybutem src="image_placeholder.jpg. Dodaj do tagów <img> atrybut alt z dokładną treścią prompta, który umożliwi wygenerowanie odpowiedniej grafiki. Używając odpowiedniego tagu HTML umieść podpisy pod dodanymi zdjęciami. Nie używaj CSS, Javascript i znaczników <body> <html> <head>

    Artykuł:
    """+article
    new_article = send_prompt(prompt)

    save_html("artykul.html", new_article)


if __name__ == "__main__":
    main()