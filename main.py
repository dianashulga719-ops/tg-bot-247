from telethon import TelegramClient, events

api_id = 34771076
api_hash = 'f697607767753e21c302bf6b1fee0602'

TARGET_WORDS = ['центр', 'печерськ', 'липки']
WATCH_CHANNELS = ['waypoint_ua', 'kyiv_monitor1', 'war_monitor', 'kyivnebomonitoring']

# Використовуємо вашу сесію, щоб бот не просив код у консолі
client = TelegramClient('my_new_session', api_id, api_hash)

@client.on(events.NewMessage(chats=WATCH_CHANNELS))
async def handler(event):
    message_text = event.message.text or ''
    message_lower = message_text.lower()
    
    found_word = next((word for word in TARGET_WORDS if word in message_lower), None)
    
    if found_word:
        await client.send_message(
            'me', 
            f'🔔 Знайдено слово "**{found_word}**" у каналі @{event.chat.username}:\n\n{message_text}'
        )

print("Бот запускається...")
with client:
    print("Бот працює і слухає канали 24/7!")
    client.run_until_disconnected()
