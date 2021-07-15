import pandas as pd

path = ("dataset/titanic/source.csv")

try: 
    df = pd.read_csv(path)
except:
    print("pandas did not find the dataset source")
finally:
    del path

print(df.shape)

"""
    • pclass: classe do passageiro (1 = primeira, 2 = segunda, 3 = terceira)
    • survived: sobreviveu (0 = não, 1 = sim)
    • name: nome
    • sex: sexo
    • age: idade
    • sibsp: número de irmãos/esposa(o) a bordo
    • parch: número de pais/filhos a bordo
    • ticket: número da passagem
    • fare: preço da passagem
    • cabin: cabine
    • embarked: (local em que o passageiro embarcou C = Cherbourg, Q =
    Queenstown, S = Southampton)
    • boat: bote salva-vidas
    • body: número de identificação do corpo
    • home.dest: lar/destino
"""