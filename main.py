#!/usr/bin/env python3
"""
Telegram Bot - responde /ping com o horário atual

Como usar:
1. Instale as dependências: pip install -r requirements.txt
2. Crie um bot no Telegram via @BotFather e obtenha o token
3. Configure o token no arquivo .env ou como variável de ambiente:
   export TELEGRAM_BOT_TOKEN="seu_token_aqui"
4. Execute: python main.py
"""

import os
import sys
import logging
from datetime import datetime

# Verifica se está rodando em modo de teste (sem argumentos reais)
TEST_MODE = os.environ.get("TELEGRAM_BOT_TOKEN") is None and len(sys.argv) == 1

if TEST_MODE:
    print("=" * 50)
    print("  Telegram Ping Bot - Modo de demonstração")
    print("=" * 50)
    print()
    print("O bot NÃO foi iniciado porque nenhum token foi encontrado.")
    print()
    print("Para usar o bot:")
    print("  1. Crie um bot no Telegram via @BotFather")
    print("  2. Copie o token gerado")
    print("  3. Execute:")
    print("     export TELEGRAM_BOT_TOKEN='seu_token_aqui'")
    print("     python main.py")
    print()
    print("Simulando resposta do /ping:")
    now = datetime.now()
    print(f"  🏓 Pong! Horário atual: {now.strftime('%d/%m/%Y %H:%M:%S')}")
    print()
    print("=" * 50)
    sys.exit(0)

# Configuração de logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

try:
    from telegram import Update
    from telegram.ext import Application, CommandHandler, ContextTypes
except ImportError:
    print("Erro: biblioteca python-telegram-bot não instalada.")
    print("Execute: pip install -r requirements.txt")
    sys.exit(1)


def get_current_time() -> str:
    """Retorna o horário atual formatado em português."""
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")


async def ping_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde ao comando /ping com o horário atual."""
    current_time = get_current_time()
    message = f"🏓 *Pong!*\n📅 Horário atual: `{current_time}`"
    
    await update.message.reply_text(
        message,
        parse_mode="Markdown"
    )
    logger.info(f"Comando /ping recebido de @{update.effective_user.username} - Horário: {current_time}")


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde ao comando /start com uma mensagem de boas-vindas."""
    user = update.effective_user
    name = user.first_name if user.first_name else "usuário"
    
    message = (
        f"Olá, {name}! 👋\n\n"
        "Eu sou o *Ping Bot*!\n\n"
        "📌 *Comandos disponíveis:*\n"
        "/ping — Retorna o horário atual\n"
        "/start — Exibe esta mensagem\n"
        "/help — Exibe ajuda"
    )
    
    await update.message.reply_text(message, parse_mode="Markdown")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde ao comando /help."""
    message = (
        "🤖 *Ajuda - Ping Bot*\n\n"
        "*Comandos disponíveis:*\n\n"
        "🏓 `/ping` — Responde com o horário atual do servidor\n"
        "🚀 `/start` — Exibe a mensagem de boas-vindas\n"
        "❓ `/help` — Exibe esta mensagem de ajuda\n\n"
        "_Desenvolvido com python-telegram-bot_"
    )
    
    await update.message.reply_text(message, parse_mode="Markdown")


def main() -> None:
    """Inicia o bot."""
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    
    if not token:
        logger.error("Token do bot não encontrado!")
        logger.error("Defina a variável de ambiente TELEGRAM_BOT_TOKEN")
        logger.error("Exemplo: export TELEGRAM_BOT_TOKEN='seu_token_aqui'")
        sys.exit(1)
    
    logger.info("Iniciando Telegram Ping Bot...")
    
    # Cria a aplicação
    application = Application.builder().token(token).build()
    
    # Registra os handlers de comandos
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("ping", ping_command))
    
    logger.info("Bot iniciado! Aguardando mensagens... (Pressione Ctrl+C para parar)")
    
    # Inicia o bot em modo polling
    application.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True
    )


if __name__ == "__main__":
    main()
