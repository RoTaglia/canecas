<h1 align="center">Gerador de PDF de Imagens para Canecas</h1>

<p align="center">
  Este é um aplicativo desenvolvido em Python usando <strong>Tkinter</strong>, <strong>PIL</strong> e <strong>FPDF</strong> para gerar PDFs a partir de imagens selecionadas, adequado para a impressão de estampas em canecas. Ele permite que os usuários adicionem imagens, visualizem miniaturas e gerem um PDF formatado automaticamente.
</p>

---

<h2>📦 Funcionalidades</h2>

<ul>
  <li>Interface gráfica moderna e intuitiva.</li>
  <li>Adição e visualização de imagens antes da geração do PDF.</li>
  <li>Remoção de imagens selecionadas.</li>
  <li>Geração de PDFs formatados automaticamente com alinhamento das imagens.</li>
  <li>Visualização do PDF gerado diretamente no navegador.</li>
  <li>Inicia em tela maximizada para melhor experiência do usuário.</li>
</ul>

---

<h2>🛠️ Instalação</h2>

<h3>🔹 Pré-requisitos</h3>

<p>Certifique-se de ter o <strong>Python 3.8+</strong> instalado em seu sistema.</p>

<h3>🔹 Clonando o Repositório</h3>

<p>Clone o repositório para o seu computador:</p>

<pre><code>git clone https://github.com/seu-usuario/gerador-pdf-canecas.git
cd gerador-pdf-canecas
</code></pre>

<h3>🔹 Instalando Dependências</h3>

<p>Execute o seguinte comando para instalar todas as bibliotecas necessárias:</p>

<pre><code>pip install -r requirements.txt
</code></pre>

<p>Se preferir instalar as dependências manualmente, execute:</p>

<pre><code>pip install tkinter pillow fpdf pymupdf
</code></pre>

---

<h2>🚀 Como Usar</h2>

<ol>
  <li>Execute o programa com o seguinte comando:</li>
  <pre><code>python app.py</code></pre>
  <li>Clique no botão <strong>"Adicionar Imagens"</strong> para selecionar os arquivos desejados.</li>
  <li>Visualize as miniaturas das imagens selecionadas.</li>
  <li>Remova imagens se necessário, clicando no botão <strong>"Excluir"</strong> abaixo de cada miniatura.</li>
  <li>Clique em <strong>"Gerar PDF"</strong> para criar o documento.</li>
  <li>O PDF será salvo temporariamente e aberto automaticamente no navegador.</li>
</ol>

---

<h2>🖥️ Capturas de Tela (Opcional)</h2>

<p>Adicione capturas de tela do programa em funcionamento aqui.</p>

---

<h2>🔧 Como Empacotar para Executável (Opcional)</h2>

<p>Caso deseje gerar um arquivo executável, utilize o <strong>PyInstaller</strong>:</p>

<pre><code>pyinstaller --onefile --windowed --icon=caneca.ico app.py
</code></pre>

<p>Isso criará um executável na pasta <code>dist/</code>.</p>

---

<h2>📜 Licença</h2>

<p>Este projeto é distribuído sob a licença <strong>MIT</strong>. Veja o arquivo <a href="LICENSE">LICENSE</a> para mais detalhes.</p>

---

<h2>📌 Contribuição</h2>

<p>Contribuições são bem-vindas! Se quiser sugerir melhorias ou corrigir erros, sinta-se à vontade para abrir uma <strong>issue</strong> ou enviar um <strong>pull request</strong>.</p>

<p>Se gostou do projeto, ⭐ considere deixar um <strong>star</strong> no repositório!</p>

---

<h2>📞 Contato</h2>

<p>Caso tenha dúvidas ou sugestões, entre em contato:</p>

<ul>
  <li>📧 <strong>Email</strong>: <a href="mailto:seu-email@email.com">falecomigo@gmail.com</a></li>
  <li>🔗 <strong>GitHub</strong>: <a href="https://rotaglia.github.io/">RoTaglia.github.io</a></li>
</ul>

---

<h3>Estrutura do Projeto</h3>

<pre>
/gerador-pdf-canecas
│
├── /images
│   └── caneca.png          # Ícone da aplicação
│
├── /templates
│   └── index.html          # Template HTML (se aplicável)
│
├── /static
│   └── styles.css          # Estilos CSS (se aplicável)
│
├── app.py                  # Código principal
├── requirements.txt        # Lista de dependências
├── LICENSE                 # Arquivo de licença
└── README.md               # Este arquivo
</pre>