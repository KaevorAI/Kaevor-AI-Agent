translations = {
    "en": {
        "welcome": "Welcome to Kaevor AI",
        "prompt_required": "Prompt is required",
    },
    "zh": {
        "welcome": "欢迎使用 Kaevor AI",
        "prompt_required": "需要输入提示",
    },
    "es": {
        "welcome": "Bienvenido a Kaevor AI",
        "prompt_required": "Se requiere un mensaje",
    }
}

def translate(language, key):
    return translations.get(language, translations["en"]).get(key, key)
