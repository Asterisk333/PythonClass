import json
import xml.etree.ElementTree as ET
from lxml import etree
import tkinter as tk
from tkinter import filedialog, messagebox


# XML Schema Validation
def validate_xml(xml_file, schema_file):
    try:
        xmlschema_doc = etree.parse(schema_file)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        xml_doc = etree.parse(xml_file)
        xmlschema.assertValid(xml_doc)
        return True, "XML ist gültig."
    except etree.XMLSyntaxError as e:
        return False, f"XML-Syntaxfehler: {str(e)}"
    except etree.DocumentInvalid as e:
        return False, f"XML ist ungültig gemäß Schema:\n{str(e)}"


# Klassenstruktur für die Produkte
class Product:
    def __init__(self, product_id, name, price, category, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def to_dict(self):
        return {
            "id": self.product_id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "stock": self.stock
        }


class ProductList:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def to_dict(self):
        return [product.to_dict() for product in self.products]


# XML Parsing
def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    product_list = ProductList()

    for product_elem in root.findall('product'):
        product_id = product_elem.get('id')
        name = product_elem.find('name').text
        price = float(product_elem.find('price').text)
        category = product_elem.find('category').text
        stock = int(product_elem.find('stock').text)

        product = Product(product_id, name, price, category, stock)
        product_list.add_product(product)

    return product_list


# JSON Export
def export_to_json(data, json_file):
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)


# Funktion zum Auswählen der XML-Datei
def select_xml_file():
    xml_file = filedialog.askopenfilename(title="Wähle eine XML-Datei", filetypes=[("XML files", "*.xml")])
    xml_file_var.set(xml_file)


# Funktion zum Auswählen der Schema-Datei
def select_schema_file():
    schema_file = filedialog.askopenfilename(title="Wähle eine XSD-Datei", filetypes=[("XSD files", "*.xsd")])
    schema_file_var.set(schema_file)


# Funktion zum Validieren des XML und Exportieren nach JSON
def validate_and_export():
    xml_file = xml_file_var.get()
    schema_file = schema_file_var.get()
    json_file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])

    if not xml_file or not schema_file:
        messagebox.showwarning("Fehlende Eingabe", "Bitte wählen Sie sowohl eine XML- als auch eine Schema-Datei.")
        return

    # Validierung des XML
    valid, message = validate_xml(xml_file, schema_file)

    if valid:
        messagebox.showinfo("Erfolg", message)

        # Parsing des XML
        product_list = parse_xml(xml_file)

        # Export nach JSON
        export_to_json(product_list.to_dict(), json_file)
        messagebox.showinfo("Erfolg", f"Die Daten wurden erfolgreich in {json_file} exportiert.")
    else:
        messagebox.showerror("Fehler", message)


# Haupt-GUI
root = tk.Tk()
root.title("XML-Validator und JSON-Exporter")

# GUI Layout
xml_file_var = tk.StringVar()
schema_file_var = tk.StringVar()

tk.Label(root, text="XML-Datei:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
tk.Entry(root, textvariable=xml_file_var, width=50).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Durchsuchen", command=select_xml_file).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="XSD-Datei:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
tk.Entry(root, textvariable=schema_file_var, width=50).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Durchsuchen", command=select_schema_file).grid(row=1, column=2, padx=10, pady=5)

tk.Button(root, text="Validieren und Exportieren", command=validate_and_export).grid(row=2, column=1, pady=20)

# GUI starten
root.mainloop()
