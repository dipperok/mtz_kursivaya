import numpy as np
import pandas as pd


class ConvertExcelToTxt:
    def __init__(self, file_path):
        self.status = True
        self.err_msg = "No errors"
        self.output_file_path = ""
        self.df = pd.DataFrame()

        try:
            self.df = pd.read_excel(file_path)
        except:
            self.status = False
            self.err_msg = "Error while reading file, try: install openpyxl | check folder restrictions | run as admin"

        if self.status:
            try:
                r = [len(self.df.iloc[0]), len(self.df.iloc[1])]
                r.extend([np.nan for i in range(len(self.df.columns)-2)])

                t_df = pd.DataFrame(r, index=list(self.df.columns)).transpose()
                t_df = pd.concat([t_df, self.df])

                new_file_name = file_path.split('/')[-1].split('.')[0]

                self.output_file_path = f"temp/{new_file_name}.txt"

                t_df.to_csv(self.output_file_path, sep=" ", header=False, index=False, float_format="%.0f")
            except:
                self.status = False
                self.err_msg = "Error while saving txt file"

        if not self.status:
            print(self.err_msg)


if __name__ == "__main__":
    test = ConvertExcelToTxt("test_data/x.xlsx")
    print(test.err_msg)
