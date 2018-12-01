class PharmaceuticalData:

    # LOCATION      --> Country code
    # Time          --> Date in the form of %Y
    # PC_HEALTHXP   --> % of Health spending
    # PC_GDP        --> % of GDP
    # USD_CAP       --> in USD per capita (using economy-wide PPPs)
    # FLAG_CODES    --> ????
    # TOTAL_SPEND   --> Total spending in millions

    def __init__(self, location, year, percHealthExp, percPIB, usdPerCapita, flag, totalSpend  ):
        self.location = location
        self.year =  year
        self.percHealthExp = percHealthExp
        self.percPIB = percPIB
        self.usdPerCapita = usdPerCapita
        self.flag = flag
        self.totalSpend = totalSpend

    def __str__(self):
        return self.location + " - " + self.year + " - " + self.percHealthExp + " - " + self.percPIB + " - " + self.usdPerCapita + " - " + self.flag + " - " + self.totalSpend

    def buildFromCsv( iterator ):
        return PharmaceuticalData(iterator['LOCATION'], iterator['TIME'], iterator['PC_HEALTHXP'], iterator['PC_GDP'], iterator['USD_CAP'], iterator['FLAG_CODES'], iterator['TOTAL_SPEND'])