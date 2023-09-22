
<h1 align="center"> ~ YOLOv8Train ~ </h1>

# Data Set

  Na construção dos modelos de IA, foram utilizados dois grupos de datasets. O primeiro refere-se à detecção de pessoas, enquanto o segundo diz respeito à classificação de quedas. A seguir, esses datasets serão descritos, identificados, categorizados e os métodos de carregamento serão detalhados. Além disso, neste repositório, serão referenciados os métodos de normalização e a sua compreensão para a identificação do uso correto.

  ## Detecção
    
   Para a detecção, foi utilizado o dataset disponibilizado pelo próprio Google através da ferramenta OIDv4. Você pode encontrar mais informações sobre ele no seguinte link. Para o download de imagens contendo seus respectivos labels que mapeiam os quadros onde as pessoas estão localizadas e seu estado, inicialmente preparamos o OIDv4 Toolkit para posteriormente ralizar o download do dataset. Para isso, siga os comandos exigidos pelo programa:
    
  - INSTALAÇÃO
    
    1. Clone este repositório
        ```bash
        git clone https://github.com/EscVM/OIDv4_ToolKit.git
        ```
    2. Entre na pasta clonada
        ```bash
        cd OIDv4_ToolKit
        ```
    3. Instale os pacotes necessários
        ```bash
        pip3 install -r requirements.txt
        ```
    
  - DOWNLOAD
    
   Para o download, inicialmente devemos saber que o nome do dataset que iremos baixar se chama "Person". Com esse dado, usamos os comandos disponibilizados no repositório do programa e selecionamos a função de download all, baixando assim todas as imagens referentes à classe pessoa.
      ```Cmd
      python main.py downloader --classes Person --type_csv all
    
  O comando baixará todos os dados localizados na pasta "OIDv4_ToolKit\OID\Dataset". Nessa pasta, você encontrará três subdiretórios: "treinamento", "teste" e "validação". Inicialmente, realizaremos o treinamento com um número limitado de dados. Posteriormente, o próximo modelo utilizará não apenas o conjunto de dados completo, mas também incorporará a aplicação de interferências ambientais e elétricas para aprimorar a robustez do programa final.
  - NORMALIZAÇÂO<br>
    Para a normalização deste dataset, foram utilizados três códigos em Python. O primeiro código imprime o rótulo na imagem usando os próprios pixels para verificar se o dataset utiliza o padrão de localização e tamanho absoluto da imagem para mapear. Posteriormente, convertemos este rótulo para o formato exigido pelo YOLO, que é (x central, y central, altura, largura), sendo que a altura e largura se referem do ponto central até a borda. Esse processo de conversão foi guiado pelas especificações fornecidas no utilitário e no próprio repositório e site do YOLO, que descrevem o formato do mapeamento, bem como os valores numéricos, já que o YOLO não utiliza pixels, mas sim porcentagens em relação à posição.
    
    Posteriormente, verificamos se o resultado foi obtido corretamente, imprimindo o quadro usando os parâmetros do tipo (xc, yc, h, w) em porcentagem. Se for verificado que está funcionando corretamente, podemos continuar.
    
    Esses códigos estão disponíveis em outro repositório, onde são descritos integralmente todos os elementos e cuidados, além de uma descrição de transformação mais técnica. Você pode encontrar mais informações e o link na imagem abaixo: 
            
