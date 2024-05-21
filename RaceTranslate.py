import pandas as pd 
import numpy as np
import googletrans as gt
import pickle 
from typing import List

def translate(list_of_str: List[str], column_name: str, savePath: str):
    translated_df = pd.DataFrame(columns=["context"])

    for i in range(len(list_of_str)):
        translate: str = gt.translate(list_of_str[i], "id")
        row = pd.DataFrame({column_name: translate})
        if i % 500 == 0:
            save_to_pickle(translated_df, f"{savePath}_{i}.pickle")
            print("Saving complted, continuing...")
    print("Translation completed, all data will be saved")
    save_to_pickle(translated_df, f"{savePath}_all.pickle")

    return translated_df


def join_column_to_str(list_context: List[str],
                       list_question: List[str],
                       list_correct: List[str],
                       list_ic1: List[str],
                       list_ic2: List[str],
                       list_ic3: List[str],
                       delimiter: str = "|;|") -> List[str]:
    list_of_str: List[str] = []
    for i in range(len(list_context)):
        cntx: str = list_context[i]
        q: str = list_question[i]
        c: str = list_correct[i]
        ic_1: str = list_ic1[i]
        ic_2: str = list_ic2[i]
        ic_3: str = list_ic3[i]
        list_of_str.append(cntx + delimiter + q + delimiter + c + delimiter + ic_1 + delimiter + ic_2 + delimiter + ic_3 )

        break
    return list_of_str


def save_to_pickle(item, fileName: str):
    with open(fileName, "wb") as f:
        pickle.dump(item, f)


if __name__ == "__main__":
    savePath: str = "./translate/RACE/test_data"
    filePath: str = "./en/RACE_test.csv"
    df = pd.read_csv(filePath)

    list_of_context = df["context"]
    list_of_question = df["question"]
    list_of_correct = df["correct"]
    list_of_incorrect1 = df["incorrect1"]
    list_of_incorrect2 = df["incorrect2"]
    list_of_incorrect3 = df["incorrect3"]
    
    list_of_str = join_column_to_str(list_of_context,
                                     list_of_question,
                                     list_of_correct,
                                     list_of_incorrect1,
                                     list_of_incorrect2,
                                     list_of_incorrect3)
    td = translate(list_of_str, "translation", savePath)
    print(td.values)
    

