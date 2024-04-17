import os
import json
import time
import shutil
import xmltodict


def convert_json_to_xml(input_file, output_folder):
    # Sprawdź, czy plik wejściowy jest już w całości zapisany
    while True:
        try:
            with open(input_file, 'r') as f:
                json_data = json.load(f)
            break
        except json.decoder.JSONDecodeError as e:
            print(f"Plik {input_file} nie jest poprawnym plikiem .json")
            return

    try:
        # Konwersja danych JSON na XML
        xml_data = xmltodict.unparse(json_data, pretty=True)
        # Zapis do pliku XML
        xml_filename = os.path.splitext(os.path.basename(input_file))[0]+".xml"
        xml_filepath = os.path.join(output_folder, xml_filename)
        with open(xml_filepath, 'w') as xml_file:
            xml_file.write(xml_data)

        return xml_filepath

    except json.JSONDecodeError as e:
        print(f"Błąd podczas konwersji pliku {input_file}: {e}")
        filename = input_file
        input_filepath = os.path.join(input_folder, filename)
        shutil.move(input_filepath, error_folder)


def process_files(input_folder, output_folder):
    while True:
        for filename in os.listdir(input_folder):
            if filename.endswith(".json"):
                input_filepath = os.path.join(input_folder, filename)
                try:
                    xml_filepath = convert_json_to_xml(input_filepath, output_folder)
                    if xml_filepath is not None:
                     print(f"Konwersja zakończona: {input_filepath} -> {xml_filepath}")
                     # Usuń plik
                     os.remove(input_filepath)

                except Exception as e:
                    print(f"Błąd podczas konwersji pliku {input_filepath}: {e}")
                    # Przenieś błędny plik do innego folderu, aby uniknąć blokowania przepływu
                    shutil.move(input_filepath, error_folder)

        dir = os.listdir(input_folder)
        if len(dir) ==0:
            ans = input("Folder wejściowy jest pusty. Zakończyć działanie programu? [Y/n]")
            if ans =="y" or ans =="Y":
                return
        time.sleep(1)


if __name__ == "__main__":
    input_folder = "C:/Users/HP/PycharmProjects/branzowe/input"
    output_folder = "C:/Users/HP/PycharmProjects/branzowe/output"
    error_folder = "C:/Users/HP/PycharmProjects/branzowe/output/errors"
    process_files(input_folder, output_folder)

