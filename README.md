# NASA Mars Curiosity Rover — Photos

Photos du rover Mars Curiosity récupérées via l’API NASA Mars Photos.

## Description

Ce dépôt contient un script Python qui interroge l’[API NASA Mars Photos](https://api.nasa.gov/) pour télécharger les images prises par le rover **Curiosity** sur Mars. Vous pouvez choisir le sol (jour martien) et la caméra pour récupérer les photos correspondantes.

## Prérequis

- **Python 3**
- **Clé API NASA** (gratuite) : [https://api.nasa.gov/](https://api.nasa.gov/)

## Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/Fabrice-Heuvrard/NASA_MARS_CURIOSITY.git
cd NASA_MARS_CURIOSITY
```

2. Installer les dépendances :

```bash
pip install requests
```

3. Obtenir une clé API NASA sur [api.nasa.gov](https://api.nasa.gov/) et la renseigner dans le script (remplacer `#YOUR API KEY` par votre clé).

## Utilisation

1. Ouvrir `Mars_Curiosity_Rover.py`.
2. Renseigner votre clé API : `api_key = "VOTRE_CLE_API"`.
3. Ajuster si besoin :
   - **`Camera`** : caméra utilisée (voir liste ci-dessous).
   - **`sol`** : jour martien (ex. `3662` ≈ 24/11/2022).
4. Exécuter le script :

```bash
python Mars_Curiosity_Rover.py
```

Les images sont téléchargées dans le répertoire courant avec des noms du type :  
`Sol 3662 - ID 12345 - Curiosity NAVCAM 2022-11-24.jpg`.

## Caméras disponibles

| Caméra   | Description |
|----------|-------------|
| `NAVCAM` | Navigation Camera |
| `CHEMCAM`| Chemistry and Camera |
| `FHAZ`   | Front Hazard Avoidance Camera |
| `RHAZ`   | Rear Hazard Avoidance Camera |
| `MARDI`  | Mars Descent Imager |

## Fichiers du projet

- **`Mars_Curiosity_Rover.py`** — Script principal pour récupérer et télécharger les photos Curiosity.

## API NASA

- Documentation : [https://api.nasa.gov/](https://api.nasa.gov/)
- Endpoint utilisé : `https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos`

## Contribution

Les contributions sont les bienvenues. N’hésitez pas à ouvrir une [issue](https://github.com/Fabrice-Heuvrard/NASA_MARS_CURIOSITY/issues) ou une [pull request](https://github.com/Fabrice-Heuvrard/NASA_MARS_CURIOSITY/pulls).

## Licence

Voir le dépôt pour les informations de licence. Les images proviennent de la NASA et sont soumises à leur politique d’utilisation.
