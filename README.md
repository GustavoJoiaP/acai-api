# Estudando o Monolíto em Camadas

## Projeto Monolíto com foco no Dominio de um ponto comercial de Açai 

O projeto tem como principal objetivo a implementação Monolítica baseado em principais da Arquitetura Hexagonal.

## O que é o Monolitoco?
- "Arquitetura Monolítica é um sistema único, não dividido, que roda em um único processo, uma aplicação de software em que diferentes componentes estão ligados a um único programa dentro de uma única plataforma."
- Atualmente, após o lançamento da Amazom e do Netflix utilizando a arquitetura em Microsserviços, a comunidade da Porgramação direcionou-se para implementações e estudos com foco em serviços separados.
- No entanto, todo e qualquer implementação de Software tem que ser estudada para realizar a arquitetura e design da Aplicação, ou seja, não existindo uma "Bola de Prata".

## Beneficios que o Monolíto Oferece
- Implantação fácil – Um arquivo ou diretório executável facilita a implantação.
- Desenvolvimento – Quando um aplicativo é construído com uma base de código, é mais fácil de desenvolver.
- Desempenho – Em uma base de código e repositório centralizados, uma API geralmente pode executar a mesma função que várias APIs executam com microsserviços.
- Teste simplificado – Como um aplicativo monolítico é uma unidade única e centralizada, o teste de ponta a ponta pode ser executado mais rapidamente do que com um aplicativo distribuído. 
- Fácil depuração – Com todo o código localizado em um só lugar, é mais fácil seguir uma solicitação e encontrar um problema.

## Desvantagens que o Monolíto Oferece
- Velocidade de desenvolvimento mais lenta – Um aplicativo grande e monolítico torna o desenvolvimento mais complexo e mais lento.
- Escalabilidade – Você não pode dimensionar componentes individuais.
- Confiabilidade – Se houver um erro em algum módulo, isso pode afetar a disponibilidade de toda a aplicação.
- Barreira à adoção de tecnologia – Quaisquer alterações na estrutura ou na linguagem afetam todo o aplicativo, tornando as alterações muitas vezes caras e demoradas.
- Falta de flexibilidade – Um monólito é limitado pelas tecnologias já utilizadas no monólito.
- Implantação – Uma pequena alteração em um aplicativo monolítico requer a reimplantação de todo o monólito.
- Manutenção — Se o aplicativo for muito grande e complexo para ser totalmente compreendido, é difícil fazer alterações rápidas e corretas.

## Monolíto em Camadas
É possível criar Monólitos bem estruturados. Uma maneira comum de organizar um monólito é usar camadas: cada camada provê um serviço para a camada de cima e é um cliente das camadas de baixo.

O grande costume da comunidade é utilizar o código de uma aplicação estruturada em 3 camadas:

- _Camada de Apresentação_: É a camada responsável pela interação do usuário com o sistema, apresentando informações e recebendo comandos.
- _Camada de Negócio_: É a camada que contém a lógica de negócios do sistema, implementando a funcionalidade específica do domínio do problema.
- _Camada de Persistência_: É a camada que gerencia a persistência de dados do sistema, incluindo a leitura e gravação de dados em bancos de dados ou outros tipos de armazenamento.

Algumas implementações de arquitetura de camadas podem incluir camadas adicionais, como uma camada de serviços ou uma camada de infraestrutura.
O principal objetivo da arquitetura de camadas é separar as *PREOCUPAÇÕES* do sistema em níveis distintos de abstração, permitindo  que cada camada seja implementada, testada e mantida de forma independente das outras. Isso facilita a escalabilidade, o teste e a manutenção do sistema, além de melhorar sua modularidade e flexibilidade.

