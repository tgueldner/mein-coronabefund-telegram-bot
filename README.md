# Telegram Bot zum SARS-CoV-2-Befund
Ein Telegram-Bot, der einen PCR-Befund von mein-coronabefund.de abfragt und per Telegram benachrichtigt, wenn sich der Status ändert.   

## Setup
* Git-Repository clonen
* Telegram-Bot erstellen, siehe https://www.heise.de/tipps-tricks/Telegram-Bot-erstellen-so-geht-s-5055172.html
* Telegram-TOKEN und CHAT_ID in in ``keys/telegram.py.example`` eintragen und nach ``keys/telegram.py`` umbenennen
* PCR-Test-ID, Geburtstag und Name der Testperson in ``userRepository.py`` eintragen

## Bot starten
``
python3 main.py
``
