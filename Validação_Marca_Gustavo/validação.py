marcas ={
    "fiat",
    "chevrolet",
    "toyota",
    "honda",
    "ferrari",
    "porsche",
    "mercedes",
    "audi",
    "bmw",
    "volkswagen",
    "mazda",
    "nissan",
    "lamborghini",
}

marca = input (("Digite uma marca de carro: "))
if marca in marcas:
    print ("Tem no estoque")
else:
    print("Não tem no estoque")
