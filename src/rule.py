import pandas


class Rule:
    def __init__(self, div1, div2, div3, desc, writer):
        self.div1 = div1
        self.div2 = div2
        self.div3 = div3
        self.desc = desc
        self.writer = writer

    def validate(self) -> bool:
        if pandas.isna(self.div1) and pandas.isna(self.div2) and pandas.isna(self.div3):
            print("> [WARN] 구분1, 구분2, 구분3 중 하나는 값이 있어야 합니다.")
            return False

        if pandas.isna(self.desc) and pandas.isna(self.writer):
            print("> [WARN] 적요, 작성자 중 하나는 값이 있어야 합니다.")
            return False

        return True

    def desc_rule(self, desc: str):
        if pandas.isna(desc):
            return False

        if pandas.isna(self.desc):
            return True

        if self.desc.startswith('$'):
            return desc.startswith(self.desc.lstrip('$'))

        if self.desc.startswith('^'):
            return desc.endswith(self.desc.rstrip('^'))

        return False not in [
            True in [x in desc for x in and_desc_rule.split('|')]
            for and_desc_rule in self.desc.split(',')
        ]

    def writer_rule(self, writer: str):
        if pandas.isna(writer):
            return False

        if pandas.isna(self.writer):
            return True

        return writer in self.writer.split('|')

    def __repr__(self):
        return f'div1={self.div1}, div2={self.div2}, div3={self.div3},' \
               f'desc_rule={self.desc}, writer_rule={self.writer}'
