import boto3
import pandas as pd
from tqdm import tqdm

## Criar um cliente para integir com o AWS S3
s3_cliente = boto3.client('s3')

## Upload do arquivo
#s3_cliente.download_file("datalake-romulo-432558339686",
#                        "raw-data/MICRODADOS_ENEM_2019.csv",
#                        "data/MICRODADOS_ENEM_2019.csv"
#                        )

##Apresentação do dataframe
df = pd.read_csv("data/MICRODADOS_ENEM_2019.csv", sep=";", encoding="ANSI")
#, error_bad_lines="false")
print(df)

# Upload do arquivo
# tqdm(s3_cliente.upload_file("data/MICRODADOS_ENEM_2019.csv",
#                         "datalake-romulo-432558339686",
#                         "raw-data/MICRODADOS_ENEM_2019.csv"
#                         ))