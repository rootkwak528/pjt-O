import pandas as pd

from src.rule import Rule


def main():

    rule_df = pd.read_excel("files/rules.xlsx", header=0)
    input_df = pd.read_excel("files/input.xlsx", header=0)

    rules = [
        Rule(_row['구분1'], _row['구분2'], _row['구분3'], _row['적요'], _row['작성자'])
        for _, _row in rule_df.iterrows()
    ]

    for rule in rules:
        indexes = input_df['적요'].apply(rule.desc_rule) & input_df['작성자'].apply(rule.writer_rule)

        input_df.loc[indexes, '구분1'] = rule.div1
        input_df.loc[indexes, '구분2'] = rule.div2
        input_df.loc[indexes, '구분3'] = rule.div3

    input_df.to_excel('files/output.xlsx', index=False)


if __name__ == "__main__":
    main()
