📘 Инструкция по использованию языка Harmony
Harmony — это язык, работающий на основе формально-диалектической логики (FDL). Он применим к логическим системам, AI-модулям, городским системам, образовательным платформам и агентным средам.
________________________________________
📥 Установка (разработка локально)
git clone https://github.com/NgoiSigma/Harmony-Development.git
cd Harmony-Development
python3 fdl_core.py
________________________________________
🔰 Пример FDL-команды
from fdl_core import FDLCore

fdl = FDLCore()
print(fdl.thesis("Истина относительна"))
print(fdl.antithesis("Истина абсолютна"))
print(fdl.synthesize())
print(fdl.analyze())
________________________________________
🧪 Пример прикладной логики (Pragma)
from pragma_layer import PragmaLayer

p = PragmaLayer()
p.register_action("ОтправитьСообщение", "Send Telegram")
p.register_action("Синхронизация", "Sync Kernel", condition="user_authenticated")

print(p.evaluate(["user_authenticated"]))
________________________________________
🔍 Парсинг Harmony-команд
from harmony_parser import HarmonyParser

parser = HarmonyParser()
code = "тезис: Смысл в форме антитезис: Форма в смысле синтез"
parser.tokenize(code)
parser.parse()
print(parser.display_tree())
________________________________________
🧩 Расширение языка
•	Изучи harmony_grammar.json — для добавления новых операторов и синтаксических конструкций.
•	Подключи свою pragma-функцию через register_action().
•	Используй синтез FDL для принятия решений в ИИ.
________________________________________
🧠 Принцип мышления
Каждое решение в Harmony проходит этапы:
1.	Тезис → 2. Антитезис → 3. Синтез → 4. (необязательно) Анализ → 5. Прагма → 6. Действие в среде
________________________________________
Harmony — не просто язык. Это форма смысла.
Применяй его осознанно. Да пребудет с тобой логика. ✨

