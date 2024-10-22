from gemini import complete_gemini
from claude import complete_claude
from llama import complete_llama
from mistral import complete_mistral
from mistral_small import complete_mistral_s

llms_api = {
    'gemini': complete_gemini,
    'claude': complete_claude,
    'llama': complete_llama,
    'mistral': complete_mistral,
    'mistral_s': complete_mistral_s
}
def llm_infer(llm_name: str, prompt: str):
    """
    llms_name: the specific llm model name
    prompt: the context asking llm to generated response
    """
    if llm_name not in llms_api.keys():
        raise Exception(f"not valid LLM model {llm_name}, only support {str(llms_api.keys())}!")
    result = llms_api[llm_name](prompt)
    return result