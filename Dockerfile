#iniciar no shell a criação do conteiner
#sudo docker build -t quarta-integracoes .


#lsb_release -a >> versão utilizada no momento do versionamento >> ubuntu:22.04
FROM ubuntu:22.04

WORKDIR /trabalho-integracaosftw

ADD . /trabalho-integracaosftw

RUN apt update
RUN apt install -y python3 python3-pip make
RUN pip install flask


# RODAR O CONTAINER E INDICAR QUAL PORTA DE DENTRO QUE ELE VAI TRANSMITIR PRA FORA
# sudo docker run -p 5000:5000 -it quarta-integracoes

CMD ["make", "dev"]
