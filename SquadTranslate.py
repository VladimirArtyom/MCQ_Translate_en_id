import pandas as pd 
import numpy as np
import googletrans as gt
import pickle

def save_to_pickle(item, fileName: str):
    with open(fileName, 'wb') as f:
        pickle.dump(item, f)

def translate(text: str):
    translated: str = gt.translate(text, 'id')
    row_id =  pd.DataFrame([{"context": translated}])

    return row_id

if __name__ == "__main__":
    translated_df: pd.DataFrame = pd.DataFrame(columns=["context"])
    savePath: str = "./translate/SQUAD/train/train_data"

    df: pd.DataFrame = pd.read_csv('./en/SQUAD_train.csv')

    list_of_context = df['context_para'].values.tolist()

    print("Translating Squad dataset ... ")
    for i in range(len(list_of_context)):
        translated_df = pd.concat([translated_df,
                                   translate(list_of_context[i])], ignore_index=True)
        if i % 500 == 0:
            print(f"Saving it to pickle ... at i = {i}")
            save_to_pickle(translated_df, f"{savePath}_{i}.pickle")
            print("Saving completed, continuing ...")

    save_to_pickle(translate, f"{savePath}_{i}.pickle")
    print("Translating Complete")

