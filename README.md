# 🎬 Projeto Integrador – Cloud Developing 2025/1

> CRUD simples + API Gateway + Lambda `/report` + RDS + CI/CD (Jenkins)

---

## 👥 Grupo

| RA | Nome | Responsabilidade |
|----|------|------------------|
| 10426930 | **Leonardo De Castro Tonon** | Backend, Docker, EC2, Jenkins |
| 10417578 | **João Pedro Fernandes Milhomens** | Integração API / Front-end |
| 10417821 | **Marcel Nobrega Zamboni** | Banco de Dados, RDS, Relatórios |


---

## 🧩 1. Visão Geral

**Domínio escolhido:** Catálogo de Filmes 🎥  
**Motivação:** Aplicação simples para demonstrar um fluxo completo de nuvem — CRUD, persistência, automação e endpoint de relatório.

### Funcionalidades

- **Entidade principal:** `Filme`
- **Campos:** `id`, `titulo`, `diretor`, `genero`, `anoLancamento`, `avaliacao`
- **Operações entregues (4 obrigatórias):**
  1. **Listar filmes** (`GET /filmes`)
  2. **Criar filme** (`POST /filmes`)
  3. **Atualizar filme** (`PUT /filmes/{id}`)
  4. **Excluir filme** (`DELETE /filmes/{id}`)



---

## ☁️ 2. Arquitetura

| Camada | Serviço | Descrição |
|--------|----------|-----------|
| **Frontend** | HTML/CSS/JS (EC2 - Spring Boot Static) | Interface do Catálogo de Filmes exibida pelo navegador |
| **Backend (API REST)** | EC2 + Docker (Spring Boot) | Fornece endpoints CRUD `/filmes` e conecta ao RDS |
| **Banco de Dados** | Amazon RDS (MySQL) | Armazena os dados dos filmes em subnet privada |
| **Gateway** | Amazon API Gateway | Faz proxy das rotas `/filmes` → EC2 e `/report` → Lambda |
| **Relatórios** | AWS Lambda `/report` | Gera estatísticas e top 10 filmes a partir do RDS |
| **CI/CD** | Jenkins + CodePipeline | Build automático do Gradle, geração da imagem Docker e deploy na EC2 |

---

- **Backend:** Spring Boot (Java 21) rodando em Docker na EC2  
- **Banco:** MySQL hospedado no RDS (subnet privada)  
- **Gateway:** Amazon API Gateway  
  - Rota `/filmes` → proxy para EC2  
  - Rota `/report` → Lambda (consulta e gera relatório)  
- **Lambda `/report`:** conecta ao RDS e retorna estatísticas em JSON  
- **CI/CD:** Jenkins em container → build com Gradle → imagem Docker → deploy na EC2  

---

### 🗺️ Diagrama de Arquitetura

```mermaid
flowchart LR
    subgraph VPC
        subgraph Public_Subnet
            User((Usuário)) -->|HTTPS| APIGW[API Gateway]
            APIGW -->|/filmes| EC2[EC2 com Docker e Spring Boot]
            APIGW -->|/report| LAMBDA[AWS Lambda]
            EC2 -->|JDBC| RDS[(RDS MySQL)]
            LAMBDA -->|PyMySQL| RDS
            JENKINS[Jenkins CI/CD] -.-> EC2
        end
        subgraph Private_Subnet
            RDS
        end
    end

