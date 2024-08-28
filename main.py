from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

modelo = "gemini-1.5-flash"
cliente = genai.GenerativeModel(model_name = modelo)

prompt = "Crie um poema sobre a empresa Hare Express, uma empresa de entrega inovadora que utiliza uma combinação única de corredores ágeis e tecnologia de ponta para garantir entregas ultrarrápidas em áreas urbanas."
resposta = cliente.generate_content(prompt)
print(resposta.text)