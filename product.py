#Read and write product, tool and program data from csv file

import pandas as pd


class Product:
    def __init__(self):
        self.df_tool = pd.DataFrame
        self.df_product = pd.DataFrame
        self.df_prog = pd.DataFrame

        self.artNo = 00000000
        self.name = ""
        self.steps = 0

        self.read_csv()

    # Read actual product and tool data
    def read_csv(self):
        file = open("/home/hansgrohe/Desktop/Lists/Produktliste.csv", 'r')
        self.df_product = pd.read_csv(file, delimiter=";", index_col=0)
        file.close()
        file = open("/home/hansgrohe/Desktop/Lists/Toolliste.csv", 'r')
        self.df_tool = pd.read_csv(file, delimiter=";", index_col=0)
        file.close()
        file = open("/home/hansgrohe/Desktop/Lists/Programmliste.csv", 'r')
        self.df_prog = pd.read_csv(file, delimiter=";", index_col=0)
        file.close()

    # Set article number according to user input
    def set_art_no(self, value):
        self.artNo = value

    def get_name(self):
        return self.name

    def get_steps(self):
        return self.steps

    # get product data when selected product changed
    def select_product(self, art_no):
        self.set_art_no(art_no)
        # if selected article number is in product data read values
        if self.artNo in self.df_product.index:
            self.name = self.df_product.at[self.artNo, "Bezeichnung"]
            self.steps = self.df_product.at[self.artNo, "Anzahl Schritte"]
            return True
        else:
            return False

    def get_cyc(self, step):
        cycno = self.df_product.at[self.artNo, "S" + str(step) + "_Prog"]
        
        return self.df_prog.at[cycno, "CVIR Nr"]

    def get_toolno(self, step):
        return self.df_product.at[self.artNo, "S" + str(step) + "_Tool"]

    def get_toolname(self, step):
        toolno = self.df_product.at[self.artNo, "S" + str(step) + "_Tool"]

        return self.df_tool.at[toolno, "Tool"]
    
    def get_torque(self, step):
        progno = self.df_product.at[self.artNo, "S" + str(step) + "_Prog"]

        return self.df_prog.at[progno, "Drehmoment"]
    
    def get_progdescription(self, step):
        progno = self.df_product.at[self.artNo, "S" + str(step) + "_Prog"]

        return self.df_prog.at[progno, "Beschreibung"]
