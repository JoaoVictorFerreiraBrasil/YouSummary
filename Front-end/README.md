*🧠 YouSummary – Resumos Inteligentes de Vídeos do YouTube*

YouSummary é uma aplicação web que utiliza inteligência artificial para gerar **resumos automáticos de vídeos do YouTube**. Basta colar o link de um vídeo com legenda disponível, e o sistema retorna alguns tópicos explicados de forma mais clara.

---

*🚀 Funcionalidades*

- 🧾 Geração automática de resumo de vídeos do YouTube com legenda (em PT ou EN)
- 🤖 Integração com a API do ChatGPT (OpenAI)
- 🧠 Processamento de transcrição com `youtube_transcript_api`
- 🌐 Front-end responsivo em React com estilo tech
- 🛡️ CORS habilitado para uso em ambientes web

-

*🛠️ Tecnologias Utilizadas*

*Back-end*
- [Python 3.11+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)
- [OpenAI Python SDK](https://pypi.org/project/openai/)
- [dotenv](https://pypi.org/project/python-dotenv/)

*Front-end*
- [React JS](https://reactjs.org/)
- [JavaScript (ES6+)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [CSS customizado com tema tech](#)
- [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

-

*🔧 Como Executar Localmente*

### 1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/YouSummary.git
cd YouSummary
```

### 2. Instale o back-end:
```bash
cd Back-end
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

Crie um arquivo `.env` com sua chave:
```env
OPENAI_API_KEY=sua chave aqui!
```

Execute o servidor:
```bash
uvicorn main:app --reload
```

### 3. Instale o front-end:
```bash
cd ../Front-end
npm install
npm start
```

---

## 🧪 Testes

Com o servidor rodando em `http://127.0.0.1:8000`, você pode testar diretamente no navegador acessando:

```bash
http://127.0.0.1:8000/docs
```

Ou pelo front-end React (`http://localhost:3000`), inserindo um link válido do YouTube com legenda.

---

## 📌 Observações

- A API do YouTube só permite transcrição de vídeos que tenham **legendas ativas (geradas ou manuais)**.
- Se sua chave da OpenAI estiver sem saldo, o sistema retornará um resumo simulado.
---

## 📄 Licença

Feito por João Víctor Ferreira Brasil.

---

## 📬 Contato

- joaovictorferreirabrasil@email.com
- (21)96751-20002