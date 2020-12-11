# Starting
Para iniciar a aplicação, é necessário o comando ``` python manage.py seed ```

## API Endpoints

```/sports``` retorna uma lista com todos os **sports** e seu respectivo **game**

```/events``` retorna uma lista com todos os **events** com seu respectivo **sport** e **game** daquele sport

```/athletes``` (demora em torno de 2 minutos para retornar) retorna uma lista com todos os **athletes** e suas respectivas informações, incluindo o **NOC** de que faz parte



## Resumo
Como não tenho experiência com back-end e venho estudando ainda na Kenzie, tive bastante dificuldades para fazer o teste. Infelizmente não consegui terminar e adicionar todas as features solicitadas. Sei que tem muito o que melhorar no app em questões de performance, organização e etc, porem irei entregar até aonde consegui fazer e da maneira que consegui implementar.
Pretendo finalizar o teste futuramente com todas as features/rotas e implementar Testes Unitários, Deploy Heroku, CL/CI.

## Dificuldades
A parte de Modelagem de Banco com certeza foi onde mais tive dificuldades, a primeira vista o exercício não parece ser tão complexo, mas logo percebi detalhes que iriam deixar a coisa interessante, como a idade do atleta que aumenta de acordo com os anos, e até atletas com o mesmo nome!
