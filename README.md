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

Ao lidar com o conjunto de dados de quedas, enfrentamos desafios relacionados à quantidade e qualidade dos dados disponíveis. Embora tenhamos encontrado vários conjuntos de dados que continham informações sobre quedas, muitos deles não continham marcações específicas que indicassem como recortar as pessoas nas imagens. No entanto, encontramos dois conjuntos de dados relevantes que incluíam essas marcações, um composto por vídeos e outro por imagens variadas. Agora, vamos explicar o processo de trabalho com esses dados da mesma forma que fizemos com o conjunto de dados de detecção de pessoas.

### Conjuntos de Dados Mapeados

#### [UTTEJ KUMAR KANDAGATLA](https://www.kaggle.com/datasets/uttejkumarkandagatla/fall-detection-dataset)

Este é um conjunto de dados disponibilizado no Kaggle, composto por 485 imagens, cada uma com suas respectivas marcações e classes de queda.

**Para fazer o download:**
- Clique no [link de download](https://www.kaggle.com/datasets/uttejkumarkandagatla/fall-detection-dataset/download?datasetVersionNumber=1).
- O download resultará em um arquivo .rar contendo os arquivos do conjunto de dados.

#### [ImViA](https://imvia.u-bourgogne.fr/en/database/fall-detection-dataset-2.html)

Este conjunto de dados é composto por 5 grupos de vídeos, sendo que cada grupo foi gravado em quartos diferentes. Três dos quartos possuem marcações de mapeamento e classes, enquanto os outros dois não possuem.

**Para fazer o download:**
- Clique no [link de download](http://imvia.u-bourgogne.fr/database/FallDataset.zip).
- O download resultará em um arquivo .rar que contém 5 subpastas correspondentes a cada um dos quartos referenciados.

### Conjuntos de Dados Não Mapeados

#### [Adhikari, Kripesh, Hamid Bouchachia, and Hammadi Nait-Charif](https://falldataset.com)

Este conjunto de dados é mencionado como não mapeado, o que indica que pode não conter marcações específicas para a localização das pessoas nas imagens. Para fazer o download deste conjunto de dados, siga as etapas abaixo:

1. Acesse o [link de download](https://falldataset.com/data/).

2. Você verá várias pastas, cada uma contendo um conjunto de dados de vídeo fragmentado em imagens .png.

3. Você pode baixar cada conjunto de dados individualmente clicando nas pastas correspondentes. No entanto, este processo pode ser um pouco demorado, pois envolve baixar várias pastas separadamente.

