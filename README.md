<h1 align="center"> ~ YOLOv8Train ~ </h1>

# Conjunto de Dados

Para construir modelos de IA, utilizamos dois grupos de conjuntos de dados. O primeiro é destinado à detecção de pessoas, enquanto o segundo se concentra na classificação de quedas. Vamos descrever, identificar, categorizar esses conjuntos de dados e detalhar os métodos de carregamento. Além disso, neste repositório, forneceremos informações sobre a normalização e sua importância para garantir o uso adequado dos dados.

## Detecção de Pessoas

Para a tarefa de detecção de pessoas, utilizamos o conjunto de dados disponibilizado pelo Google por meio da ferramenta OIDv4. Você pode obter mais informações sobre este conjunto de dados [neste link](https://storage.googleapis.com/openimages/web/index.html). Para baixar imagens com suas respectivas etiquetas que indicam as áreas onde as pessoas estão localizadas e seu estado, siga as etapas abaixo:

### Instalação

1. Clone este repositório
   ```bash
   git clone https://github.com/EscVM/OIDv4_ToolKit.git
   ```

2. Acesse a pasta clonada
   ```bash
   cd OIDv4_ToolKit
   ```

3. Instale as dependências necessárias
   ```bash
   pip3 install -r requirements.txt
   ```

### Download

Para o processo de download, você precisará especificar que deseja baixar o conjunto de dados "Person". Use os comandos fornecidos no repositório da ferramenta e selecione a função "download all" para baixar todas as imagens relacionadas à classe "pessoa".
```Cmd
python main.py downloader --classes Person --type_csv all
```

O comando baixará todos os dados para a pasta "OIDv4_ToolKit\OID\Dataset". Dentro dessa pasta, você encontrará três subdiretórios: "treinamento", "teste" e "validação". Inicialmente, recomendamos o treinamento com um subconjunto limitado de dados. Posteriormente, o próximo modelo usará o conjunto de dados completo e incorporará perturbações ambientais e elétricas para aprimorar a robustez do programa final.

### Normalização

Para normalizar esse conjunto de dados, implementamos três códigos em Python. O primeiro código adiciona rótulos às imagens usando as coordenadas dos pixels para garantir que o conjunto de dados utilize o padrão de localização e tamanho absoluto da imagem para mapear objetos. Em seguida, convertemos esses rótulos para o formato exigido pelo YOLO, que é (x central, y central, altura, largura), onde a altura e a largura se referem às distâncias do centro até as bordas da caixa delimitadora. Essa conversão segue as especificações fornecidas no utilitário e no repositório/site oficial do YOLO, que descrevem o formato do mapeamento e os valores numéricos em porcentagens, em vez de pixels.

Depois de verificar que a conversão foi realizada corretamente, podemos prosseguir com o treinamento.

Os códigos completos e informações detalhadas sobre a transformação estão disponíveis em outro repositório. Você pode encontrar mais informações [neste link](https://1drv.ms/f/s!ArPFsy1SEFgWhIhjBBqUEIBE25SlMw?e=5LFAFo).

## Classificação de Quedas

Ao lidar com o conjunto de dados de quedas, encontramos desafios em relação à quantidade e qualidade dos dados. Embora tenhamos encontrado conjuntos de dados que continham quedas, muitos deles não possuíam marcações específicas para recortar as pessoas nas imagens. No entanto, encontramos dois conjuntos de dados relevantes que continham essas marcações: um consistindo em vídeos e outro em imagens variadas. Agora, explicaremos o processo de trabalho com esses dados da mesma forma que fizemos com o conjunto de dados de detecção de pessoas.
###   [UTTEJ KUMAR KANDAGATLA](https://www.kaggle.com/datasets/uttejkumarkandagatla/fall-detection-dataset)
este é um dataset diponivilizado no Kaggle, o qual é composto por um banco de 485 imagens com seus reppectivos mapeametos e classes.
