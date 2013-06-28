# coding=utf-8
from src.Constants import BuildIds as BID
import codecs
try:
    #python3
    from configparser import SafeConfigParser
except:
    from ConfigParser import SafeConfigParser
import os

try:
    from config import config
    language = ""
    if "language" in config:
        language = config["language"]
    elif config["universe"][-2:] == "de":
        language = "de"
    elif config["universe"][-2:] == "se":
        language = "se"
except:
    language = "de"

# this Translations class is from kovans ogbot with slight modifications
class Translations(dict):
    def __init__(self):
        for fileName in os.listdir('languages'):
            fileName, extension = os.path.splitext(fileName)

            if not fileName or fileName.startswith('.') or extension != '.ini':
                continue
            parser = SafeConfigParser()
            parser.optionxform = str # prevent ini parser from converting names to lowercase
            try:
                parser.readfp(codecs.open(os.path.join("languages", fileName+extension), "r", "utf8"))
                translation = {}
                for section in parser.sections():
                    translation.update((key, value) for key, value in parser.items(section))
                self[translation['languageCode']] = translation
            except Exception as e:
                raise Exception("Malformed language file (%s%s): %s"%(fileName,extension,e))

# TODO remove below code
t = Translations()
translation = t[language]

buildLabels = {
        BID.METALMINE  : translation["metalMine"],
        BID.CRYSTALMINE  : translation["crystalMine"],
        BID.DEUTERIUMSYNTHESIZER  : translation["deuteriumSynthesizer"],
        BID.SOLARPLANT  : translation["solarPlant"],
        BID.FUSIONREACTOR : translation["fusionReactor"],
        BID.ROBOTICSFACTORY : translation["roboticsFactory"],
        BID.NANITEFACTORY : translation["naniteFactory"],
        BID.SHIPYARD : translation["shipyard"],
        BID.METALSTORAGE : translation["metalStorage"],
        BID.CRYSTALSTORAGE : translation["crystalStorage"],
        BID.DEUTERIUMTANK : translation["deuteriumTank"],
        BID.METALHIDING : translation["metalHiding"],
        BID.CRYSTALHIDING : translation["crystalHiding"],
        BID.DEUTERIUMHIDING : translation["deuteriumHiding"],
        BID.RESEARCHLAB : translation["researchLab"],
        BID.TERRAFORMER : translation["terraformer"],
        BID.ALLIANCEDEPOT : translation["allianceDepot"],
        BID.MISSILESILO : translation["missileSilo"],
        # Research
        BID.ESPIONAGETECHNOLOGY: translation["espionageTechnology"],
        BID.COMPUTERTECHNOLOGY: translation["computerTechnology"],
        BID.WEAPONSTECHNOLOGY: translation["weaponsTechnology"],
        BID.SHIELDINGTECHNOLOGY: translation["shieldingTechnology"],
        BID.ARMOURTECHNOLOGY: translation["armourTechnology"],
        BID.ENERGYTECHNOLOGY: translation["energyTechnology"],
        BID.HYPERSPACETECHNOLOGY: translation["hyperspaceTechnology"],
        BID.COMBUSTIONDRIVE: translation["combustionDrive"],
        BID.IMPULSEDRIVE: translation["impulseDrive"],
        BID.HYPERSPACEDRIVE: translation["hyperspaceDrive"],
        BID.LASERTECHNOLOGY: translation["laserTechnology"],
        BID.IONTECHNOLOGY: translation["ionTechnology"],
        BID.PLASMATECHNOLOGY: translation["plasmaTechnology"],
        BID.INTERGALACTICRESEARCHNETWORK: translation["intergalacticResearchNetwork"],
        BID.ASTROPHYSICS: translation["astroPhysics"],
        BID.GRAVITONTECHNOLOGY: translation["gravitonTechnology"],
        # Shipyard
        BID.SMALLCARGO: translation["smallCargo"],
        BID.LARGECARGO: translation["largeCargo"],
        BID.LIGHTFIGHTER: translation["lightFighter"],
        BID.HEAVYFIGHTER: translation["heavyFighter"],
        BID.CRUISER: translation["cruiser"],
        BID.BATTLESHIP: translation["battleShip"],
        BID.COLONYSHIP: translation["colonyShip"],
        BID.RECYCLER: translation["recycler"],
        BID.ESPIONAGEPROBE: translation["espionageProbe"],
        BID.BOMBER: translation["bomber"],
        BID.SOLARSATELLITE: translation["solarSatellite"],
        BID.DESTROYER: translation["destroyer"],
        BID.DEATHSTAR: translation["deathStar"],
        BID.BATTLECRUISER: translation["battleCruiser"],
        BID.ROCKETLAUNCHER: translation["rocketLauncher"],
        BID.LIGHTLASER: translation["lightLaser"],
        BID.HEAVYLASER: translation["heavyLaser"],
        BID.GAUSSCANNON: translation["gaussCannon"],
        BID.IONCANNON: translation["ionCannon"],
        BID.PLASMATURRET: translation["plasmaTurret"],
        BID.SMALLSHIELDDOME: translation["smallShieldDome"],
        BID.LARGESHIELDDOME: translation["largeShieldDome"],
        BID.ANTIBALLISTICMISSILE: translation["antiBallisticMissile"],
        BID.INTERPLANETARYMISSILE: translation["interplanetaryMissile"],
    }
buildLabelsName = dict(zip(buildLabels.values(),buildLabels.keys()))
