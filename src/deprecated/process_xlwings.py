import pandas as pd
import xlwings as xw
from tqdm import tqdm

from src.rule import Rule


def process(rule_file_name: str, original_file_name: str, output_file_name: str):

    # pre_process
    rule_df = pd.read_excel(rule_file_name, header=0)

    rules = [
        Rule(_row['구분1'], _row['구분2'], _row['구분3'], _row['적요'], _row['작성자'])
        for _, _row in rule_df.iterrows()
    ]

    # validation
    for rule in rules:
        if not rule.validate():
            return

    # process
    app = xw.App(visible=False)
    wb = app.books.open(original_file_name)
    sheet = wb.sheets.active

    header = {cell: idx for idx, cell in enumerate(sheet.range('1:1').value)}

    for row in tqdm(range(2, sheet.range('A1').current_region.last_cell.row)):
        row_data = sheet.range(f'{row}:{row}').value
        for rule in rules:
            if rule.desc_rule(row_data[header['적요']]) and rule.writer_rule(row_data[header['작성자']]):
                sheet.range((row, header['구분1'] + 1)).value = rule.div1
                sheet.range((row, header['구분2'] + 1)).value = rule.div2
                sheet.range((row, header['구분3'] + 1)).value = rule.div3
                break

    wb.save()
    app.quit()
