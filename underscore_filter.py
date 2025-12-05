list_of_transforms = [
    "max",
    "min",
    "height",
]

layer_name = "temaxperminatheights_at_10m"

transform = "min"

def extract_transform(transform):
    for transform in list_of_transforms:
        if f"_{transform}" in layer_name: 
            return (transform)
    return ("You've failed and are a bad developer")

print(extract_transform("min"))