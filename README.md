# Modifica camada CAR

## Sumário
1. [Descrição](#Descrição)
2. [Uso](#Uso)
   - [Sobre os arquivos](#Sobre-os-arquivos)
4. [Instalação](#Instalação)

## Descrição

Script para remover os CARs cancelados e classificar os imóveis na [camada do CAR: AREA_IMOVEL_1.shp](https://www.car.gov.br/#/). Reescreve na própria camada, sendo o input o mesmo do output.
A classificação é definida pela [Lei 8.629, de 25 de fevereiro de 1993](https://www.planalto.gov.br/ccivil_03/leis/l8629.htm), alterada pela [Lei nº 13.465  de 2017](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/L13465.htm), e considera o módulo fiscal, que varia de acordo com cada município.

Em relação ao tamanho da área, os imóveis rurais são classificados em: 
 
1. **Minifúndio**: imóvel rural com área inferior a Fração Mínima de Parcelamento;
2. **Pequena Propriedade**: imóvel com área entre a Fração Mínima de Parcelamento e 4 módulos fiscais;
3. **Média Propriedade**: imóvel rural de área superior a 4 e até 15 módulos fiscais;
4. **Grande Propriedade**: imóvel rural de área superior a 15 módulos fiscais.

## Uso
Para utilizar o script é necessário colocar o arquivo `AREA_IMOVEL_1.shp` na mesma pasta do arquivo python.
Execute o código `camada_car.py` para remover os CARs cancelados e classificar os imóveis em: Minifúndio, Pequena Propriedade, Média Propriedade e Grande Propriedade.

### Sobre os arquivos

* [**camada_car.py**](camada_car.py): Tem como input e output o `AREA_IMOVEL_1.shp`, que deverá ser baixado no [site do CAR](https://www.car.gov.br/#/).

## Instalação

Para utilizar os scripts é necessária a instalação das bibliotecas Python:

* **pandas**: Esta é a biblioteca fundamental para manipulação e análise de dados.
* **geopandas**: Biblioteca responsável pela leitura do geodataframe (gdf) e manipulações de dados.
* **shapely.geometry**: Essa biblioteca é responsável por manter os polígonos e a geometria dos dados.

