#!/usr/bin/python
import csv
import sys

def readCategories(catfile):

def ask_and_update_categories(naam_tegenpartij, categories):

def getCategory(categories, naam_tegenpartij):
    if naam_tegenpartij in categories.keys():
        category = categories[naam_tegenpartij]
    else:
        category, categories = aks_and_update_categories(naam_tegenpartij, categories)
    return [category, categories]

def main():
    if len(sys.argv) != 2:
        print "usage: ./convert.py infile categoriesfile"
        sys.exit(-1)

    infile, catfile = sys.argv[1:2]
    categories = readCategories(catfile)
    reader = csv.reader(file(infile), delimiter=";")
    header = reader.next()
    for row in reader:
        valutadatum, ref_vd_verrichting, beschrijving, bedrag_vd_verrichting, munt, datum_v_verrichting, rekening_tegenpartij, naam_tegenpartij, mededeling1, mededeling2 = row
        category, categories = getCategory(naam_tegenpartij, categories)

main()
