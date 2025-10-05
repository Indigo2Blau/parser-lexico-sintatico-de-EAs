Para rodar localmente execute ou o arquivo compilar ou testes, aquele te dá acesso a uma aba iterativa estilizada e este uma série de destes de comportamento unificados, tanto para as monadas, quando para os algoritmos.


O parser para Expressões Algébricas com notação intrafixa suporta: ., +, -, x, /, ^, (, ), floats, ints.


O parser iterativo tem uma ideia diferente por trás, visto que ',' faz parte da sua grámatica, assim um parser não é totalmente integrado com o outro, cada um tendo escopos diferentes. 
O iterativo é capaz de interpretar e avaliar notação préfixa. Usando parser guloso e stack de números. Suportanto em sua grámatica: +, *, -, ^, floats, ints.
