# README e Markdown ✔

> **Bem Vindo** ao meu repositório, vou estar listando aqui diversas marcações de Markdown e informações sobre **git**.

## Aprendendo sobre Git na CLI 😜
Antes de começar, certifique-se de instalar o [Git](https://git-scm.com/downloads) no site oficial. 

Basta apenas baixar o instalador e prosseguir, ceritfique-se de habilitar a opção de adicionar ao "menu de contexto" no Windows e mudar o editor de texto padrão para maior facilidade no uso do Git.

### Inicializando um repositório

```bash
# Crie um diretório para seu primeiro repositório, mkdir = makedir ou criar diretório

mkdir Cats

# Navegue até o diretório com cd, change directory ou mudar diretório
cd Cats/

# Verifique a versão do Git
git --version

# Defina seu usuário e email em escopo global, eles serão usados para identificação no ecossistema do Git
git config --global user.name "Usuário"
git config --global user.email "Email"

# Retire o param global e o usuário será utilizado somente no repositório especifico, salvo no git config local

# Verifique as configurações do git
git config --list

# Inicialize o git no repositório, --initial-branch=main para criar a ramificação principal com esse nome
git init --initial-branch=main
# ou
git init -b main

# Verifique o status do projeto, se contém modificações ou novos arquivos
git status

# Veja se o arquivo .Git foi criado, lista todos os arquivos incluindo arquivos ocultos
ls -a

# Retorna um manual para comandos do Git, utilize com outros comandos para obter ajuda sobre eles.
git --help
```
### Criando Commits
```bash
# Atualize a hora de modificação de um arquivo, ou crie se não existir.
touch index.html

# Verifique o status do Git
git status

# Adicione o arquivo para a commit
git add index.html

# Apaga o arquivo, removendo do versionamento também
git rm index.html

# ou a pasta atual inteira
git add .

# Faça o commit com uma mensagem, indicando a ação que será realizada nesse commit.
# Exemplo: "Criar index.html"

git commit -m "Create index.html"
# -m indica a mensagem a seguir, tente ser objetivo

# Use a opção -a para automaticamente adicionar arquivos modificados para o próximo commit
git commit -a -m "Create a Heading to index.html"

# Comitando espaços vazios com .git-keep
mkdir pasta
touch pasta/.git-keep


# Removendo versionamento de repositórios
rm -rf .git/
```

### Logs do Git
```bash
# Visualize a diferença do arquivo atual com o último commit
git diff


# Criando o .gitignore
nano .gitignore
# Arquivo que define os tipos de arquivos a serem ignorados ao adicionar para commit

# Leia o log
git log
# Leia o log em linhas únicas
git log --oneline
# Leia os n'x' últimos logs
git log -n2
# Leia o log completo de todas as alterações (Caso a árvore seja restaurada 
# a uma versão anterior).
git reflog

```

### Repositórios Remotos
```bash
# Clone um repositório para sua máquina
git clone url_ou_path
# No processo uma referência à origem é criada e denominada origin

# Também é possivel selecionar a branch para clonar
git clone url --branch nome_branch --single-branch

# O comando pull copia somente arquivos novos e faz o check-in na árvore
git pull url

# Procura por alterações no origin
git fetch url
# Utilizado com git diff para verificar as diferenças entre versões
git diff branch origin/branch
# Mescla essas alterações ao seu repositório
git merge url

# Envia mudanças ao repositório remoto
git push url

# Para enviar uma solicitação para incorporar o código no projeto original, é necessário fazer um pedido antes, para ser analisado e então integrado ao código original
git request-pull -p origin/main .

# Crie um repositório remoto
git remote add nome_repositorio caminho_guardar_remoto

# Esse repositório remoto funciona desde que estejam na mesma rede
git pull nome_repositorio main

# Caso contrário será necessário um repositório central, como o GitHub
git remote add origin URL
```

### Branches com Git
```bash
# Criando uma nova branch
git branch nome_branch
# ou
git checkout -b nome_branch
# Tanto a main quanto a nova branch vão apontar para o commit mais recente

# Para trocar para a nova branch
git checkout nome_branch

# Atualizando a main
git checkout main
git merge nome_branch

# Veja as branches disponiveis, -v para listagem completa
git branch -v

# Delete a branch
git branch -d nome_branch

# Para alterações com repositorios desatualizados, podemos salvar as alterações atuais (antes do commit) e então realizar um pull
git stash
git pull

# Logo após, aplique suas alterações e exclua o "save"
git stash pop
# ou só aplique as modificações
git stash apply

# Ver modificações guardadas
git stash list

# Esses comandos também são usados ao trocar de branch, se a alteração não foi
# commitada e você deseja trocar de branch, salve-as antes para não perder.
```

Esse foi o ***getting started***, para se aprofundar mais em Git e seus comandos veja a documentação oficial do software.

## Utilizando Markdown ❤
 
**Negrito**:

    **Negrito** ou __Negrito__

*Itálico*:

    *Itálico* ou _Itálico_
    
***Ambos***:

	  ___negrito-itálico___ ou ***negrito-itálico***

~~Texto excluido~~:

    ~~texto excluido~~

Títulos:

     # Título nivel 1
     ## Título nivel 2
     ### Título nivel 3
     #### Título nível 4
     ##### Título nível 5
     ###### Título nível 6

# Título nivel 1
## Título nivel 2
### Título nivel 3
#### Título nível 4
##### Título nível 5
###### Título nível 6

Linha Horizontal:

    ---
    ***
---

Listas Enumeradas:

    1. Teste1
    2. Teste2
       1. Teste3 - Três espaços para transformar em sub-item

  1. Teste1
  2. Teste2
     1. Teste3 - Três espaços para transformar em sub-item

Listas Demarcadas:

    * Teste
    * Teste
       * Teste
    - Teste
       - Teste

   * Teste
   * Teste
      * Teste
   - Teste
      - Teste

Lista de Tarefas:

    - [x] Criar página principal
    - [] Criar página da loja
    - [] Finalizar a reunião  com o cliente

  - [x] Criar página principal
  - [] Criar página da loja
  - [] Finalizar a reunião  com o cliente

Links:

    [Acesse meu Github](https://github.com/Gabryel-Barboza)
 
  [Acesse meu Github](https://github.com/Gabryel-Barboza)
    
Imagens:

		![Texto alternativo](link)
		
  Pule uma linha entre elementos para indicar quebra de linha
  
![Imagem do Git](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi0.wp.com%2Fborrowbits.com%2Fwp-content%2Fuploads%2F2016%2F06%2Fgit-goodness-1.png%3Fw%3D1600%26ssl%3D1&f=1&nofb=1&ipt=8e8150732cf8590d6e0ca7c4ca3fb12b50dc9bbd63abc4b822c331e042c8b6e2&ipo=images)

Tabelas:

    Número | Nome | Nota
    ---|---|---
    1 | Gustavo | 8,5
    2 | José | 10,0
    3 | Maria | 9,0

 Número | Nome | Nota
 ---|---|---
 1 | Gustavo | 8,5
 2 | José | 10,0
 3 | Maria | 9,0

Códigos:

    `document.getElementById()`
    
    ```python
    num = int(input("Digite um valor: "))
    if num % 2 == 0:
        print(f"O valor {num} é Par")
    else:
        print(f"O valor {num} é Ímpar")
    ```
    
   `document.getElementById()`
   ```python
   num = int(input("Digite um valor: "))
   if num % 2 == 0:
       print(f"O valor {num} é Par")
   else:
       print(f"O valor {num} é Ímpar")
   ```

Emojis:

    Olá, pequeno Gafanhoto :vulkan_salute: :hand:
    
  Olá, pequeno Gafanhoto :vulkan_salute: :hand:

Citações:

    @Gabryel-Barboza
    > Qualquer Coisa
    > Respondendo alguém em Issues

@Gabryel-Barboza

> Qualquer Coisa

> Respondendo alguém em Issues
