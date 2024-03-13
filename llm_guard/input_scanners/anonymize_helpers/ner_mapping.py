DISTILBERT_BASE_NER_CONF = {
    "PRESIDIO_SUPPORTED_ENTITIES": [
        "LOCATION",
        "PERSON",
        "ORGANIZATION",
    ],
    "DEFAULT_MODEL_PATH": "dslim/distilbert-NER",
    "ONNX_MODEL_PATH": "dslim/distilbert-NER",
    "LABELS_TO_IGNORE": ["O", "CARDINAL"],
    "DEFAULT_EXPLANATION": "Identified as {} by the dslim/bert-base-NER NER model",
    "SUB_WORD_AGGREGATION": "simple",
    "DATASET_TO_PRESIDIO_MAPPING": {
        "MISC": "O",
        "LOC": "LOCATION",
        "ORG": "ORGANIZATION",
        "PER": "PERSON",
    },
    "MODEL_TO_PRESIDIO_MAPPING": {
        "MISC": "O",
        "LOC": "LOCATION",
        "ORG": "ORGANIZATION",
        "PER": "PERSON",
    },
    "CHUNK_OVERLAP_SIZE": 40,
    "CHUNK_SIZE": 600,
    "ID_SCORE_MULTIPLIER": 0.4,
    "ID_ENTITY_NAME": "ID",
}

BERT_BASE_NER_CONF = {
    "PRESIDIO_SUPPORTED_ENTITIES": [
        "LOCATION",
        "PERSON",
        "ORGANIZATION",
    ],
    "DEFAULT_MODEL_PATH": "dslim/bert-base-NER",
    "ONNX_MODEL_PATH": "dslim/bert-base-NER",
    "LABELS_TO_IGNORE": ["O", "CARDINAL"],
    "DEFAULT_EXPLANATION": "Identified as {} by the dslim/bert-base-NER NER model",
    "SUB_WORD_AGGREGATION": "simple",
    "DATASET_TO_PRESIDIO_MAPPING": {
        "MISC": "O",
        "LOC": "LOCATION",
        "ORG": "ORGANIZATION",
        "PER": "PERSON",
    },
    "MODEL_TO_PRESIDIO_MAPPING": {
        "MISC": "O",
        "LOC": "LOCATION",
        "ORG": "ORGANIZATION",
        "PER": "PERSON",
    },
    "CHUNK_OVERLAP_SIZE": 40,
    "CHUNK_SIZE": 600,
    "ID_SCORE_MULTIPLIER": 0.4,
    "ID_ENTITY_NAME": "ID",
}

BERT_LARGE_NER_CONF = {
    "PRESIDIO_SUPPORTED_ENTITIES": [
        "LOCATION",
        "PERSON",
        "ORGANIZATION",
    ],
    "DEFAULT_MODEL_PATH": "dslim/bert-large-NER",
    "ONNX_MODEL_PATH": "dslim/bert-large-NER",
    "LABELS_TO_IGNORE": ["O", "CARDINAL"],
    "DEFAULT_EXPLANATION": "Identified as {} by the dslim/bert-large-NER NER model",
    "SUB_WORD_AGGREGATION": "simple",
    "DATASET_TO_PRESIDIO_MAPPING": {
        "MISC": "O",
        "LOC": "LOCATION",
        "ORG": "ORGANIZATION",
        "PER": "PERSON",
    },
    "MODEL_TO_PRESIDIO_MAPPING": {
        "MISC": "O",
        "LOC": "LOCATION",
        "ORG": "ORGANIZATION",
        "PER": "PERSON",
    },
    "CHUNK_OVERLAP_SIZE": 40,
    "CHUNK_SIZE": 600,
    "ID_SCORE_MULTIPLIER": 0.4,
    "ID_ENTITY_NAME": "ID",
}

BERT_ZH_NER_CONF = {
    "PRESIDIO_SUPPORTED_ENTITIES": [
        "LOCATION",
        "PERSON",
        "ORGANIZATION",
    ],
    "DEFAULT_MODEL_PATH": "gyr66/bert-base-chinese-finetuned-ner",
    "ONNX_MODEL_PATH": "ProtectAI/gyr66-bert-base-chinese-finetuned-ner-onnx",
    "LABELS_TO_IGNORE": ["O", "CARDINAL"],
    "DEFAULT_EXPLANATION": "Identified as {} by the gyr66/bert-base-chinese-finetuned-ner NER model",
    "SUB_WORD_AGGREGATION": "simple",
    "DATASET_TO_PRESIDIO_MAPPING": {
        "MISC": "O",
        "address": "LOCATION",
        "company": "ORGANIZATION",
        "name": "PERSON",
    },
    "MODEL_TO_PRESIDIO_MAPPING": {
        "MISC": "O",
        "address": "LOCATION",
        "company": "ORGANIZATION",
        "name": "PERSON",
    },
    "CHUNK_OVERLAP_SIZE": 40,
    "CHUNK_SIZE": 600,
    "ID_SCORE_MULTIPLIER": 0.4,
    "ID_ENTITY_NAME": "ID",
}

DISTILBERT_AI4PRIVACY_v2_CONF = {
    "PRESIDIO_SUPPORTED_ENTITIES": [
        "LOCATION",
        "PERSON",
        "ORGANIZATION",
        "EMAIL_ADDRESS",
        "PHONE_NUMBER",
        "CREDIT_CARD",
        "CRYPTO",
        "DATE_TIME",
        "IBAN_CODE",
        "IP_ADDRESS",
        "URL",
    ],
    "DEFAULT_MODEL_PATH": "Isotonic/distilbert_finetuned_ai4privacy_v2",
    "ONNX_MODEL_PATH": "Isotonic/distilbert_finetuned_ai4privacy_v2",
    "LABELS_TO_IGNORE": ["O", "CARDINAL"],
    "DEFAULT_EXPLANATION": "Identified as {} by the Isotonic/distilbert_finetuned_ai4privacy_v2 NER model",
    "SUB_WORD_AGGREGATION": "simple",
    "DATASET_TO_PRESIDIO_MAPPING": {
        "MISC": "O",
        "STREET": "LOCATION",
        "CITY": "LOCATION",
        "ZIPCODE": "LOCATION",
        "BUILDINGNUMBER": "LOCATION",
        "NEARBYGPSCOORDINATES": "LOCATION",
        "SECONDARYADDRESS": "LOCATION",
        "STATE": "LOCATION",
        "COUNTY": "LOCATION",
        "EMAIL": "EMAIL_ADDRESS",
        "COMPANYNAME": "ORGANIZATION",
        "PHONENUMBER": "PHONE_NUMBER",
        "FIRSTNAME": "PERSON",
        "LASTNAME": "PERSON",
        "MIDDLENAME": "PERSON",
        "USERNAME": "PERSON",
        "CREDITCARDNUMBER": "CREDIT_CARD",
        "ETHEREUMADDRESS": "CRYPTO",
        "BITCOINADDRESS": "CRYPTO",
        "LITECOINADDRESS": "CRYPTO",
        "DATE": "DATE_TIME",
        "TIME": "DATE_TIME",
        "DOB": "DATE_OF_BIRTH",
        "IBAN": "IBAN_CODE",
        "IPV4": "IP_ADDRESS",
        "IPV6": "IP_ADDRESS",
        "IP": "IP_ADDRESS",
        "URL": "URL",
        "AGE": "AGE",
    },
    "MODEL_TO_PRESIDIO_MAPPING": {
        "MISC": "O",
        "STREET": "LOCATION",
        "CITY": "LOCATION",
        "ZIPCODE": "LOCATION",
        "BUILDINGNUMBER": "LOCATION",
        "NEARBYGPSCOORDINATES": "LOCATION",
        "SECONDARYADDRESS": "LOCATION",
        "STATE": "LOCATION",
        "COUNTY": "LOCATION",
        "EMAIL": "EMAIL_ADDRESS",
        "COMPANYNAME": "ORGANIZATION",
        "PHONENUMBER": "PHONE_NUMBER",
        "FIRSTNAME": "PERSON",
        "LASTNAME": "PERSON",
        "MIDDLENAME": "PERSON",
        "USERNAME": "PERSON",
        "CREDITCARDNUMBER": "CREDIT_CARD",
        "ETHEREUMADDRESS": "CRYPTO",
        "BITCOINADDRESS": "CRYPTO",
        "LITECOINADDRESS": "CRYPTO",
        "DATE": "DATE_TIME",
        "TIME": "DATE_TIME",
        "DOB": "DATE_OF_BIRTH",
        "IBAN": "IBAN_CODE",
        "IPV4": "IP_ADDRESS",
        "IPV6": "IP_ADDRESS",
        "IP": "IP_ADDRESS",
        "URL": "URL",
        "AGE": "AGE",
    },
    "CHUNK_OVERLAP_SIZE": 40,
    "CHUNK_SIZE": 600,
    "ID_SCORE_MULTIPLIER": 0.4,
    "ID_ENTITY_NAME": "ID",
}

DEBERTA_AI4PRIVACY_v2_CONF = {
    "PRESIDIO_SUPPORTED_ENTITIES": [
        "LOCATION",
        "PERSON",
        "ORGANIZATION",
        "EMAIL_ADDRESS",
        "PHONE_NUMBER",
        "CREDIT_CARD",
        "CRYPTO",
        "DATE_TIME",
        "IBAN_CODE",
        "IP_ADDRESS",
        "URL",
    ],
    "DEFAULT_MODEL_PATH": "Isotonic/deberta-v3-base_finetuned_ai4privacy_v2",
    "ONNX_MODEL_PATH": "Isotonic/deberta-v3-base_finetuned_ai4privacy_v2",
    "LABELS_TO_IGNORE": ["O", "CARDINAL"],
    "DEFAULT_EXPLANATION": "Identified as {} by the Isotonic/deberta-v3-base_finetuned_ai4privacy_v2 NER model",
    "SUB_WORD_AGGREGATION": "simple",
    "DATASET_TO_PRESIDIO_MAPPING": {
        "MISC": "O",
        "STREET": "LOCATION",
        "CITY": "LOCATION",
        "ZIPCODE": "LOCATION",
        "BUILDINGNUMBER": "LOCATION",
        "NEARBYGPSCOORDINATES": "LOCATION",
        "SECONDARYADDRESS": "LOCATION",
        "STATE": "LOCATION",
        "COUNTY": "LOCATION",
        "EMAIL": "EMAIL_ADDRESS",
        "COMPANYNAME": "ORGANIZATION",
        "PHONENUMBER": "PHONE_NUMBER",
        "FIRSTNAME": "PERSON",
        "LASTNAME": "PERSON",
        "MIDDLENAME": "PERSON",
        "USERNAME": "PERSON",
        "CREDITCARDNUMBER": "CREDIT_CARD",
        "ETHEREUMADDRESS": "CRYPTO",
        "BITCOINADDRESS": "CRYPTO",
        "LITECOINADDRESS": "CRYPTO",
        "DATE": "DATE_TIME",
        "TIME": "DATE_TIME",
        "DOB": "DATE_OF_BIRTH",
        "IBAN": "IBAN_CODE",
        "IPV4": "IP_ADDRESS",
        "IPV6": "IP_ADDRESS",
        "IP": "IP_ADDRESS",
        "URL": "URL",
        "AGE": "AGE",
    },
    "MODEL_TO_PRESIDIO_MAPPING": {
        "MISC": "O",
        "STREET": "LOCATION",
        "CITY": "LOCATION",
        "ZIPCODE": "LOCATION",
        "BUILDINGNUMBER": "LOCATION",
        "NEARBYGPSCOORDINATES": "LOCATION",
        "SECONDARYADDRESS": "LOCATION",
        "STATE": "LOCATION",
        "COUNTY": "LOCATION",
        "EMAIL": "EMAIL_ADDRESS",
        "COMPANYNAME": "ORGANIZATION",
        "PHONENUMBER": "PHONE_NUMBER",
        "FIRSTNAME": "PERSON",
        "LASTNAME": "PERSON",
        "MIDDLENAME": "PERSON",
        "USERNAME": "PERSON",
        "CREDITCARDNUMBER": "CREDIT_CARD",
        "ETHEREUMADDRESS": "CRYPTO",
        "BITCOINADDRESS": "CRYPTO",
        "LITECOINADDRESS": "CRYPTO",
        "DATE": "DATE_TIME",
        "TIME": "DATE_TIME",
        "DOB": "DATE_OF_BIRTH",
        "IBAN": "IBAN_CODE",
        "IPV4": "IP_ADDRESS",
        "IPV6": "IP_ADDRESS",
        "IP": "IP_ADDRESS",
        "URL": "URL",
        "AGE": "AGE",
    },
    "CHUNK_OVERLAP_SIZE": 40,
    "CHUNK_SIZE": 600,
    "ID_SCORE_MULTIPLIER": 0.4,
    "ID_ENTITY_NAME": "ID",
}
