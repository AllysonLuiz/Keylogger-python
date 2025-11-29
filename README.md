# Keylogger em Python (Uso Educacional)

Este repositório contém um **exemplo prático de keylogger em Python** com fins **estritamente educacionais**.  
O objetivo é demonstrar como funcionam técnicas de captura de teclado e envio de dados, para que estudantes e profissionais de segurança possam **entender, detectar e prevenir** ataques semelhantes.

⚠️ **Aviso Importante**  
Este projeto **não deve ser utilizado em ambientes reais** sem autorização explícita.  
O uso indevido pode ser considerado crime conforme a legislação vigente.

---

## 📂 Estrutura do Projeto

- `src/keylogger.py` → Script de exemplo
- `logs/log.txt` → Arquivo de saída com teclas capturadas
- `docs/teoria.md` → Explicações teóricas sobre keyloggers
- `docs/prevencao.md` → Contramedidas e boas práticas de segurança

---
## 🔑 Configuração de Variáveis de Ambiente

Este projeto utiliza um arquivo `.env` para armazenar credenciais de teste (como e-mail e senha de autenticação).  
Isso evita que informações sensíveis fiquem expostas diretamente no código.

### Estrutura do `.env`

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte formato:

```env
EMAIL_ORIGEM=seu_email_aqui
EMAIL_DESTINO=seu_email_aqui
PASSWORD=sua_senha_aqui

## 🚀 Como funciona (teoria)

1. Captura das teclas digitadas.
2. Armazenamento em um arquivo `log.txt`.
3. Envio do arquivo como anexo por e-mail (simulação).

---

## 🛡️ Contramedidas de Prevenção

Para se proteger contra keyloggers, recomenda-se:

- **Antivírus e Antimalware**  
  Utilizar softwares atualizados que detectem comportamentos suspeitos.

- **Monitoramento de processos**  
  Verificar programas em execução e consumo anormal de recursos.

- **Atualizações regulares**  
  Manter sistema operacional e aplicativos sempre atualizados.

- **Uso de autenticação multifator (MFA)**  
  Reduz o impacto caso credenciais sejam capturadas.

- **Teclados virtuais e gerenciadores de senhas**  
  Dificultam a captura direta de teclas.

- **Educação e conscientização**  
  Treinar usuários para reconhecer sinais de infecção e evitar downloads suspeitos.

---

## 📚 Objetivo Educacional

Este projeto é destinado a:
- Estudantes de segurança da informação
- Pesquisadores em cibersegurança
- Profissionais que desejam entender ataques e desenvolver defesas

---

## 📜 Licença

Distribuído sob licença MIT.  
Uso permitido apenas para fins **educacionais e acadêmicos**.
