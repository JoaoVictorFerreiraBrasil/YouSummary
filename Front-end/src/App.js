import React, { useState } from 'react';
import './App.css';



function App() {
  const [link, setLink] = useState('');
  const [resumo, setResumo] = useState('');
  const [erro, setErro] = useState('');
  const [carregando, setCarregando] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResumo('');
    setErro('');
    setCarregando(true);

    try {
      const response = await fetch('http://127.0.0.1:8000/resumir', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: link })
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Erro ao resumir o vídeo');
      }

      setResumo(data.resumo);
    } catch (err) {
      setErro(err.message);
    } finally {
      setCarregando(false);
    }
  };

  return (
    <div className="App">
      <h1>YouSummary</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Cole o link do YouTube aqui"
          value={link}
          onChange={(e) => setLink(e.target.value)}
        />
        <button type="submit" disabled={carregando}>
          {carregando ? 'Resumindo...' : 'Resumir'}
        </button>
      </form>

      <div className="resultado">
        {erro && <p className="erro">⚠️ {erro}</p>}
        {resumo && (
          <>
            <h2>Resumo:</h2>
            <p>{resumo}</p>
          </>
        )}
      </div>
    </div>
  );
}

export default App;
