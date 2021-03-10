## Questão 1

Após a conexão entre o cliente e o servidor, o cliente consegue acessar métodos e atributos 
marcados como expostos(prefixo "exposed_") na implementação server-side. Logo, a informação mostrada
no stdout do cliente diz respeito, respectivamente: 
    - ao objeto "root" que referencia o serviço executado no servidor, 
a partir desse objeto é possível acessar métodos e atributos expostos no serviço;
    - ao retorno do método "get_answer" exposto dentro do processo server-side;
    - o valor da variável exposta "the_real_answer_though" dentro de MyService.

## Questão 2

Nesse caso a execução do cliente foi interrompida devido ao erro "AttributeError" não tratado.
O cliente tentou executar o código que faz referência à um método não exposto no servidor. Nesse caso,
o objeto "root" não possui nenhuma referencia à esse método na memória, sendo assim, não é possivel executa-lo remotamente.

## Questão 3

O método de soma("sum_array") se encontra em ./server.py. o cliente referente a essa questão é o arquivo
client_q3.py

## Questão 4

O método de soma foi modificado para marcar o tempo de execução("sum_array_timed") e o mesmo se encontra em ./server.py.
o cliente referente a essa questão é o arquivo client_q4.py

O tempo marcado server-side foi 1.4539194s e no client-side foi 1.4617078s

## Questão 5

Executando o cliente em um container docker(virtualização) na mesma rede, tivemos um tempo de 1.948440s no client-side e em 
server-side local, um tempo de 1.943156s. Não satisfeito, resolvi testar o procedimento entre um cliente e servidor na mesma rede de uma VPC AWS, 
em North Virginia(us-east-1), entre máquinas diferentes. Obtive o tempo de execução para o servidor em média de 5.41025495529 e para o cliente, um 
tempo na média dos 5.41613364219s

[server log](https://lh6.googleusercontent.com/aekAf9egzcYnXj4Jr3VvD5zSXI_9Tw3aAyxQ5K_Q8f1UeKcs7v_rNvQqoOp_upAT4jswqsSpLE3GxOto6RBlk_9lMHGyZiZKTXHJIo9ku6jUxdeeyLqy_IG4lacKRTXucR-SiKaW)
<br>
[client log](https://lh4.googleusercontent.com/fq7cadH_gOFE0jV7dyLfJmcCFdceATMo7l1Chxdt3yxLw_CxphRgFapXzxEdnc5gu1u-lap9w4E3hSYUsQBb03dK7evmqYqDdY0dUpu6)

## Questão 6

O tempo de execução das instruções no cliente foi de 1.5150041580200195, e no servidor de 1.5113048553466797.

## Questão 7 e 8

### Mesma máquina

|    n        | 100           | 1000          | 10000          |
|:------------|:-------------:|:-------------:|:--------------:|
| server-side | 0.014939      | 0.149000      | 1.576465       |
| client-side | 0.018375      | 0.152526      | 1.582473       |

<br>
Nota-se que a diferença entre o cliente e o servidor é bem pequena, pois o cliente e o servidor estão sendo executados
na mesma máquina, ou seja, o tempo de requisição é mínimo, pois o client-side aponta para o localhost.
<br>
<br>

### Máquinas diferentes

|    X        | 100           | 1000          | 10000          |
|:------------|:-------------:|:-------------:|:--------------:|
| server-side | 0.051945      | 0.583914      | 6.247325       |
| client-side | 0.057946      | 0.589876      | 6.253410       |

<br>
A diferença entre as requisições continua pequena, mas aumentou bastante em porcentagem. Como a comunicação é
feita entre máquinas diferentes, o tempo de resposta entre servidor e cliente aumentou.
<br><br>

## Questão 9 e 10

Na tabela 2, podemos observar que quanto mais longe geograficamente uma máquina da outra, esse tempo de resposta tende a aumentar. Porém é um aumento ínfimo.
Pode ser devido a problemas no meio físico de transporte, perda de pacotes, interferência na rede, etc.
O processamento continua ocupando maior parte do tempo total de requisição entre cliente e servidor.

