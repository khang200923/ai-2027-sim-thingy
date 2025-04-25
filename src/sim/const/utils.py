def number_type_with_anchors(end: int, anchors: dict[int, str]) -> str:
    return f"number from 0 to {end}; {', '.join(f'{n} is {a}' for n, a in anchors.items())}"

def get(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()
