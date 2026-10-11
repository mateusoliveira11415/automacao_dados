# Fox Scriptor - Interprete. Estruture. Escreva

## Sobre o projeto

O _Fox Scriptor_ surgiu a partir da necessidade de **automatizar um processo de interpretação e transcrição de dados**.

Inicialmente, o processo consistia em consultar diversos registros em um banco de dados, interpretar manualmente a situação de cada registro e transcrever essa interpretação para uma planilha separada.

Ao analisar esse processo, foi identificado que grande parte das interpretações seguia estruturas semânticas semelhantes, variando principalmente nos dados utilizados para preencher essas estruturas.

A partir dessa observação, foi desenvolvido um sistema capaz de receber dados condensados em um arquivo `.txt`, interpretá-los, processá-los e transformá-los automaticamente em conteúdo textual estruturado, reduzindo a necessidade de realizar manualmente tarefas repetitivas de transcrição.

O projeto encontra-se em evolução e tem como objetivo ampliar esse conceito para uma aplicação mais flexível, configurável e acessível por meio de uma interface gráfica.

## Como funciona

O _Fox Scriptor_ utiliza um arquivo de entrada (`encoded_data.txt`) contendo comandos compactos que descrevem qual conteúdo deve ser gerado e quais dados devem ser utilizados.

O arquivo `process_encoded_data.py` realiza a leitura desses comandos e identifica seu tipo a partir do primeiro caractere de cada linha. Comandos iniciados por um número são encaminhados para o processamento simples ou composto, enquanto comandos iniciados por uma letra minúscula são encaminhados para o processamento complexo.

Após a identificação, o comando é processado pelas funções presentes em `write_functions.py`. Essas funções consultam os dicionários configurados em `configs/context.json`, obtêm o modelo textual correspondente e substituem seus marcadores pelos dados fornecidos no comando.

Os marcadores seguem o formato `.0.`, `.1.`, `.2.` e assim por diante. Cada marcador representa uma posição nos dados fornecidos pelo comando. Dessa forma, um mesmo modelo textual pode ser reutilizado com diferentes informações sem que seja necessário alterar o código-fonte.

Depois de gerar o texto final, o Fox Scriptor utiliza `pyautogui` e `pyperclip` para realizar a interação automatizada com o ambiente de destino: copia o conteúdo gerado para a área de transferência, utiliza os atalhos configurados e insere o texto automaticamente.

As configurações utilizadas pelo sistema são mantidas separadamente da lógica de processamento. O arquivo `context.json` contém os modelos textuais e outras configurações de contexto, `error_messages.json` contém as mensagens de erro e `hot_keys.json` define os atalhos utilizados pela automação.

De maneira simplificada, o fluxo de processamento pode ser representado da seguinte forma:

`encoded_data.txt`
→ leitura do comando
→ identificação do tipo
→ processamento
→ consulta aos modelos
→ substituição dos parâmetros
→ geração do texto
→ automação da entrada

Essa estrutura permite separar os dados utilizados pelo sistema de sua lógica de processamento, tornando possível modificar modelos, mensagens e atalhos sem alterar diretamente as funções responsáveis pela execução.

## Estrutura do projeto

O projeto está organizado de forma a separar o processamento dos comandos, as funções auxiliares e os arquivos de configuração.

```text
automacao_dados/
│
├── auto_process/
│   ├── functions/
│   │   ├── __init__.py
│   │   ├── reader_configs.py
│   │   └── text.py
│   │
│   ├── process_encoded_data.py
│   └── write_functions.py
│
├── configs/
│   ├── context.json
│   ├── error_messages.json
│   └── hot_keys.json
│
├── encoded_data.txt
│
└── modify_context_funcs.py
```

### `auto_process/`

Contém a lógica principal responsável por interpretar os comandos e gerar os textos.

`process_encoded_data.py` é o ponto de entrada do processamento. Ele lê o conteúdo de `encoded_data.txt`, identifica o tipo de cada comando e encaminha cada linha para a função responsável pelo seu processamento.

`write_functions.py` contém as principais funções de processamento e automação. É responsável por interpretar os parâmetros recebidos, consultar os modelos configurados, substituir seus marcadores e inserir o resultado no ambiente de destino.

### `auto_process/functions/`

Contém funções auxiliares utilizadas pelo processamento principal.

`reader_configs.py` realiza a leitura dos arquivos de configuração e disponibiliza seus valores para os demais módulos.

`text.py` contém funções relacionadas ao tratamento do texto. Atualmente, sua principal responsabilidade é realizar a substituição dos marcadores presentes nos modelos textuais.

### `configs/`

Contém os dados de configuração utilizados pelo sistema.

`context.json` armazena os modelos textuais, organizados nos dicionários `simple_dicio`, `compound_dicio` e `complex_dicio`, além de configurações relacionadas ao processamento.

`error_messages.json` armazena as mensagens utilizadas para informar erros durante a interpretação dos comandos.

`hot_keys.json` define os atalhos de teclado utilizados pela automação.

### `encoded_data.txt`

É o arquivo utilizado como entrada para o processamento. Cada linha representa um comando que será interpretado pelo Fox Scriptor.

### `modify_context_funcs.py`

Contém funções destinadas ao gerenciamento das entradas dos dicionários presentes em `context.json`, permitindo listar, adicionar e remover pares de chave e valor.

Essas funções constituem uma base para o gerenciamento programático dos modelos utilizados pelo sistema.

## Sistema de comandos

O Fox Scriptor utiliza uma sintaxe baseada em valores separados por vírgulas. Cada linha de `encoded_data.txt` representa um comando independente.

O primeiro valor da linha determina o tipo de processamento que será realizado.

Atualmente, existem três tipos de comandos:

* comandos simples;
* comandos compostos;
* comandos complexos.

### Comandos simples

Comandos simples utilizam o formato:

```text
0,chave
```

O valor `0` identifica o comando como simples. O segundo valor corresponde à chave que será procurada no dicionário `simple_dicio` de `context.json`.

Por exemplo:

```text
0,1
```

Com a configuração:

```json
"simple_dicio": {
    "1": "Mensagem simples de chave 1"
}
```

o sistema localiza a chave `1` e utiliza o texto associado a ela.

Esse tipo de comando é utilizado quando o texto necessário já está completamente definido no modelo e não necessita receber parâmetros adicionais.

### Comandos compostos

Comandos compostos utilizam o formato:

```text
chave,quantidade_de_valores,valor_1,valor_2,...
```

Nesse caso, o primeiro valor identifica o modelo no dicionário `compound_dicio`, enquanto o segundo informa quantos valores deverão ser utilizados na substituição dos marcadores do texto.

Por exemplo:

```text
1,2,15,16
```

A primeira posição (`1`) identifica o modelo:

```json
"compound_dicio": {
    "1": "Mensagem composta de chave 1, dado1: .0.; dado2: .1."
}
```

O valor `2` informa que serão utilizados dois parâmetros. Os valores seguintes, `15` e `16`, substituem respectivamente `.0.` e `.1.`.

O resultado será equivalente a:

```text
Mensagem composta de chave 1, dado1: 15; dado2: 16
```

A quantidade de valores indicada no comando determina quantos marcadores serão processados, começando sempre por `.0.`.

### Comandos complexos

Comandos complexos possuem uma estrutura mais extensa e permitem gerar textos a partir de múltiplas partes.

Seu formato geral é:

```text
chave,quantidade_de_substituições,quantidade_de_iterações,ordenação,...
```

Após esses quatro valores iniciais, são fornecidos os parâmetros utilizados pelo modelo principal e pelas partes adicionais que serão inseridas durante as iterações.

Por exemplo:

```text
a,2,3,0,15,16,1,1,10,3,1,1,2,1,4
```

Nesse comando:

* `a` identifica o modelo principal;
* `2` indica a quantidade de valores utilizados pelo modelo principal;
* `3` determina a quantidade de iterações;
* `0` define que a numeração das iterações não será adicionada ao texto.

O modelo principal pode ser encontrado em `complex_dicio`:

```json
"a": ".0. Documentos em atividade de .1., "
```

Os dois valores seguintes, `15` e `16`, substituem `.0.` e `.1.`.

Após o processamento do modelo principal, o sistema utiliza uma chave secundária em cada iteração. Essa chave é concatenada à chave principal para localizar novos modelos no mesmo dicionário.

Por exemplo:

```text
a1
a2
a3
```

correspondem às seguintes entradas:

```json
"a1": ".0. cocumentos ativos; ",
"a2": ".0. documentos desativos; ",
"a3": ".0. documentos perdidos; "
```

Cada uma dessas partes possui sua própria quantidade de substituições e seus próprios valores.

A estrutura permite, portanto, combinar um modelo principal com diversas partes complementares, produzindo um texto final a partir de uma única linha de comando.

### Marcadores de substituição

Os modelos textuais utilizam marcadores numéricos no formato:

```text
.0.
.1.
.2.
...
```

A numeração indica a posição do valor que será utilizado na substituição.

Por exemplo, considerando o modelo:

```text
"Documento: .0.; responsável: .1."
```

e os valores:

```text
123,João
```

o resultado será:

```text
Documento: 123; responsável: João
```

Os marcadores são processados sequencialmente a partir de `.0.`. A quantidade de marcadores processados é determinada pelo parâmetro correspondente do comando.

### Identificação dos comandos

A classificação dos comandos é realizada pelo primeiro caractere da linha.

| Primeiro caractere | Tipo de comando     |
| ------------------ | ------------------- |
| Número             | Simples ou composto |
| Letra minúscula    | Complexo            |

Assim, uma linha iniciada por `0` ou `1` será encaminhada para o processamento simples/composto, enquanto uma linha iniciada por uma letra minúscula, como `a`, será encaminhada para o processamento complexo.

O sistema atualmente utiliza essa convenção para determinar qual estrutura de parâmetros deverá ser interpretada.

## Configuração

O comportamento do Fox Scriptor é parcialmente definido por arquivos JSON localizados no diretório `configs/`. Essa separação permite modificar modelos textuais, mensagens e atalhos sem alterar diretamente o código responsável pelo processamento.

### `context.json`

O arquivo `context.json` contém os modelos utilizados pelo sistema e algumas configurações gerais.

A estrutura atual é:

```json
{
    "additional_enter": true,
    "simple_dicio": {
        "1": "Mensagem simples de chave 1"
    },
    "compound_dicio": {
        "1": "Mensagem composta de chave 1, dado1: .0.; dado2: .1."
    },
    "complex_dicio": {
        "a": ".0. Documentos em atividade de .1., ",
        "a1": ".0. cocumentos ativos; ",
        "a2": ".0. documentos desativos; ",
        "a3": ".0. documentos perdidos; "
    }
}
```

O campo `additional_enter` determina se o sistema deverá pressionar `Enter` antes de inserir o texto gerado.

Os demais campos correspondem aos dicionários utilizados pelos diferentes tipos de comandos:

`simple_dicio` contém os modelos utilizados pelos comandos simples.

`compound_dicio` contém os modelos utilizados pelos comandos compostos.

`complex_dicio` contém os modelos utilizados pelos comandos complexos.

As chaves desses dicionários são utilizadas pelos comandos para localizar seus respectivos modelos.

### Criação de modelos

Para criar um novo modelo, basta adicionar uma nova chave ao dicionário correspondente.

Por exemplo:

```json
"simple_dicio": {
    "1": "Mensagem simples de chave 1",
    "2": "Novo modelo de mensagem"
}
```

O novo modelo poderá então ser utilizado por meio de:

```text
0,2
```

Modelos que necessitam receber informações variáveis podem utilizar os marcadores de substituição:

```text
.0.
.1.
.2.
```

Por exemplo:

```json
"compound_dicio": {
    "2": "O documento .0. pertence ao setor .1."
}
```

poderá receber os valores correspondentes por meio de um comando composto.

### `error_messages.json`

O arquivo `error_messages.json` contém as mensagens utilizadas quando ocorre um erro durante o processamento.

Atualmente são utilizadas três categorias principais:

```json
{
    "none_key": "!Chave Inexistente!",
    "index_error": "!Valores Insuficientes!",
    "value_error": "!Valor inválido para conversão!"
}
```

`none_key` é utilizado quando uma chave procurada não está presente no dicionário correspondente.

`index_error` é utilizado quando os valores fornecidos pelo comando são insuficientes para o processamento solicitado.

`value_error` é utilizado quando um valor não pode ser convertido para o tipo esperado pelo sistema.

Essas mensagens também podem ser alteradas diretamente no arquivo de configuração.

### `hot_keys.json`

O arquivo `hot_keys.json` armazena os atalhos utilizados pela automação.

A configuração atual é:

```json
{
    "init_0": ["ctrl", "alt", "right"],
    "init_1": ["alt", "tab"]
}
```

Esses valores são utilizados pelo `pyautogui` para executar os atalhos necessários durante a automação.

Dessa forma, os atalhos podem ser modificados de acordo com o ambiente em que o Fox Scriptor estiver sendo utilizado, sem que seja necessário alterar diretamente as funções Python.

### `modify_context_funcs.py`

O arquivo `modify_context_funcs.py` fornece funções para gerenciar os modelos presentes em `context.json`.

Atualmente, são disponibilizadas operações para:

* listar chaves e valores de um dicionário;
* adicionar uma nova chave e seu respectivo valor;
* remover uma chave existente.

Essas funções permitem modificar programaticamente o conteúdo de `context.json` e constituem a base para uma futura camada de gerenciamento mais acessível das configurações.

## Como executar

O Fox Scriptor atualmente é executado diretamente a partir do código-fonte.

Antes de iniciar, é necessário possuir uma instalação do Python compatível com o projeto e instalar as bibliotecas externas utilizadas pela automação.

As dependências externas utilizadas atualmente são:

```bash
pip install pyautogui pyperclip
```

Após instalar as dependências, mantenha a estrutura de diretórios do projeto preservada, pois os módulos utilizam caminhos relativos para acessar os arquivos de configuração e o arquivo de entrada.

O processamento é realizado a partir do arquivo:

```text
auto_process/process_encoded_data.py
```

Os comandos que deverão ser processados devem ser adicionados ao arquivo:

```text
encoded_data.txt
```

Cada linha desse arquivo representa um comando independente.

Com o ambiente configurado, execute o módulo de processamento a partir da raiz do projeto:

```bash
python auto_process/process_encoded_data.py
```

O programa irá ler as linhas de `encoded_data.txt`, identificar o tipo de cada comando, gerar os textos correspondentes e utilizar os atalhos e mecanismos de automação configurados para inseri-los no ambiente de destino.

### Atenção ao ambiente de execução

Como o Fox Scriptor utiliza `pyautogui` para controlar o teclado, sua execução depende do ambiente gráfico em que o programa estiver sendo executado.

O programa não apenas produz texto: ele também realiza ações de teclado e colagem. Portanto, o ambiente de destino deve estar preparado para receber essas ações quando o processamento for iniciado.

Os atalhos utilizados podem ser configurados em:

```text
configs/hot_keys.json
```

Os modelos e demais parâmetros podem ser configurados em:

```text
configs/context.json
```

As mensagens de erro podem ser configuradas em:

```text
configs/error_messages.json
```

## Exemplos

Os exemplos a seguir utilizam a configuração atualmente presente no projeto e demonstram os três tipos de comandos suportados pelo Fox Scriptor.

### Exemplo de comando simples

Considere o comando:

```text
0,1
```

O primeiro valor, `0`, indica que se trata de um comando simples. O segundo valor, `1`, corresponde à chave que será procurada em `simple_dicio`.

Com a configuração:

```json
"simple_dicio": {
    "1": "Mensagem simples de chave 1"
}
```

o texto gerado será:

```text
Mensagem simples de chave 1
```

Nesse caso, nenhum valor adicional precisa ser fornecido, pois o modelo já contém todo o conteúdo necessário.

### Exemplo de comando composto

Considere o comando:

```text
1,2,15,16
```

O primeiro valor, `1`, identifica o modelo em `compound_dicio`.

O segundo valor, `2`, determina que serão realizadas duas substituições.

Os valores `15` e `16` são utilizados para substituir os marcadores `.0.` e `.1.`, respectivamente.

Com o modelo:

```json
"1": "Mensagem composta de chave 1, dado1: .0.; dado2: .1."
```

o resultado será:

```text
Mensagem composta de chave 1, dado1: 15; dado2: 16
```

Assim, um único modelo pode ser reutilizado para diferentes conjuntos de dados.

### Exemplo de comando complexo

Um exemplo mais completo é:

```text
a,2,3,0,15,16,1,1,10,3,1,1,2,1,4
```

Os quatro primeiros valores definem a estrutura inicial do processamento:

```text
a    → chave do modelo principal
2    → quantidade de substituições do modelo principal
3    → quantidade de iterações
0    → não adicionar numeração às iterações
```

O modelo principal associado à chave `a` é:

```json
"a": ".0. Documentos em atividade de .1., "
```

Os valores `15` e `16` são utilizados para preencher seus marcadores, produzindo:

```text
15 Documentos em atividade de 16,
```

Em seguida, o sistema realiza três iterações. Em cada uma delas, uma chave secundária é fornecida para determinar qual modelo complementar deverá ser utilizado.

A sequência utilizada pelo exemplo é:

```text
a1 → 10
a3 → 1
a2 → 4
```

Os respectivos modelos são:

```json
"a1": ".0. cocumentos ativos; ",
"a2": ".0. documentos desativos; ",
"a3": ".0. documentos perdidos; "
```

Após as substituições, o texto final gerado pelo exemplo é:

```text
15 Documentos em atividade de 16, 10 cocumentos ativos; 1 documentos perdidos; 4 documentos desativos;
```

Esse exemplo demonstra uma das principais características dos comandos complexos: diferentes modelos podem ser combinados em uma única operação, utilizando dados distintos para cada parte do texto.

### Relação entre comando e configuração

Os exemplos demonstram que os comandos presentes em `encoded_data.txt` não armazenam diretamente todos os textos que serão produzidos. Eles funcionam como instruções que indicam ao sistema qual modelo utilizar e quais valores devem ser inseridos.

Dessa maneira, uma alteração no conteúdo de `context.json` pode modificar o texto produzido por um determinado comando sem que seja necessário alterar o próprio comando ou a lógica de processamento.

Essa separação entre instrução, dados e modelo textual é a base da estrutura atual do Fox Scriptor.

## Estado atual

O Fox Scriptor encontra-se em uma etapa inicial de desenvolvimento, com a estrutura fundamental do sistema de interpretação, processamento e automação já implementada.

Atualmente, o projeto é capaz de:

* ler comandos a partir de um arquivo `.txt`;
* identificar diferentes tipos de comandos a partir de sua estrutura;
* processar comandos simples, compostos e complexos;
* utilizar modelos textuais armazenados em arquivos de configuração;
* substituir marcadores por valores fornecidos nos comandos;
* realizar múltiplas substituições durante o processamento;
* combinar diferentes modelos em comandos complexos;
* configurar mensagens de erro separadamente da lógica principal;
* configurar os atalhos utilizados pela automação;
* utilizar `pyautogui` e `pyperclip` para automatizar a inserção do conteúdo gerado;
* listar, adicionar e remover entradas dos dicionários presentes em `context.json` por meio de `modify_context_funcs.py`.

A versão atual também já apresenta uma separação inicial entre lógica de processamento, funções auxiliares e dados de configuração. Essa organização permite que os modelos textuais e outros parâmetros sejam modificados sem a necessidade de alterar diretamente as funções responsáveis pelo processamento.

Apesar disso, o sistema ainda possui limitações. Sua utilização depende da edição manual dos arquivos de entrada e configuração, e a execução ainda ocorre diretamente pelo código-fonte. A interpretação dos comandos também depende de uma estrutura rígida de valores separados por vírgulas, o que limita a flexibilidade da entrada de dados.

Outro ponto importante é que o projeto ainda não possui uma interface gráfica para facilitar a configuração e o gerenciamento dos modelos. Atualmente, essas operações são realizadas diretamente pelos arquivos de configuração ou pelas funções disponíveis no código.

Portanto, a versão atual deve ser entendida como uma base funcional para o desenvolvimento de uma aplicação mais completa. O foco até este estágio está na construção e validação da lógica de interpretação, geração de texto e automação, enquanto aspectos relacionados à experiência de utilização, configuração e distribuição ainda permanecem em desenvolvimento.

## Próximos passos

O desenvolvimento do Fox Scriptor pretende ampliar a estrutura atual, transformando o protótipo de automação em uma aplicação mais flexível e acessível.

Entre os principais objetivos estão:

* desenvolver uma interface gráfica para facilitar a utilização do sistema;
* tornar o gerenciamento dos modelos e configurações mais acessível;
* ampliar a flexibilidade do sistema de comandos;
* melhorar o tratamento e a validação dos dados de entrada;
* aprimorar o gerenciamento dos modelos armazenados em `context.json`;
* reduzir a necessidade de interação direta com os arquivos de configuração;
* organizar a aplicação de forma a facilitar sua manutenção e evolução.

Esses objetivos poderão ser modificados ou ampliados conforme o desenvolvimento do projeto avance e novas necessidades sejam identificadas.

## Tecnologias utilizadas

O Fox Scriptor é desenvolvido em Python e utiliza bibliotecas e recursos voltados principalmente para processamento de dados, manipulação de texto e automação do ambiente gráfico.

### Python 

Linguagem principal utilizada no desenvolvimento do projeto. É responsável pela interpretação dos comandos, processamento dos dados, gerenciamento das configurações e execução da automação.

### JSON

Utilizado para armazenar configurações e modelos textuais de forma separada da lógica do programa.

Atualmente, o projeto utiliza arquivos JSON para:

* modelos e configurações de contexto;
* mensagens de erro;
* atalhos de teclado.

### PyAutoGUI

Biblioteca utilizada para realizar a automação das ações de teclado no ambiente gráfico.

### Pyperclip

Biblioteca utilizada para manipular a área de transferência, permitindo que os textos gerados sejam copiados e posteriormente inseridos pelo sistema.

### Git

Utilizado para controle de versão e acompanhamento da evolução do código-fonte durante o desenvolvimento do projeto.

## Especificações do documento

#### Data de criação

02 de outubro de 2026

#### Ultima alteração:

02 de outubro de 2026

#### Versão do documento:

v0.1