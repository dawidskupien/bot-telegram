import time
import os
from twilio.rest import Client
from telethon import TelegramClient, events


api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

client = Client(account_sid, auth_token)

# Inicjalizacja klienta Telethon
Tclient = TelegramClient("session", api_id, api_hash)

def make_call():
    print("📞 Dzwonię do ciebie...")

    # Wywołanie połączenia na numer telefonu (Twój numer)
    call = client.calls.create(
        from_=twilio_phone_number,  # Twój numer Twilio
        to=phone_number,  # Twój numer telefonu
        url="http://demo.twilio.com/docs/voice.xml"  # Adres do dźwięku połączenia
    )

    print(f"Połączenie SID: {call.sid}")


# Logowanie (tylko przy pierwszym uruchomieniu trzeba wpisać kod z SMS)
async def main():
    await Tclient.start(phone_number)
    print("✅ Bot jest gotowy!")

# Nasłuchiwanie wiadomości w grupach
@Tclient.on(events.NewMessage(chats=None))  # None = wszystkie czaty, można dodać ID grupy
async def auto_reply(event):
    if "oddam" in event.message.text.lower():
        time.sleep(1)
        await event.reply("Wezmę")
        make_call()

# Uruchomienie bota
with Tclient:
    Tclient.loop.run_until_complete(main())
    Tclient.run_until_disconnected()
    
