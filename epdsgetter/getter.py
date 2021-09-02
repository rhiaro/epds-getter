import os
import csv
import dataset


API_URL = "https://environment.data.gov.uk/public-register/%s/registration"
TMP_LOCAL_CSV = "tmpdata/ea-sample_%s.csv"
EXEMPTION_REGISTERS = ["waste-exemptions", "water-discharge-exemptions", "flood-risk-exemptions"]
PERMIT_REGISTERS = ["radioactive-substance", "industrial-installations", "waste-operations", "water-discharges"]
OTHER_REGISTERS = ["enforcement-action", "waste-carriers-brokers", "scrap-metal-dealers", "end-of-life-vehicles"]

db = dataset.connect()

reg = "water-discharges"

def get_local_data():

    raw_table = db["raw_%s" % reg]

    with open(TMP_LOCAL_CSV % reg) as fh:
        header = [h.replace('.','_') for h in fh.readline().split(',')]
        reader = csv.DictReader(fh, fieldnames=header)

        for row in reader:
            raw_table.insert(row)

    return raw_table


def countdata():
    return len(db["raw_%s" % reg])