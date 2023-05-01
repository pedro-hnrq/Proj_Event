<h1 align="center"> Projeto Type Event </h1>

<h2 align="center">Skills: <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=gree"/>  <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E"/>  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=whitehttps://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"/>  <img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=black">   <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/> </h2>

<h2 align="center"> Prévia <h2>

<h3>Objetivo</h3>

<h4 align="justify">O projeto Type Event utiliza Python e Django para gerenciar eventos e certificados de participação, com a ajuda da biblioteca PIL para personalização dos certificados e geração de arquivos CSV para contabilizar a quantidade de pessoas cadastradas. Dessa forma, fornecer uma solução completa e personalizada para gerenciamento de eventos e certificados de participação. Com ele, você poderá criar, visualizar e gerenciar eventos, bem como gerar certificados personalizados para os participantes.</h4>

<h3>Etapas</h3>
<ul style="list-style-type:square">
  <h4><a href="https://github.com/pedro-hnrq/Proj_Event/tree/main/autenticacao">Autenticação</a></h4>
  <li align="justify">Utilizado o Django Auth, realizei no sistema verificação de autenticação de usuários. </li>
  <li align="justify">Cadastra-se: para o registro de usuário, eu criei uma função que verifica se já existe um username ou email cadastrado, se a senha e confirma senha, assim, atende aos requisitos de segurança.</li>
  <li align="justify">Loga-se: criei uma função que autentica o usuário e faz o seu login. É importante lembrar que eu utilizei o decorador "@login_required" para impedir que usuários mal intencionados acessem a plataforma sem estar logados. </li>
  <li align="justify">Sair: criei uma função que faz o logout do usuário autenticado, permitindo que outro usuário possa realizar o login na plataforma.</li>
  
<h4><a href="https://github.com/pedro-hnrq/Proj_Event/tree/main/eventos">Eventos</a></h4>
 <li align="justify">Type Event permite ao usuário criar e gerenciar eventos, incluindo a inscrição de participantes, a geração de certificados, a exportação de listas de participantes em CSV, entre outras funcionalidades.</li>
  <li align="justify">Novo Evento: é responsável por criar um novo evento, coletando informações do usuário via formulário, como: nome do evento, descrição, data ínicio, data de término, carga horário, logo do evento e paletras de cores. Com isso, salvando no banco de dados.</li>
  <li align="justify">Gerenciar Evento: lista os eventos cadastrados pelo usuário logado, permitindo a busca por nome. Com isso, requisição HTTP GET para extrair um possível parâmetro de busca por nome do evento e filtrar a lista de eventos exibidos na tela. </li>
  <li align="justify">Inscrever Evento: permite que o usuário se inscreva em um evento.</li>
  <li align="justify">Participantes Evento: lista os participantes de um evento, desde que o usuário logado seja o criador do mesmo.</li>
  <li align="justify">Gerar CSV: gera um arquivo CSV contendo os dados dos participantes de um evento.</li>
  <li align="justify">Certificados Evento: exibe a quantidade de certificados pendentes para um evento, desde que o usuário logado seja o criador do mesmo. Além disso, a view conta quantos certificados ainda não foram gerados e exibe esse número na tela.</li>
  <li align="justify">Gerar Certificado: gera um certificado personalizado para cada participante inscrito em um evento, com base em um modelo de certificado presente no diretório do projeto.</li>
  
  <h4><a href="https://github.com/pedro-hnrq/Proj_Event/tree/main/cliente">Cliente</a></h4>
  <li align="justify">Meus Certificados: é responsável por retornar uma lista de certificados relacionados ao usuário que fez a requisição aos eventos. Essa lista é filtrada utilizando o objeto "Certificado" do modelo definido na aplicação "eventos".</li>
</ul>

<h3>Conclusão</h3>
<p align="justify">O projeto Type Event oferece uma solução completa e personalizada para gerenciamento de eventos e certificados de participação, utilizando Python, Django e a biblioteca PIL para geração de certificados personalizados e exportação de arquivos CSV. As etapas fornece uma solução completa e personalizada para gerenciamento de eventos e certificados de participação, com funcionalidades que incluem autenticação de usuários, cadastro e gerenciamento de eventos, inscrição de participantes, geração de certificados, exportação de listas de participantes em CSV, entre outras.</p>
  
  

