import os
from dotenv import load_dotenv

from search_prompt import search_prompt
import ingest_pdf

from langchain_openai import ChatOpenAI

load_dotenv()

# Cores ANSI para print
class Colors:
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GREEN = '\033[92m'  
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

def main():

    print(f"{Colors.BLUE }╔══════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.BLUE }║                    🤖 ASSISTENTE IA RAG - Postgres           ║{Colors.END}")
    print(f"{Colors.BLUE }╠══════════════════════════════════════════════════════════════╣{Colors.END}")
    print(f"{Colors.BLUE }║  ❌ Para sair: digite {Colors.YELLOW}'exit'{Colors.BLUE}                                 ║{Colors.END}")
    print(f"{Colors.BLUE }║  💬 Para fazer perguntas: digite sua pergunta diretamente    ║{Colors.END}")
    print(f"{Colors.BLUE }╚══════════════════════════════════════════════════════════════╝{Colors.END}")
    print(f"")
    print(f"{Colors.CYAN}✨ Como posso ajudá-lo hoje?{Colors.END}")
    print()

    while(True):

        # Captura da pergunta do usuário
        print(f"{Colors.CYAN}┌─ Digite a sua dúvida{Colors.END}")
        question = input(f"{Colors.CYAN}└─ {Colors.END}")
        print()
        
        if question == "exit":
            print(f"{Colors.GREEN}👋 Obrigado por usar o Assistente IA RAG! Até logo!{Colors.END}")
            break
        else:
            # Resposta da IA
            print(f"{Colors.PURPLE}┌─ 🤖 Assistente IA trabalhando{Colors.END}")
            print(f"{Colors.PURPLE}├─ Processando sua pergunta...{Colors.END}")
            
            question =search_prompt(question)
            model = ChatOpenAI(model=os.getenv("OPENAI_MODEL_CHAT","gpt-3.5-turbo"), temperature=0.5)
            response = model.invoke(question)
            
            print(f"{Colors.PURPLE}└─ {response.content}{Colors.END}")
            print()

if __name__ == "__main__":
    main()