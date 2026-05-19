# 🤖 Telegram Ping Bot

Bot simples para Telegram que responde ao comando `/ping` com o horário atual.

## 📋 Pré-requisitos

- Python 3.8+
- Uma conta no Telegram
- Um token de bot (obtido via [@BotFather](https://t.me/BotFather))

## 🚀 Como configurar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Crie um bot no Telegram

1. Abra o Telegram e procure por **@BotFather**
2. Envie o comando `/newbot`
3. Siga as instruções e escolha um nome e username para o bot
4. Copie o **token** gerado (parece com: `123456789:ABCdefGHI...`)

### 3. Configure o token

**Opção A - Variável de ambiente (recomendado):**
```bash
export TELEGRAM_BOT_TOKEN="seu_token_aqui"
```

**Opção B - Arquivo .env:**
```bash
cp .env.example .env
# Edite o arquivo .env e cole seu token
```

> Se usar `.env`, instale também: `pip install python-dotenv`
> E adicione no início do `main.py`: `from dotenv import load_dotenv; load_dotenv()`

### 4. Execute o bot

```bash
python main.py
```

## 💬 Comandos disponíveis

| Comando | Descrição |
|---------|----------|
| `/start` | Mensagem de boas-vindas |
| `/ping` | Retorna o horário atual |
| `/help` | Exibe a ajuda |

## 📌 Exemplo de uso

```
Você: /ping
Bot: 🏓 Pong!
     📅 Horário atual: 15/01/2024 14:32:07
```

## 🛑 Como parar o bot

Pressione `Ctrl+C` no terminal onde o bot está rodando.
