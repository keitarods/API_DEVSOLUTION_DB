import requests

# Defina a URL do seu endpoint FastAPI
url = "https://api-devsolution-db.onrender.com/inseri_dados"

# Dados a serem enviados (substitua conforme necessário)
dados = {"g":"g",
         "col1":3,
         "col2":2,
         "col3":5,
         "col4":4,
         "col5":5,
         "col6":2,
         "col7":7,
         "col8":8,
         "col9":"oioioibsas"}

# Envie a solicitação POST
response = requests.post(url, json=dados)

# Verifique a resposta
if response.status_code == 200:
    print("Dados enviados com sucesso!")
else:
    print(f"Erro ao enviar dados. Código de status: {response.status_code}")
    print(response.text)  # Exibe o corpo da resposta em caso de erro