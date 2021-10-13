import boto3
import pandas as pd

# Criar um cliente para integir com o AWS S3
s3_cliente = boto3.client('s3')

s3_cliente.download_file("datalake-rom-igti-edc",
                        "MICRODADOS_ENEM_2019.csv",
                        "data/MICRODADOS_ENEM_2019.csv"
                        )

#df = pd.read_csv("Data/MICRODADOS_ENEM_2019.csv", sep=";")
#print(df)

# s3_cliente.upload_file("data/pnadc20203.csv",
#                         "datalake-rom-igti-edc",
#                         "data/pnadc20203.csv"
#                         )

#s3_cliente.upload_file("data/MICRODADOS_ENEM_2019.csv","datalake-rom-igti-edc","data/MICRODADOS_ENEM_2019.csv")
