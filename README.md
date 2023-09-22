# YOLOv8Train
 1.DATA-SETS
  Na construção dos modelos de IA, foram utilizados dois grupos de datasets. O primeiro refere-se à detecção de pessoas, enquanto o segundo diz respeito à classificação de quedas. A seguir, esses datasets serão descritos, identificados, categorizados e os métodos de carregamento serão detalhados. Além disso, neste repositório, serão referenciados os métodos de normalização e a sua compreensão para a identificação do uso correto.

 - Detecção
  
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
      ```
      O comando baixará todos os dados localizados na pasta "OIDv4_ToolKit\OID\Dataset". Nessa pasta, você encontrará três subdiretórios: "treinamento", "teste" e "validação". Inicialmente, realizaremos o treinamento com um número limitado de dados. Posteriormente, o próximo modelo utilizará não apenas o conjunto de dados completo, mas também incorporará a aplicação de interferências ambientais e elétricas para aprimorar a robustez do programa final.
  - NORMALIZAÇÂo
      
