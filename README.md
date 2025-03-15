# WPX Firewall

_[English version below](#english-version)_

Um firewall de rede baseado em Python com uma interface interativa para monitoramento de pacotes em tempo real e bloqueio de IPs.

![WPX Firewall Preview](images/firewall-preview.png)

## Recursos

- Captura e análise de pacotes em tempo real
- Interface de menu interativa
- Pausar/Retomar a varredura de pacotes
- Gerenciamento de lista negra de IPs
- Sistema de registro automático
- Armazenamento persistente de lista negra
- Feedback visual para todas as operações

## Requisitos

- Python 3.x
- Biblioteca Scapy
- Privilégios de administrador
- Windows: Npcap (necessário para captura de pacotes)
- Linux: libpcap-dev

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/Wil-JC-Pimenta/wpx_firewall

cd wpx_firewall
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Para usuários Windows:
   - Baixe e instale [Npcap](https://npcap.com/)
   - Execute o PowerShell como Administrador

## Uso

Execute o firewall com privilégios de administrador:

Windows:

```bash
python wpx_firewall.py
```

Linux:

```bash
sudo python3 wpx_firewall.py
```

### Menu Interativo

```
╔════════════════════════════════════╗
║          WPX Firewall              ║
╠════════════════════════════════════╣
║ 1. Adicionar IP à lista negra      ║
║ 2. Remover IP da lista negra       ║
║ 3. Listar IPs bloqueados           ║
║ 4. Alternar varredura de pacotes   ║
║ 5. Sair                            ║
╚════════════════════════════════════╝
```

### Opções do Menu

1. **Adicionar IP à lista negra**

   - Bloqueia pacotes do IP especificado
   - Salva automaticamente no armazenamento persistente
   - Exemplo: `192.168.1.100`

2. **Remover IP da lista negra**

   - Remove o IP da lista de bloqueio
   - Atualiza imediatamente o armazenamento persistente

3. **Listar IPs bloqueados**

   - Mostra todos os IPs atualmente bloqueados
   - Exibe em ordem classificada com formatação visual

4. **Alternar varredura de pacotes**

   - Pausar/Retomar o monitoramento de pacotes
   - Útil para manutenção ou atualizações do sistema
   - O status é claramente exibido

5. **Sair**
   - Para o firewall com segurança
   - Salva todas as alterações antes de sair

## Estrutura do Projeto

```
firewall/
├── wpx_firewall.py     # Implementação principal do firewall
├── requirements.txt    # Dependências Python
├── blacklist.json      # Lista negra persistente de IPs
├── logs/
│   └── firewall.log    # Registros de atividades
└── README.md           # Documentação
```

## Sistema de Registro

O firewall mantém registros detalhados de todas as atividades:

- Eventos de início/parada do firewall
- Adições/remoções de IP da lista negra
- Tentativas de pacotes bloqueados
- Erros e exceções do sistema

Localização do arquivo de log: `logs/firewall.log`

## Indicadores de Status

O programa usa indicadores visuais para diferentes tipos de mensagens:

- `[+]` - Operações de adição
- `[-]` - Operações de remoção
- `[*]` - Informações de status
- `[!]` - Avisos/Erros

## Recursos de Segurança

1. **Lista Negra Persistente**

   - A lista negra sobrevive a reinicializações do programa
   - Salvamento automático após cada modificação
   - Formato JSON para fácil backup/restauração

2. **Tratamento de Erros**

   - Gerenciamento robusto de exceções
   - Registro detalhado de erros
   - Mensagens de erro amigáveis ao usuário

3. **Desligamento Seguro**
   - Encerramento gracioso com CTRL+C
   - Salvamento automático de estado
   - Gerenciamento limpo de threads

## Solução de Problemas

1. **Problemas de Permissão**

   - Windows: Execute o PowerShell como Administrador
   - Linux: Use sudo
   - Verifique as permissões de arquivo para o diretório de logs

2. **Problemas de Captura de Pacotes**

   - Windows: Verifique a instalação do Npcap
   - Linux: Instale libpcap-dev
   - Verifique as permissões da interface de rede

3. **Mensagens de Erro Comuns**
   - "No libpcap provider available": Instale Npcap
   - "Permission denied": Execute com privilégios de administrador
   - "Address already in use": Verifique outros softwares de firewall

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir novos recursos
- Enviar pull requests
- Melhorar a documentação

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter detalhes.

## Agradecimentos

- Biblioteca Scapy para manipulação de pacotes
- Npcap para captura de pacotes no Windows
- Contribuidores e testadores da comunidade

---

<a name="english-version"></a>

# WPX Firewall

A Python-based network firewall with an interactive interface for real-time packet monitoring and IP blocking.

![WPX Firewall Preview](images/firewall-preview.png)

## Features

- Real-time packet capture and analysis
- Interactive menu interface
- Pause/Resume packet scanning
- IP blacklist management
- Automatic logging system
- Persistent blacklist storage
- Visual feedback for all operations

## Requirements

- Python 3.x
- Scapy library
- Administrator privileges
- Windows: Npcap (required for packet capture)
- Linux: libpcap-dev

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Wil-JC-Pimenta/wpx_firewall

cd wpx_firewall
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. For Windows users:
   - Download and install [Npcap](https://npcap.com/)
   - Run PowerShell as Administrator

## Usage

Run the firewall with administrator privileges:

Windows:

```bash
python wpx_firewall.py
```

Linux:

```bash
sudo python3 wpx_firewall.py
```

### Interactive Menu

```
╔════════════════════════════════════╗
║          WPX Firewall              ║
╠════════════════════════════════════╣
║ 1. Add IP to blacklist             ║
║ 2. Remove IP from blacklist        ║
║ 3. List blocked IPs                ║
║ 4. Toggle packet scanning          ║
║ 5. Quit                            ║
╚════════════════════════════════════╝
```

### Menu Options

1. **Add IP to blacklist**

   - Blocks packets from specified IP
   - Automatically saves to persistent storage
   - Example: `192.168.1.100`

2. **Remove IP from blacklist**

   - Removes IP from blocking list
   - Updates persistent storage immediately

3. **List blocked IPs**

   - Shows all currently blocked IPs
   - Displays in sorted order with visual formatting

4. **Toggle packet scanning**

   - Pause/Resume packet monitoring
   - Useful for system maintenance or updates
   - Status is clearly displayed

5. **Quit**
   - Safely stops the firewall
   - Saves all changes before exit

## Project Structure

```
firewall/
├── wpx_firewall.py    # Main firewall implementation
├── requirements.txt      # Python dependencies
├── blacklist.json       # Persistent IP blacklist
├── logs/
│   └── firewall.log     # Activity logs
└── README.md            # Documentation
```

## Logging System

The firewall maintains detailed logs of all activities:

- Firewall start/stop events
- IP additions/removals from blacklist
- Blocked packet attempts
- System errors and exceptions

Log file location: `logs/firewall.log`

## Status Indicators

The program uses visual indicators for different types of messages:

- `[+]` - Addition operations
- `[-]` - Removal operations
- `[*]` - Status information
- `[!]` - Warnings/Errors

## Security Features

1. **Persistent Blacklist**

   - Blacklist survives program restarts
   - Automatic saving after each modification
   - JSON format for easy backup/restore

2. **Error Handling**

   - Robust exception management
   - Detailed error logging
   - User-friendly error messages

3. **Safe Shutdown**
   - Graceful termination on CTRL+C
   - Automatic state saving
   - Clean thread management

## Troubleshooting

1. **Permission Issues**

   - Windows: Run PowerShell as Administrator
   - Linux: Use sudo
   - Check file permissions for logs directory

2. **Packet Capture Issues**

   - Windows: Verify Npcap installation
   - Linux: Install libpcap-dev
   - Check network interface permissions

3. **Common Error Messages**
   - "No libpcap provider available": Install Npcap
   - "Permission denied": Run with admin privileges
   - "Address already in use": Check for other firewall software

## Contributing

Contributions are welcome! Please feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Scapy library for packet manipulation
- Npcap for Windows packet capture
- Community contributors and testers
