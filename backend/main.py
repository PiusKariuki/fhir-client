from fastapi import FastAPI
from fhir.resources.patient import Patient

app = FastAPI()

def create_patient():
    patient = Patient(
        id="example-patient",
        active=True,
        name=[{
            "use": "official",
            "family": "Doe",
            "given": ["John"]
        }],
        gender="male",
        birthDate="1990-05-10"
    )

    return patient.dict()


    # convert Patient to json
    patient_json = patient.json(indent=2)
    print("FHIR Patient Resource:\n", patient_json)

    # save to a file (optional)
    with open("../patient.json", "w") as file:
        file.write(patient_json)

    return patient_json

@app.get("/patient/{patient_id}")
def get_patient(patient_id: str):
    # Here you would typically query your database to retrieve a patient.
    # For simplicity, we're returning the example patient.
    if patient_id == "example-patient":
        patient = Patient(
            id="example-patient",
            active=True,
            name=[{
                "use": "official",
                "family": "Doe",
                "given": ["John"]
            }],
            gender="male",
            birthDate="1990-05-10"
        )
        return patient.dict()
    else:
        return {"detail": "Patient not found"}



if __name__ == "__main__":
    create_patient()