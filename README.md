# DevMap 🎯  

## Sobre o Projeto  
O **DevMap** é uma plataforma web desenvolvida para otimizar a distribuição de tarefas em equipes de desenvolvimento com base nas habilidades individuais de cada membro. O sistema permite que desenvolvedores cadastrem suas competências técnicas, facilitando a alocação eficiente em projetos e a distribuição adequada de tickets baseada em suas especialidades.  

### 🧪 Exemplo Prático  
Um desenvolvedor com experiência em design e conhecimentos sólidos em HTML/CSS será naturalmente direcionado para tarefas de front-end, recebendo tickets relacionados à interface e experiência do usuário. Isso garante que cada membro da equipe trabalhe em áreas onde pode contribuir melhor.  

---

## Funcionalidades Principais  
- 🔐 Autenticação simplificada com Google  
- 📊 Mapeamento detalhado de habilidades por categoria  
- 📈 Níveis de proficiência (Básico, Intermediário, Avançado)  
- 👥 Perfil técnico detalhado para cada membro da equipe  
- 🎯 Distribuição inteligente de tarefas baseada em competências  

---

## Tecnologias Utilizadas  

### Backend  
- Python 3.13  
- Django 5.2  
- Django AllAuth (Autenticação Social)  
- SQLite3 (Banco de Dados)  

### Frontend  
- HTML5  
- CSS3  
- Bootstrap 5  
- Font Awesome  

---

## 📍 Evoluções Planejadas  
- 📋 Sistema de tickets integrado  
- 👥 Formação automática de equipes baseada em competências  
- 📊 Dashboard de distribuição de habilidades por equipe  
- 🔄 Recomendação inteligente de alocação de tarefas  
- 📈 Análise de gaps de habilidades na equipe  
- 🎯 Matching de desenvolvedores com projetos  
- 📱 Interface responsiva aprimorada  
- 🔍 Busca avançada de talentos por habilidade  

---

## 🚀 Como Executar o Projeto  

### 1. Clone o repositório    
`git clone https://github.com/seu-usuario/DevMap.git`
`cd DevMap`

# Criar ambiente virtual  
`python -m venv venv`

# Ativar ambiente virtual (Windows)  
`venv\Scripts\activate`  

# Instalar dependências
`pip install -r requirements.txt`

# Aplicar as migrações
`python manage.py migrate`

# Executar o projeto
`python manage.py runserver` 

🔐 Configuração do Google OAuth
# Acesse o Google Cloud Console
Crie um novo projeto

Vá em APIs e Serviços > Credenciais

Crie um novo ID do cliente OAuth 2.0 com o tipo Aplicativo Web

Configure os URIs de redirecionamento autorizados:


http://localhost:8000/accounts/google/login/callback/
No Django Admin
Acesse http://localhost:8000/admin

Em Sites, adicione localhost:8000

Em Social Applications:

Provedor: Google

Nome: Google

ID do Cliente: (insira o ID do Google Cloud)

Chave Secreta: (insira a chave secreta do Google Cloud)

Sites: selecione localhost:8000

🤝 Contribuindo
Contribuições são bem-vindas!

Faça um Fork do projeto

Crie uma branch para sua ideia

`git checkout -b feature/NovaIdeia`
Commit suas mudanças

`git commit -m 'Add NovaIdeia'`
Push para a branch

`git push origin feature/NovaIdeia`
Abra um Pull Request


📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.