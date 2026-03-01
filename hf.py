import config 
from huggingface_hub import InferenceClient 

MODELS = getattr(config, "HF_MODELS", ["meta-llama/Llama-3.1-8b-Instruct"])

def generate_response(prompt: str, temperature: float = 0.3, max_tokens: int = 512) -> str:
    key = getattr(config, "HF_API_KEY", None)

    if not key:
        return "Error: HF_API_KEY missing in config.py"
        
    last_err = None
    for m in MODELS:
        try:
            client = InferenceClient(token=key)
            # HF text_generation often uses a slightly different structure depending on the model
            response = client.chat_completion(
                model=m,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response.choices[0].message.content
        except Exception as e:
            last_err = e
            
    return (
        "Hugging Face model failed\n"
        f"Tried models: {MODELS}\n"
        f"Details: {type(last_err).__name__}: {last_err}"
    )