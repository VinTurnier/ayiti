import pickle
import cPickle

class Commune(object):
    pass

class SectionCommunal(object):
    pass


Locations = [
    {
        "name": "Artibonite",
        "capital": "Gonaive",
        "area": 4986.94,
        "coordinates":{
            "latitude": 19.45,
            "longitude": -72.68
        },
        "arrondissements": [
            {
                "name": "Dessalines",
                "communes":[
                    {
                        "name": "Desdunes"
                    },
                    {
                        "name": "Dessalines"
                    },
                    {
                        "name": "Grande Saline"
                    },
                    {
                        "name": "Petite Rivière de l'Artibonite"
                    }
                ]
            },
            {
                "name": "Gonaive",
                "communes":[
                    {
                        "name": "Ennery"
                    },
                    {
                        "name": "L'Estère"
                    },
                    {
                        "name": "Gonaïves"
                    }
                ]
            },
            {
                "name": "Gros-Morne",
                "communes": [
                    {
                        "name": "Anse-Rouge"
                    },
                    {
                        "name": "Gros-Morne"
                    },
                    {
                        "name": "Terre-Neuve"
                    }
                ]
            },
            {
                "name": "Marmelade",
                "communes":[
                    {
                        "name": "Marmelade"
                    },
                    {
                        "name": "Saint-Michel-de-l'Atalaye"
                    },
            },
            {
                "name": "Saint-Marc",
                "communes": [
                    {
                        "name": "La Chapelle"
                    },
                    {
                        "name": "Saint-Marc"
                    },
                    {
                        "name": "Verrettes"
                    },
                    {
                        "name": "Montrouis"
                    }
                ]
            }
        ]
    },
    {
        "name": "Centre",
        "capital": "Hinche",
        "area": 3487.41,
        "coordinates":{
            "latitude": 19.15,
            "longitude": -72.016667
        },
        "arrondissements": [
            {
                "name": "Cerca la Source",
                "communes": [
                    {
                        "name": "Cerca-la-Source"
                    },
                    {
                        "name": "Thomassique"
                    }
                ]
            },
            {
                "name": "Hinche",
                "communes": [
                    {
                        "name": "Hinche"
                    },
                    {
                        "name": "Cerca-Cavajal"
                    },
                    {
                        "name": "Maissade"
                    },
                    {
                        "name": "Thomonde"
                    }
                ]
            },
            {
                "name": "Lascahobas",
                "communes": [
                    {
                        "name": "Lascahobas"
                    },
                    {
                        "name": "Belladere"
                    },
                    {
                        "name": "Savanette"
                    }
                ]
            },
            {
                "name": "Mirebalais",
                "communes": [
                    {
                        "name": "Mirebalais"
                    },
                    {
                        "name": "Saut-d'Eau"
                    },
                    {
                        "name": "Boucan-Carre"
                    }
                ]
            }
        ]
    },
    {
        "name": "Ouest",
        "capital": "Port-au-Prince",
        "area": 4982.56,
        "coordinates":{
            "latitude": 19.15,
            "longitude": -72.016667
        }
        "arrondissements":[
            {
                "name": "Arcahaie",
                "communes":[
                    {
                        "name": "Arcahaie"
                    },
                    {
                        "name": "Cabaret"
                    }
                ]
            },
            {
                "name": "Croix-des-Bouquets",
                "communes": [
                    {
                        "name": "Croix-des-Bouquets"
                    },
                    {
                        "name": "Cornillon"
                    },
                    {
                        "name": "Fonds-Verettes"
                    },
                    {
                        "name": "Ganthier"
                    },
                    {
                        "name": "Thomazeau"
                    }
                ]
            },
            {
                "name": "La Gonâve",
                "communes": [
                    {
                        "name": "Anse-à-Galets"
                    },
                    {
                        "name": "Pointe-à-Raquette"
                    }
                ]
            },
            {
                "name": "Léogâne",
                "communes": [
                    {
                        "name": "Léogâne"
                    },
                    {
                        "name": "Grand-Goâve"
                    },
                    {
                        "name": "Petit-Goâve"
                    }
                ]
            },
            {
                "name": "Port-au-Prince"
                "communes": [
                    {
                        "name": "Port-au-Prince"
                    },
                    {
                        "name": "Carrefour"
                    },
                    {
                        "name": "Cité Soleil"
                    },
                    {
                        "name": "Delmas"
                    },
                    {
                        "name": "Gressier"
                    },
                    {
                        "name": "Kenscoff"
                    },
                    {
                        "name": "Pétion-Ville"
                    },
                    {
                        "name": "Tabarre"
                    }
                ]
            }
        ]
    },
    {
        "name": "Grand'Anse",
        "capital": "Jeremi",
        "area": 1911.97,
        "coordinates":{
            "latitude": 18.65,
            "longitude": -74.11
        },
        "arrondissements": [
            {
                "name": "Anse-d'Hainault",
                "communes": [
                    {
                        "name": "Anse-d'Hainault"
                    },
                    {
                        "name": "Dame-Marie"
                    },
                    {
                        "name": "Les Irois"
                    }
                ]
            },
            {
                "name": "Corail",
                "communes": [
                    {
                        "name": "Corail"
                    },
                    {
                        "name": "Beaumont"
                    },
                    {
                        "name": "Pestel"
                    },
                    {
                        "name": "Roseaux"
                    }
                ]
            },
            {
                "name": "Jérémie",
                "communes": [
                    {
                        "name": "Jérémie"
                    },
                    {
                        "name": "Abricots"
                    },
                    {
                        "name": "Bonbon"
                    },
                    {
                        "name": "Chambellan"
                    },
                    {
                        "name": "Moron"
                    },
                    {
                        "name": "Marfranc"
                    }
                ]
            }
        ]
    },
    {
        "name": "Sud",
        "capital": "Les Cayes",
        "area": 2653.6,
        "coordinates":{
            "latitude": 18.2,
            "longitude": -73.75
        },
        "arrondissements": [
            {
                "name": "Aquin",
                "communes": [
                    {
                        "name": "Aquin"
                    },
                    {
                        "name": "Cavaillon"
                    },
                    {
                        "name": "Saint-Louis du Sud"
                    }
                ]
            },
            {
                "name": "Chardonnières",
                "communes": [
                    {
                        "name": "Chardonnières"
                    },
                    {
                        "name": "Les Anglais"
                    },
                    {
                        "name": "Tiburon"
                    }
                ]
            },
            {
                "name": "Côteaux",
                "communes": [
                    {
                        "name": "Côteaux"
                    },
                    {
                        "name": "Port-à-Piment"
                    },
                    {
                        "name": "Roche-à-Bateaux"
                    }
                ]
            },
            {
                "name": "Les Cayes",
                "communes": [
                    {
                        "name": "Les Cayes"
                    },
                    {
                        "name": "Camp-Perrin"
                    },
                    {
                        "name": "Chantal"
                    },
                    {
                        "name": "Île à Vache"
                    },
                    {
                        "name": "Maniche"
                    },
                    {
                        "name": "Torbeck"
                    }
                ]
            },
            {
                "name": "Port-Salut",
                "communes": [
                    {
                        "name": "Port-Salut"
                    },
                    {
                        "name": "Arniquet"
                    },
                    {
                        "name": "Saint-Jean-du-Sud"
                    }
                ]
            }
        ]
    },
    {
        "name": "Sud-Est",
        "capital": "Jacmel",
        "area": 2034.1,
        "coordinates":{
            "latitude": 18.23,
            "longitude": -72.53
        },
        "arrondissements": [
            {
                "name": "Bainet",
                "communes": [
                    {
                        "name": "Bainet"
                    },
                    {
                        "name": "Côtes-de-Fer"
                    }
                ]
            },
            {
                "name": "Belle-Anse",
                "communes": [
                    {
                        "name": "Belle-Anse"
                    },
                    {
                        "name": "Anse-à-Pitres"
                    },
                    {
                        "name": "Grand-Gosier"
                    },
                    {
                        "name": "Thiotte"
                    }
                ]
            },
            {
                "name": "Jacmel",
                "communes": [
                    {
                        "name": "Jacmel"
                    },
                    {
                        "name": "Cayes-Jacmel"
                    },
                    {
                        "name": "La Vallée"
                    },
                    {
                        "name": "Marigot"
                    }
                ]
            }
        ]
    },
    {
        "name": "Nippe",
        "capital": "Miragoane",
        "area": 1267.77,
        "coordinates":{
            "latitude": 18.27,
            "longitude": -73.6
        },
        "arrondissements": [
            {
                "name": "Anse-à-Veau",
                "communes": [
                    {
                        "name": "Anse-à-Veau"
                    },
                    {
                        "name": "Arnaud"
                    },
                    {
                        "name": "L'Asile"
                    },
                    {
                        "name": "Petit-Trou-de-Nippes"
                    },
                    {
                        "name": "Plaisance-du-Sud"
                    }
                ]
            },
            {
                "name": "Baradères",
                "communes": [
                    {
                        "name": "Baradères"
                    },
                    {
                        "name": "Grand-Boucan"
                    }
                ]
            },
            {
                "name": "Miragoâne",
                "communes": [
                    {
                        "name": "Miragoâne"
                    },
                    {
                        "name": "Fonds-des-Nègres"
                    },
                    {
                        "name": "Paillant"
                    },
                    {
                        "name": "Petite-Rivière-de-Nippes"
                    }
                ]
            }
        ]
    },
    {
        "name": "Nord-Ouest",
        "capital": "Port-de-Paix",
        "area": 2102.88,
        "coordinates":{
            "latitude": 19.95,
            "longitude": -72.83
        },
        "arrondissements": [
            {
                "name": "Môle Saint Nicholas",
                "communes": [
                    {
                        "name": "Môle Saint Nicholas"
                    },
                    {
                        "name": "Jean-Rabel"
                    },
                    {
                        "name": "Bombardopolis"
                    },
                    {
                        "name": "Baie de Henne"
                    }
                ]
            },
            {
                "name": "Port-de-Paix",
                "communes": [
                    {
                        "name": "Port-de-Paix"
                    },
                    {
                        "name": "La Tortue"
                    },
                    {
                        "name": "Chansolme"
                    },
                    {
                        "name": "Bassin Bleu"
                    }
                ]
            },
            {
                "name": "Saint-Louis du Nord",
                "communes": [
                    {
                        "name": "Saint-Louis du Nord"
                    },
                    {
                        "name": "Anse-à-Foleur"
                    }
                ]
            }
        ] 
    },
    {
        "name": "Nord",
        "capital": "Cap-Haitian",
        "area": 2114.91,
        "coordinates":{
            "latitude": 19.7667,
            "longitude": -72.2
        } 
    },
    {
       "name": "Nord-Est",
        "capital": "Fort-Liberte",
        "area": 1622.93,
        "coordinates":{
            "latitude": 19.6678,
            "longitude": -71.8397
        }  
    }
]


def generate_pkl():
    # write python dict to a file
    loc = Locations.encode("utf-8")
    output = open('department.pkl', 'wb')
    cPickle.dumps(loc, output)
    output.close()

generate_pkl()
