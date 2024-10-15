import requests
import json

# Define API URL and headers
RENDER_API_URL = " http://127.0.0.1:5000/query"  # Changed to localhost
headers = {
    "Content-Type": "application/json"
}

# Load queries from JSON string
queries = [
    {
        "db": "demo_db",
        "collection": "movies",
        "type of query": "find",
        "query": {
            "title": "The green mile"
        }
    },
    {
        "db": "demo_db",
        "collection": "movies",
        "type of query": "find",
        "query": {
            "release_year": 2024
        }
    }
]

columns = [
    {
        "db": "demo_db",
        "collection": "employees_99",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_119",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_128",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_87",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_68",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_83",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_72",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_67",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_118",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_106",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_144",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_71",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_14",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_60",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_83",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_2",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_114",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_111",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_154",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_75",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_88",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_42",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_151",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_28",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_78",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_7",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_114",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_137",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_142",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_157",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_92",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_56",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_5",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_132",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_25",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_142",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_63",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_145",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_129",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_136",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_76",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_50",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_37",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_9",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_58",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_59",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_71",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_120",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_127",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_116",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_50",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_1",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_120",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_123",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_3",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_73",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_22",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_26",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_60",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_96",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_6",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_18",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_59",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_17",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_61",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_38",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_91",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_44",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_23",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_72",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_82",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_66",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_118",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_77",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_95",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_33",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_161",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_132",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_106",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_2",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_84",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_112",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_143",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_38",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_150",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_86",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_32",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_115",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_107",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_33",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_110",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_22",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_64",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_7",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_134",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_65",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_97",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_159",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_122",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_87",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_16",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_57",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_13",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_58",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_85",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_46",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_146",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_125",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_6",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_149",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_49",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_30",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_108",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_10",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_124",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_42",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_139",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_19",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_160",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_76",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_10",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_103",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_85",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_11",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_156",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_39",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_25",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_52",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_149",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_105",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_148",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_47",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_40",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_70",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_35",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_32",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_160",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_130",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_101",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_80",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_143",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_53",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_45",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_147",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_113",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_100",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_21",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_24",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_98",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_151",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_74",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_154",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_3",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_134",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_94",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_89",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_40",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_84",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_152",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_4",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_81",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_153",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_109",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_68",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_104",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_23",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_158",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_104",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_29",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_62",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_138",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_37",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_122",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_17",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_79",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_27",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_55",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_91",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_109",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_157",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_21",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_61",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_89",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_113",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_28",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_94",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_140",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_41",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_46",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_110",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_20",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_111",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_103",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_30",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_14",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_26",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_126",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_80",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_9",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_135",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_90",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_96",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_137",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_161",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_65",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_107",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_117",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_8",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_49",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_123",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_64",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_57",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_45",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_121",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_146",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_27",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_79",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_153",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_136",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_53",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_100",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_51",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_93",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_31",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_73",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_56",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_20",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_5",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_101",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_138",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_44",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_131",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_141",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_112",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_36",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_48",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_141",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_8",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_133",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_130",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_95",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_99",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_66",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_140",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_82",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_70",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_35",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_115",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_135",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_121",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_48",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_127",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_90",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_147",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_69",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_125",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_108",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_81",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_156",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_116",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_13",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_36",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_54",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_74",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_117",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_24",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_12",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_16",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_98",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_78",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_150",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_29",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_155",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_12",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_39",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_126",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_102",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_15",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_88",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_102",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_52",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_15",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_55",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_133",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_128",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_18",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_145",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_43",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_11",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_69",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_77",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_4",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_34",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_105",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_54",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_124",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_159",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_155",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_119",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_148",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_19",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_75",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_158",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_139",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_86",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_67",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_129",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_41",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_47",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_93",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_97",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_131",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_63",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_43",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_62",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_34",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "movies_152",
        "columns": "director, genre, rating, release_year, title"
    },
    {
        "db": "demo_db",
        "collection": "employees_92",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_51",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "employees_1",
        "columns": "active, address, age, email, name, phone"
    },
    {
        "db": "demo_db",
        "collection": "movies_31",
        "columns": "director, genre, rating, release_year, title"
    }
]

results = []

for query in queries:
    payload = {
        "db": query['db'],
        "query_type": query['type of query'],
        "query": query['query']
    }

    try:
        # Print the payload for debugging purposes
        print(f"Sending payload: {payload} to {RENDER_API_URL}")

        response = requests.post(
            RENDER_API_URL,
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            data = response.json()
            print(f"Response for query {query}: {data}")  # Print the response for debugging
            results.append({"db": query['db'], "query": query['query'], "results": data})
        else:
            error_message = response.json().get("error", response.text)
            results.append({"query": query, "error": f"Failed to retrieve data: {response.status_code}, {error_message}"})
    except requests.exceptions.RequestException as e:
        results.append({"query": query, "error": f"Request failed: {e}"})

print(results)
list_of_lists = []
column_list = []
for col in columns:
    column_list.extend(col['columns'])

# Remove duplicates and create a unique column list
column_list = list(set(col.strip() for col in column_list))
list_of_lists.append(column_list)  # Change to append the unique column list

for entry in results:
    print(entry)
    query = json.dumps(entry['query'], ensure_ascii=False)
    db = json.dumps(entry['db'], ensure_ascii=False)
    result_values = entry['results']

    if result_values:
        for i in range(len(result_values)):
            result = result_values[i]
            result_json = json.dumps(result, ensure_ascii=False)  # Convert result to JSON string

            if i == 0:
                list_of_lists.append([
                    db,
                    query,
                    result_json  
                ])
            else:
                list_of_lists.append([
                    '',  # Keep the same db and query values for subsequent results
                    '',
                    result_json  
                ])
    else:
        list_of_lists.append([db, query, ''])

def list_of_lists_to_json_format(list_of_lists):
    headers = list_of_lists[0]
    data_rows = list_of_lists[1:]
    result = []
    for row in data_rows:
        row_dict = {}
        for header, value in zip(headers, row):
            row_dict[header] = value
        result.append(row_dict)
    return result

# Converting to JSON
json_format_data = list_of_lists_to_json_format(list_of_lists)
json_string = json.dumps(json_format_data, ensure_ascii=False, indent=4)
print(json_string)  # Print the final JSON string for debugging