
def validate_age(age_input):
    try:
        age = int(age_input)
        if age <= 0:
            raise ValueError("A idade deve ser um número positivo.")
        return age
    except ValueError as e:
        print(f"Erro: {e}")
        return None
