import tabula

# Read pdf into list of DataFrame
df = tabula.read_pdf("iitbsam.pdf", pages='all')

# convert PDF into CSV file
tabula.convert_into("iitbsam.pdf", "output.csv", output_format="csv", pages='all')