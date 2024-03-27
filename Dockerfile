#iniciar no shell a criação do conteiner
#sudo docker build -t quarta-integracoes .


#lsb_release -a >> versão utilizada no momento do versionamento >> ubuntu:22.04
FROM ubuntu:22.04

#criação da pasta "trabalho-integracaosftw"
WORKDIR /trabalho-integracaosftw

#adicionando o script de python para a criação do banco de dados (vamos usar SQLite)
ADD . /trabalho-integracaosftw

#instalando o que precisa para rodar a aplicação no container
RUN apt update
RUN apt install -y python3 python3-pip make
RUN pip install flask


# RODAR O CONTAINER E INDICAR QUAL PORTA DE DENTRO QUE ELE VAI TRANSMITIR PRA FORA
# sudo docker run -p 5000:5000 -it quarta-integracoes

CMD ["make", "dev"]
