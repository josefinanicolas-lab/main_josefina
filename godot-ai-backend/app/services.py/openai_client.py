from openai import OpenAI
from app.config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_openai(user_message: str, context: dict | None = None) -> str:
    ctx = f"\n\nContexto (JSON): {context}" if context else ""

    resp = client.responses.create(
        model=OPENAI_MODEL,
        input=(
            "Sos un asistente de programación especializado en Godot 4 (GDScript). "
            "Respondé con pasos concretos y ejemplos cortos.\n\n"
            f"Usuario: {user_message}{ctx}"
        ),
        temperature=0.3,
        max_output_tokens=300,
    )

    return resp.output_text
