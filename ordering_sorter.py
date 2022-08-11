
from turtle import title
import pandas as pd
from openpyxl.workbook import Workbook
import PySimpleGUI as sg
pd.options.display.max_colwidth = None
INVENTORY = {
    "zapallo": 1,
    "calabaza": 1,
    "anco": 1,
    "kabutia": 1,
    "hokkaido": 1,
    "papa": 1,
    "zanahoria": 1,
    "batata": 1,
    "repollo": 1,
    "acelga": 1,
    "remolacha": 1,
    "pera": 2,
    "manzana": 2,
    "limon": 2,
    "naranja": 2,
    "pomelo": 2,
    "manzana verde": 2,
    "apio": 3,
    "banana": 3,
    "maracuya": 3,
    "mandarina": 3,
    "tomate": 3,
    "berenjena": 3,
    "espinaca": 3,
    "kiwi": 4,
    "morron": 4,
    "jengibre": 4,
    "curcuma": 4,
    "ajo": 4,
    "verdeo": 4,
    "verdeo colorado": 4,
    "puerro": 4,
    "kale": 4,
    "lechuga": 4,
    "rabanito": 4,
    "rucula": 4,
    "escarola": 4,
    "perejil": 4,
    "arandano": 4,
    "cilantro": 4,


}


def readFile(file):
    df = pd.read_excel(file)
    return df


def sort_order(order):
    filtered_order = {}
    missing_items = {}
    """ Add every item matched item of the inventory to sorted_list """
    for key, value in INVENTORY.items():
        for element in order.split("-"):
            if key in element:
                filtered_order[element] = value
    """ Items skipped such as explanations from Nico will be added now """

    for element in order.split("-"):
        for key, value in filtered_order.items():
            if element not in key:
                missing_items[element] = 5

    for key, value in missing_items.items():
        filtered_order[key] = value
    """ Now we sort from minor to major """
    filtered_order = sorted(filtered_order.items(), key=lambda x: x[1])
    filtered_order = [x[0] for x in filtered_order]

    return " - ".join(filtered_order)


def run():
    layout = [[sg.Text("Ordenador de pedidos de ALIMENTA SA")], [
        sg.Button("CLOSE")]]
    window = sg.Window(title="En ejecucion", layout=layout, margins=(200, 200))
    while True:
        event, values = window.read()
    # End program if user closes window or
    # presses the OK button
        if event == "CLOSE" or event == sg.WIN_CLOSED:
            break


    # file_xlsx = input(""" Give me the file:
    # """)
    # order_df = readFile(file_xlsx)
    # sorted_df = order_df
    # count = 0
    # for order in order_df.iloc[:, 4]:
    #     if type(order) != str:
    #         break
    #     sorted_df.iloc[count, 4] = sort_order(order)
    #     count += 1
    # output_filename = input("Guardar el archivo con el nombre → ")
    # sorted_df.to_excel(output_filename, index=False)
if __name__ == '__main__':
    run()
