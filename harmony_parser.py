# harmony_parser.py
# Базовый парсер для языка Harmony: создание дерева синтаксиса FDL-команд

import re

class HarmonyParser:
    def __init__(self):
        self.tokens = []
        self.tree = []

    def tokenize(self, code):
        # Разделяем на слова и спецсимволы
        pattern = r"(тезис|антитезис|синтез|анализ|pragma|:)"  # базовые ключевые слова
        self.tokens = re.split(pattern, code)
        self.tokens = [token.strip() for token in self.tokens if token.strip()]
        return self.tokens

    def parse(self):
        ast = []
        i = 0
        while i < len(self.tokens):
            token = self.tokens[i]
            if token == "тезис":
                ast.append({"type": "Thesis", "value": self.tokens[i+1]})
                i += 2
            elif token == "антитезис":
                ast.append({"type": "Antithesis", "value": self.tokens[i+1]})
                i += 2
            elif token == "синтез":
                ast.append({"type": "Synthesis", "value": None})
                i += 1
            elif token == "анализ":
                ast.append({"type": "Analysis", "value": None})
                i += 1
            elif token == "pragma":
                ast.append({"type": "PragmaCall", "value": self.tokens[i+1]})
                i += 2
            else:
                i += 1
        self.tree = ast
        return ast

    def display_tree(self):
        return "\n".join([f"🔹 {node['type']}: {node['value']}" for node in self.tree])

# Пример:
# parser = HarmonyParser()
# code = "тезис: Истина относительна антитезис: Истина абсолютна синтез анализ"
# parser.tokenize(code)
# print(parser.parse())
# print(parser.display_tree())
