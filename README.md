# Python Agent Collector
## Descrição
Este projeto consiste no desenvolvimento de um agente em Python capaz de coletar informações vitais de qualquer dispositivo. O agente é projetado para obter dados relacionados a hardware, software e configurações de rede (TCP/IP). Além disso, o agente será integrado em um aplicativo Electron multiplataforma para fornecer uma interface gráfica de usuário para interação e visualização dos dados coletados.

## Recursos

- **Coleta de Informações:**
  - Hardware: Informações sobre CPU, memória RAM, armazenamento, etc.
  - Software: Detalhes sobre o sistema operacional, versões de software instalado, drivers e licenças, arquitetura e etc.
  - Rede (TCP/IP): Informações sobre interfaces de rede, endereços IP, portas abertas...

- **Interface Gráfica Multiplataforma:**
  - Desenvolvimento de um aplicativo Electron para oferecer uma experiência de usuário consistente em diferentes plataformas (Windows, macOS, Linux).

## Integração
- **App Electron x Agente Python**
    - Comunicação Interprocessual:
      Sem a necessidade de um servidor externo, será utilizado a comunicação interprocessual (IPC) local entre o processo principal do Electron (main process) e o processo de renderização (renderer process), onde o código JavaScript é executado.

## Pré-requisitos

- Python 3.x instalado
- Node.js e npm instalados para o desenvolvimento do aplicativo Electron
