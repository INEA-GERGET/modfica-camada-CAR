import geopandas as gpd
import os
import pandas as pd
from shapely.geometry import MultiPolygon, Polygon

# --- CONFIGURAÇÕES ---
caminho_original = os.path.join('camada', 'AREA_IMOVEL_1.shp')

# --- FUNÇÃO DE CLASSIFICAÇÃO ---
def classificar_imovel(row):
    try:
        area_ha = float(row['num_area'])
        # n_modulos baseado na coluna mod_fiscal que já existe no seu SHP
        n_modulos = float(row['mod_fiscal'])
    except:
        return "Erro nos dados"

    fmp_val = 2.0  # Fração Mínima de Parcelamento fixa em 2 ha

    if area_ha < fmp_val:
        return 'Minifúndio'
    elif n_modulos <= 4:
        return 'Pequena propriedade'
    elif 4 < n_modulos <= 15:
        return 'Média propriedade'
    else:
        return 'Grande propriedade'

# --- PROCESSAMENTO ---
if os.path.exists(caminho_original):
    print(f"Lendo e processando: {caminho_original}...")
    
    # Lemos o arquivo para a memória
    gdf = gpd.read_file(caminho_original)

    # --- Processamento ---

    tamanho_antes = len(gdf)
    gdf = gdf[gdf['ind_status'] != 'CA'] 
    tamanho_depois = len(gdf)
    print(f"Foram excluídos {tamanho_antes - tamanho_depois} registros com o CAR cancelado")

    # Aplicar a classificação na nova coluna 'classe' e 'fmp'
    gdf['classe'] = gdf.apply(classificar_imovel, axis=1)
    gdf['fmp'] = 2

    # Padronização de Geometria
    gdf['geometry'] = [
        MultiPolygon([feature]) if isinstance(feature, Polygon) else feature 
        for feature in gdf['geometry']
    ]

    # --- SOBRESCREVENDO O ARQUIVO ---
    print("Classificando os imóveis e sobrescrevendo o arquivo original...")
    try:
        # O GeoPandas irá deletar os componentes antigos (.shp, .dbf, .shx) 
        # e criar os novos com a coluna 'classe' incluída.
        gdf.to_file(caminho_original, driver="ESRI Shapefile")
        
        print("_______________________________________________________________")
        print("SUCESSO: Arquivo original atualizado!")

    except Exception as e:
        print(f"\nErro crítico ao tentar sobrescrever: {e}")
else:
    print(f"Erro: O arquivo {caminho_original} não foi encontrado para sobrescrever.")


