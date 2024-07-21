import random


def genera_dummy_example():
    resp = [
        {"resultadoOperacion": "02", "motivoRechazo": "908", "fechaRespuesta": "30/11/2000 12:00:00"},
        {"resultadoOperacion": "01", "fechaRespuesta": "31/01/2023 11:59:40"},
    ]
    return random.choice(resp)
