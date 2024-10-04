import pandas as pd

def leer_excel(archivo_excel):
    try:
        # Leer todas las hojas del archivo Excel
        xls = pd.ExcelFile(archivo_excel)
        hojas = xls.sheet_names  # Obtener los nombres de las hojas

        for hoja in hojas:
            # Leer cada hoja y mostrarla
            df = pd.read_excel(xls, sheet_name=hoja)
            print(f"\nContenido de la hoja: {hoja}")
            print(df)

    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def main():
    # Nombre del archivo Excel
    archivo_excel = input("Introduce el nombre del archivo Excel (con extensión): ")

    # Llamada a la función para leer el archivo
    leer_excel(archivo_excel)

if __name__ == "__main__":
    main()
