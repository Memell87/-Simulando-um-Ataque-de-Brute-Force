<img width="945" height="656" alt="medusa py" src="https://github.com/user-attachments/assets/2177dd44-d6c7-4e18-aea8-f060e8b45d68" />
<img width="945" height="656" alt="wordlist py" src="https://github.com/user-attachments/assets/c29f3494-4b91-4910-9642-c0c64933bb5a" />
🛡️ Auditoria de Segurança: Força Bruta com Medusa e Automação em Python

📝 Descrição do Desafio
Este projeto foi desenvolvido como parte de um desafio prático na DIO (Digital Innovation One). O objetivo é simular ataques de força bruta (Brute Force) em um ambiente controlado para entender vulnerabilidades comuns e implementar medidas de mitigação eficazes.

O laboratório consiste em uma rede isolada utilizando VirtualBox, com o Kali Linux como máquina atacante e o Metasploitable 2 como alvo vulnerável.

🛠️ Tecnologias e Ferramentas
Sistema Operacional Atacante: Kali Linux.

Máquina Alvo: Metasploitable 2 (Ambiente intencionalmente vulnerável).

Ferramenta de Ataque: Medusa (Ferramenta modular de força bruta rápida).

Automação: Script em Python 3 para geração de wordlists customizadas.

Virtualização: Oracle VirtualBox com rede Host-Only.

🚀 Implementação Passo a Passo
1. Configuração do Ambiente
As máquinas virtuais foram configuradas em uma rede exclusiva de hospedeiro (Host-only) para garantir que os testes fossem realizados em um ambiente seguro e isolado da rede externa.

Foi realizada uma varredura de rede com nmap para identificar serviços ativos e portas abertas no IP do alvo.

2. Automação com Python (Geração de Wordlist)
Para aumentar a eficiência do ataque, desenvolvi um script em Python que gera combinações inteligentes de senhas. O script utiliza a biblioteca itertools para criar permutações entre palavras-chave, números e caracteres especiais.

Python
import itertools
import time
O script solicita inputs do usuário e gera combinações 
baseadas em lógica de permutação de dados conhecidos.
combinacoes = list(itertools.product(palavras, numeros, caracteres))

3. Execução do Ataque com Medusa
Com a wordlist gerada, utilizei o Medusa para testar as credenciais contra o serviço FTP do Metasploitable 2:

Bash
medusa -h 192.168.56.101 -u msfadmin -P wordlist_custom.txt -M ftp
Resultado: O ataque identificou com sucesso a credencial msfadmin:msfadmin.

💡 Destaques Técnicos
Como estudante de Análise e Desenvolvimento de Sistemas (ADS), foquei em boas práticas de desenvolvimento e administração de sistemas:

Criação de Arquivos via Terminal: Utilizei o comando cat << 'EOF' para criar o script diretamente no terminal do Kali, garantindo a integridade do código e evitando problemas de formatação entre diferentes sistemas operacionais.

Medição de Performance: Adicionei a biblioteca time ao script Python para medir o tempo de execução da geração das senhas, demonstrando preocupação com a eficiência algorítmica.

🛡️ Medidas de Mitigação Recomendadas
Para prevenir este tipo de vulnerabilidade em ambientes reais, as recomendações são:

Políticas de Senhas: Implementar requisitos de complexidade (mínimo de caracteres, uso de símbolos) e rotação periódica.

Bloqueio de Conta (Rate Limiting): Utilizar ferramentas como Fail2Ban para bloquear temporariamente IPs que excedam um número limite de tentativas de login.

Autenticação Multi-fator (MFA): Adicionar uma camada extra de segurança que invalida ataques baseados apenas em senhas.

Desativação de Serviços Inseguros: Desabilitar protocolos que trafegam dados em texto claro (como FTP) e substituí-los por versões seguras (SFTP/SSH).

👤 Autor
Daniel Gaio

Estudante de Análise e Desenvolvimento de Sistemas (ADS).

Este projeto possui finalidade estritamente educacional.
