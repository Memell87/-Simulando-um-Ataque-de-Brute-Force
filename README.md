# Medusa-e-Python
Teste de Força Bruta com Medusa e Python
🛡️ Auditoria de Segurança: Teste de Força Bruta com Medusa e Python
📖 Sobre o Projeto
Este repositório contém a documentação e os scripts desenvolvidos para o desafio prático de Cibersegurança da DIO. O objetivo principal foi simular ataques de força bruta (Brute Force) em serviços de rede (FTP) dentro de um ambiente controlado, utilizando ferramentas de auditoria e automação personalizada.

🧪 Cenário de Teste
O laboratório foi montado em um ambiente virtual isolado para garantir a segurança dos testes:

Atacante: Kali Linux (IP: Automático).

Alvo: Metasploitable 2 (IP: 192.168.56.101).

Rede: Host-only (Exclusiva de hospedeiro) configurada no VirtualBox.

🛠️ Ferramentas Utilizadas
Medusa: Ferramenta modular e rápida para ataques de força bruta em diversos protocolos.

Python 3: Utilizado para criar um script de geração de wordlists customizadas.

Nmap: Varredura inicial de portas e serviços.

VirtualBox: Orquestração das máquinas virtuais.

🚀 Implementação
1. Automação com Python
Como parte do desenvolvimento do projeto, criei um script chamado gerar_wordlist.py. Este script gera combinações de senhas baseadas em palavras-chave e padrões numéricos, otimizando o processo de auditoria.

Python
# Exemplo de lógica utilizada
import itertools
# Gera combinações entre palavras-chave e números comuns
2. Execução do Medusa
Utilizei o Medusa para testar a wordlist gerada contra o serviço FTP do alvo. Durante os testes, explorei diferentes parâmetros da ferramenta:

Bash
# Comando para testar wordlist customizada
medusa -h 192.168.56.101 -u msfadmin -P wordlist_custom.txt -M ftp

# Comando para testar variações de usuário e senha (Success Case)
medusa -h 192.168.56.101 -u msfadmin -e ns -M ftp
📈 Resultados Obtidos
Identificação de Vulnerabilidade: O sistema alvo permitia o acesso com credenciais idênticas (usuário: msfadmin / senha: msfadmin).

Validação de Automação: O script Python reduziu o tempo de criação de dicionários de senhas focados no alvo.

Logs de Auditoria: Conforme demonstrado nas capturas de tela (pasta /images), o Medusa reportou com sucesso quando a conta foi encontrada.

🛡️ Recomendações de Mitigação
Para evitar os ataques simulados neste projeto, recomenda-se:

Políticas de Complexidade: Proibir senhas iguais ao nome de usuário ou termos comuns.

Bloqueio de IP (Rate Limiting): Implementar ferramentas como o Fail2Ban para bloquear tentativas sucessivas de login falhas.

Desativação de Protocolos Inseguros: Substituir o FTP por alternativas criptografadas como SFTP ou SSH.

👤 Autor
Memell87
Estudante de Análise e Desenvolvimento de Sistemas (ADS).

📂 Estrutura do Repositório
gerar_wordlist.py: Script de automação em Python.

README.md: Documentação completa do desafio.

/images: Prints de tela das execuções e do sucesso do ataque.

Este projeto foi realizado apenas para fins educacionais em ambiente controlado.
