import pandas as pd


class ConvertExcelToTxt:
    def __init__(self, file_path):
        self.status = True
        self.error_message = "No errors"
        self.df = pd.DataFrame()

        body_size = ""
        text_file = ""

        try:
            self.df = pd.read_excel(file_path)
        except pd.errors.__all__:
            self.status = False
            self.error_message = "Error while reading file"

        if self.status:
            try:
                t_df = self.df.copy()
                t_df.to_csv(f"temp/{file_path.split('/')[-1].split('.')[0]}.txt", sep=" ", header=False, index=False)
            except pd.errors.__all__:
                self.status = False
                self.error_message = "Error while saving txt file"

        if self.status:
            try:
                body_size = f"{len(self.df.iloc[0])} {len(self.df.iloc[1])}"
            except pd.errors.__all__:
                self.status = False
                self.error_message = "Error. There less then 3 rows"

        if self.status:
            try:
                text_file = body_size + "\n"
                temp_file = open(f"temp/{file_path.split('/')[-1].split('.')[0]}.txt", "r")
                text_file += temp_file.read()
                temp_file.close()
            except IOError:
                self.status = False
                self.error_message = "Error while reading txt file"

        if self.status:
            try:
                temp_file = open(f"temp/{file_path.split('/')[-1].split('.')[0]}.txt", "w")
                temp_file.write(text_file)
                temp_file.close()
            except IOError:
                self.status = False
                self.error_message = "Error while writing txt file"

        if not self.status:
            print(self.error_message)


if __name__ == "__main__":
    test = ConvertExcelToTxt("test_data/x.xlsx")
    print(test.error_message)
