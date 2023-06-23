# Programa de Consulta em Bases de Dados

Este programa realiza consultas em duas bases de dados (X e Y) usando a biblioteca `pymssql` do Python. Os resultados da consulta são salvos em um arquivo de texto.

## Pré-requisitos

- Python 3.x instalado
- Módulo `pymssql` instalado. Você pode instalá-lo usando o seguinte comando:


## Como usar

1. Clone ou faça o download deste repositório.

2. Abra um terminal e navegue até o diretório do programa.

3. Execute o programa usando o seguinte comando:

4. O programa solicitará a base de dados onde deseja realizar a consulta. Digite `X` para selecionar a base de dados 'bdX' e tabela 'tableX' ou `Y` para selecionar a base de dados 'bdY' e tabela 'tableY'.

5. Insira o número do bordero quando solicitado.

6. O programa executará a consulta e salvará os resultados em um arquivo de texto chamado 'relatorio.txt' no diretório do programa.

7. Após a conclusão da consulta, uma barra de progresso será exibida para indicar o carregamento do programa.

8. Quando o programa terminar de executar, será exibida uma mensagem "Pressione Enter para sair...". Pressione Enter para encerrar o programa.


## Observações

- Certifique-se de fornecer as informações corretas do servidor (DNS ou IP do servidor), nome de usuário e senha no código do programa antes de executá-lo.

- Certifique-se de ter permissão de acesso às bases de dados selecionadas.

- Verifique se a biblioteca `pymssql` está instalada corretamente antes de executar o programa.

- Os resultados da consulta serão salvos em um arquivo de texto separado por pipe (`|`), um resultado por linha.

- Em caso de opção inválida, o programa exibirá a mensagem "Opção inválida." e será encerrado.

- Em caso de erros durante a execução, o programa fornecerá mensagens de erro informativas para ajudar na resolução dos problemas.



