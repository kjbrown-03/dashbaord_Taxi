from __future__ import annotations

import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))

from generate_excel import generate_excel  # noqa: E402


if __name__ == "__main__":
    generate_excel(HERE / "assets" / "modele_kpi_taxi_par_frequence.xlsx", vehicle="taxi", is_mock=False)
    generate_excel(HERE / "assets" / "donnees_test_taxi_par_frequence.xlsx", vehicle="taxi", is_mock=True)

    # Compatibilite avec l'ancien lien/nom de fichier.
    generate_excel(HERE / "assets" / "modele_kpi_multifeuilles_mis_a_jour.xlsx", vehicle="taxi", is_mock=False)
    generate_excel(HERE / "assets" / "donnees_test_import.xlsx", vehicle="taxi", is_mock=True)

    print("Modeles Excel Taxi generes par frequence.")
