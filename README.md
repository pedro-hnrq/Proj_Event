<h1 align="center"> Projeto Type Event </h1>

<h2 align="center">Skills: <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=gree"/>  <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E"/>  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=whitehttps://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"/>  <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/> </h2>

<h2 align="center"> Prévia <h2>
  
 ![Proj_Event](https://github.com/pedro-hnrq/Proj_Event/assets/74242717/e58afc4a-7323-4b67-b563-208c73f3a638)
 

<h3>Objetivo</h3>

<h4 align="justify">O projeto Type Event utiliza Python e Django para gerenciar eventos e certificados de participação, com a ajuda da biblioteca PIL para personalização dos certificados e geração de arquivos CSV para contabilizar a quantidade de pessoas cadastradas. Dessa forma, fornecer uma solução completa e personalizada para gerenciamento de eventos e certificados de participação. Com ele, você poderá criar, visualizar e gerenciar eventos, bem como gerar certificados personalizados para os participantes.</h4>

<h3>Etapas</h3>
<ul style="list-style-type:square">
  <h4><a href="https://github.com/pedro-hnrq/Proj_Event/tree/main/autenticacao">Autenticação</a></h4>
  <li align="justify">Resumo: Utilizado o Django Auth, realizei no sistema verificação de autenticação de usuários. </li>
  <li align="justify">Cadastra-se: para o registro de usuário, criei uma função que verifica se já existe um nome de usuário ou e-mail cadastrado, e se a senha e confirmação de senha são iguais, atendendo aos requisitos de segurança. Com isso, é criado um Token exclusivo que é enviado por e-mail para o usuário, com um link de autenticação do sistema.</li>
  <li align="justify">Loga-se: criei uma função que autentica o usuário e faz o seu login seguro. É importante lembrar que eu utilizei o decorador "@login_required" para impedir que usuários mal-intencionados acessem a plataforma sem estar logados. </li>
  <li align="justify">Sair: criei uma função que faz o logout do usuário autenticado, permitindo que outro usuário possa realizar o login na plataforma.</li>
  <li align="justify">Esqueceu a senha: Adicionei uma funcionalidade para permitir que os usuários redefinam suas senhas caso as tenham esquecido. Quando um usuário esquece sua senha, ele pode ir para a página "Redefinir Senha" e inserir seu endereço de e-mail associado à conta. Em seguida, o sistema gerará um token de senha exclusivo que será enviado por e-mail ao usuário. Esse token pode ser usado para redefinir a senha do usuário.</li>
  
<h4><a href="https://github.com/pedro-hnrq/Proj_Event/tree/main/eventos">Eventos</a></h4>
 <li align="justify">Resumo: Type Event permite ao usuário criar e gerenciar eventos, incluindo a inscrição de participantes, a geração de certificados, a exportação de listas de participantes em CSV, entre outras funcionalidades.</li>
  <li align="justify">Novo Evento: é responsável por criar um novo evento, coletando informações do usuário via formulário, como: nome do evento, descrição, data ínicio, data de término, carga horário, logo do evento e paletras de cores. Com isso, salvando no banco de dados.</li>
  <li align="justify">Gerenciar Evento: essa funcionalidade permite aos usuários cadastrados listar e gerenciar eventos. Na página de gerenciamento, é possível filtrar os eventos por nome e páginação, com um limite máximo de 5 eventos por página. Através de uma requisição HTTP GET, é possível extrair um parâmetro de busca por nome do evento e filtrar a lista de eventos exibidos na tela. Com isso, o usuário pode facilmente encontrar e gerenciar os eventos desejados. </li>
  <li align="justify">Inscrever Evento: permite que qualquer dos usuários se inscreva em um evento, até mesmo o criado do evento.</li>
  <li align="justify">Participantes Evento: somante o usuário que crio o evento poderá ter acesso. Dessa maneira, lista os participantes de um evento ou poderá gerar CVS, contendo os dados dos participantes de um evento pelos nomes e E-mails.</li>  
  <li align="justify">Certificados Evento: essa funcionalidade está disponível apenas para o criador do evento e permite visualizar a quantidade de certificados pendentes e não gerados para cada participante. Depois que os certificados forem gerados, eles ficarão disponíveis na seção "Meus Certificados" de cada participante. Caso um participante não encontre seu certificado, há uma barra de pesquisa que permite buscar pelo seu e-mail cadastrado no evento e recuperar o certificado correspondente.</li>
  
  
  <h4><a href="https://github.com/pedro-hnrq/Proj_Event/tree/main/cliente">Cliente</a></h4>
  <li align="justify">Meus Certificados: é responsável por retornar uma lista de certificados relacionados ao usuário que fez a requisição aos eventos. Essa lista é filtrada utilizando o objeto "Certificado" do modelo definido na aplicação "eventos".</li>
  <li align="justify">Gerenciar: essa funcionalidade permite obter os eventos criados pelo usuário e paginá-los. É possível filtrar os eventos pelo nome através da barra de pesquisa disponível na página. A visualização dos eventos é limitada a um número pré-determinado, mas é possível navegar entre as páginas.  Além disso, essa funcionalidade utiliza as seguintes: </li>
  <ul>
  <li align="justify">Editar Eventos: é responsável por editar um evento específico. Ela é ativada quando o usuário clica no botão "Editar" na página de gerenciamento de eventos. É possível alterar o nome, descrição, data de início, data de término, carga horária e cores (principal, secundária e de fundo) do evento. Também é possível modificar a logo do evento, desde que ela tenha tamanho máximo de 10MB. Ao final da edição, o usuário é redirecionado para a página de gerenciamento de eventos.</li>
  <li align="justify">Excluir Eventos: é responsável por excluir um evento específico. Ela é ativada quando o usuário clica no botão "Excluir" na página de gerenciamento de eventos.</li>
  

</ul>
</ul>

<h3>Conclusão</h3>
<p align="justify">Em suma, o projeto Type Event oferece uma solução completa e personalizada para gerenciamento de eventos e certificados de participação, utilizando Python, Django e a biblioteca PIL para geração de certificados personalizados e exportação de arquivos CSV. As etapas fornece uma solução completa e personalizada para gerenciamento de eventos e certificados de participação, com funcionalidades que incluem autenticação de usuários, cadastro e gerenciamento de eventos (edição e exclusão), inscrição de participantes, geração de certificados, exportação de listas de participantes em CSV, entre outras.</p>
  
  

