import numpy as np
import pandas as pd


class ConvertExcelToTxt:
    def __init__(self, file_path):
        self.status = True
        self.error_message = "No errors"
        self.df = pd.DataFrame()

        try:
            self.df = pd.read_excel(file_path)
        except pd.errors.__all__:
            self.status = False
            self.error_message = "Error while reading file"

        if self.status:
            try:
                r = [len(self.df.iloc[0]), len(self.df.iloc[1])]
                r.extend([np.nan for i in range(len(self.df.columns)-2)])

                t_df = pd.DataFrame(r, index=list(self.df.columns)).transpose()
                t_df = pd.concat([t_df, self.df])

                new_file_name = file_path.split('/')[-1].split('.')[0]

                t_df.to_csv(f"temp/{new_file_name}.txt", sep=" ", header=False, index=False, float_format="%.0f")
            except pd.errors.__all__:
                self.status = False
                self.error_message = "Error while saving txt file"

        if not self.status:
            print(self.error_message)


if __name__ == "__main__":
    test = ConvertExcelToTxt("test_data/x.xlsx")
    print(test.error_message)
