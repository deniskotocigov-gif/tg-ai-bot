import telebot
from openai import OpenAI

# === ВСТАВЬ СВОИ ДАННЫЕ СЮДА ===
TG_TOKEN = "8925804449:AAGbElVQ4ZDIxkF16Ia3aDXRyACxb0m5Qkc"
MY_ID = 1037796366  # ТВОИ_ЦИФРЫ_ОТ_USERINFOBOT
AI_KEY = "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"
# ===============================

# Настройка бесплатного ИИ
ai_client = OpenAI(api_key=AI_KEY, base_url="https://api.groq.com/openai/v1")

bot = telebot.TeleBot(TG_TOKEN)

def get_ai_text(title, desc):
    prompt = f"Напиши отклик на заказ: {title}. Суть: {desc}. Будь вежлив, предложи решение на Tilda или Python. Срок 7 дней."
    chat_completion = ai_client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

@bot.message_handler(commands=['test'])
def test(message):
    bot.send_message(MY_ID, "⏳ Генерирую тестовый отклик...")
    text = get_ai_text("Сделать сайт", "Нужен лендинг для продажи грибов на Тильде")
    bot.send_message(MY_ID, f"✅ ГОТОВЫЙ ОТКЛИК:\n\n{text}")

    if __name__ == "__main__":
      print("Бот запущен...")
      bot.infinity_polling()
