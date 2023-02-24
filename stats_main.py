'''
Ideia: quando eu passar o CSV ele vai ter só o nome da instância e o valor do custo junto com o tempo de execução necessário
Assim, a cada execução do meu código eu adiciono uma coluna no meu DataFrame, e salvo no .csv
Ao final, eu só chamo a função ini() e inicializo os DataFrames, podendo pedir a média, desvio padrão, variância e um
gráfico de dispersão dos meus dados para cada instância
'''

import pandas as pd
import sys
import os

class Stats:

    def __init__(self, instances_names):
        self.cost_df = pd.DataFrame()
        self.time_df = pd.DataFrame()

        self.cost_df['Name'] = instances_names
        self.time_df['Name'] = instances_names

    def load(self, path_to_csv, exp_numb):
        '''
        essa função é a função que irá realizar o load do DataFrame, passando o path_to_csv como argumento da pasta
        que contém os CSV gerados pelo programa principal (o que roda o algoritmo)
        '''

        col_cost_name="Cost_"+"exp_num_"+str(exp_numb)
        col_time_name="Time_" + "exp_num_" + str(exp_numb)

        self.cost_df[col_cost_name] = pd.read_csv(path_to_csv, usecols=['Cost'])
        self.time_df[col_time_name] = pd.read_csv(path_to_csv, usecols=['Time'])

    def ini(self, path_to_cost_csv, path_to_time_csv):
        self.cost_df = pd.read_csv(path_to_cost_csv)
        self.time_df = pd.read_csv(path_to_time_csv)

    def save_df(self):
        cwd = os.getcwd()

        # Define o caminho para salvar os csv's
        directory_path = cwd + "/db"

        # Checa se o caminho já existe
        if not os.path.exists(directory_path):
            # Se não existe eu crio
            os.mkdir(directory_path)

        time = directory_path + "/time.csv"
        cost = directory_path + "/cost.csv"

        self.cost_df.to_csv(cost, index=False)
        self.time_df.to_csv(time, index=False)

    def stats(self):
        # calculando a média
        mean_row = self.cost_df.mean(axis=1, numeric_only=True)
        mean_row = mean_row.tolist()

        # calculando o desvio padrão
        std_row = self.cost_df.std(axis=1, numeric_only=True)
        std_row = std_row.tolist()

        # calculando o desvio padrão
        var_row = self.cost_df.var(axis=1, numeric_only=True)
        var_row = var_row.tolist()

        # calculando máximo e mínimos
        min_row = self.cost_df.min(axis=1, numeric_only=True)
        min_row = min_row.tolist()
        max_row = self.cost_df.max(axis=1, numeric_only=True)
        max_row = max_row.tolist()

        self.cost_df["Min"] = min_row
        self.cost_df["Max"] = max_row
        self.cost_df["Mean"] = mean_row
        self.cost_df["Std"] = std_row
        self.cost_df["Var"] = var_row



# Cainho para o arquivo com o nome das instâncias
instance_names_fpath = sys.argv[1]

# Caminho para a pasta com os CSVs de cada execução
folder_path = sys.argv[2]

instance_names_file = open(instance_names_fpath)

instance_names = []

for line in instance_names_file:
    instance_names.append(line.strip())

obj = Stats(instance_names)

i = 1

# Listo todos os .csv contidos na pasta dada
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

df_list = []

# Pego a lista dos arquivos dentro da pasta
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    obj.load(file_path, i)
    i += 1

obj.stats()

obj.save_df()