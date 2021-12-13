class Calc:
    def __init__(self, ratios, crates):
        self.ratio = sorted(ratios)
        self.crates = crates
        self.summed_ratio = sum(ratios)

    def youngest_share(self):
        youngest = self.ratio[0] / self.summed_ratio * self.crates
        str_youngest = f"Youngest: {self.ratio[0]}/{self.summed_ratio} * {self.crates} = {youngest}"
        return str_youngest

    def middle_share(self):
        middle = self.ratio[1] / self.summed_ratio * self.crates
        str_middle = f"Middle: {self.ratio[1]}/{self.summed_ratio} * {self.crates} = {middle}"
        return str_middle

    def eldest_share(self):
        eldest = self.ratio[-1] / self.summed_ratio * self.crates
        str_eldest = f"Eldest: {self.ratio[-1]}/{self.summed_ratio} * {self.crates} = {eldest}"
        return str_eldest

    def allShares(self):
        youngest = self.ratio[0] / self.summed_ratio * self.crates
        str_youngest = f"{self.ratio[0]}/{self.summed_ratio} * {self.crates} = {youngest}"
        middle = self.ratio[1] / self.summed_ratio * self.crates
        str_middle = f"{self.ratio[1]}/{self.summed_ratio} * {self.crates} = {middle}"
        eldest = self.ratio[-1] / self.summed_ratio * self.crates
        str_eldest = f"{self.ratio[-1]}/{self.summed_ratio} * {self.crates} = {eldest}"
        return f"Eldest get: {str_eldest}\nMiddle get: {str_middle}\nYoungest get: {str_youngest}"


ratio = [1, 2, 3]
a_calc = Calc(ratio, 120)
print(a_calc.youngest_share())

b_calc = Calc(ratio, 180)
print(b_calc.middle_share())
