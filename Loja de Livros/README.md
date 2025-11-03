# 🏪 Sistema de Livraria Distribuída - Trabalho 1

## 📋 Descrição do Projeto
Sistema distribuído para gerenciamento de livraria online, implementando comunicação entre processos via sockets TCP e serialização personalizada de objetos.

## 🎯 Objetivos Atendidos
- **Serialização personalizada** de objetos Livro
- **Comunicação cliente-servidor** via sockets TCP
- **Streams customizados** (OutputStream/InputStream)
- **Arquitetura multi-threaded** no servidor

## 🏗️ Arquitetura do Sistema

### 📁 Estrutura de Pastas

livraria_distribuida/
├── model/ # Classes de domínio (POJOs)
├── streams/ # Serialização personalizada
├── server/ # Servidor TCP
├── client/ # Cliente TCP
├── testes/ # Casos de teste
└── docs/ # Documentação

🔄 Fluxo de Comunicação

Cliente → Serializa objetos → Envia via TCP → Servidor
Cliente ← Desserializa objetos ← Recebe via TCP ← Servidor