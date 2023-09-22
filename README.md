# YOLOv8Train
Na construção dos modelos de IA, foram utilizados dois grupos de datasets. O primeiro se refere à detecção de pessoas, enquanto o segundo diz respeito à classificação de quedas. A seguir, esses datasets serão descritos, identificados, categorizados, e seus métodos de carregamento serão detalhados. Além disso, neste repositório, serão referenciados os métodos de normalização e sua compreensão para a identificação do uso correto.
## Detecção
  para a deteção foi utilizado o dataset dimponivilizado pelo proprio google atravez da feramento OIDv4, pode se verificar mais referencia sobre tal no seguinte link. Para o dawload de imagens contendo sus respectivos label que mapeima os     quadros onde estão localizadas a as pessoas e seu estado, incialmente PREPARAMOS O oidV4 TOOLKIT PARA RALIZAR posteriormente o dawload do dataset, para isto seguem os comandos exigidos pelo programa
  
 -  INSTALAÇÂO
      
    1. Clone this repository
    ```bash
    git clone https://github.com/EscVM/OIDv4_ToolKit.git
    ```
    2. Install the required packages
    ```bash
    pip3 install -r requirements.txt
    ```
- dawload
    para o dawload iniclkammente temos que saber que o nome do dataset que iremos baixar se chama "Person", com esse dado usamos os cmoandos disponiblizado no repositorio do programa e selecioanmos a função de dawload all, dasta faomra baixando todoas as imagens referentes a clase pessoa.
  ```Cmd
    python main.py downloader --classes Person --type_csv all
    ```
## Clasificação
