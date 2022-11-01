COLOR_NAME_TO_COLOR_CODE = {
    "aliceblue": "#f0f8ff",
    "aqua": "#00ffff",
    "beaver": "#9f8170",
    "bitter lime": "#bfff00",
    "blue4": "#00008b",
    "cadmium orange": "#ed872d",
    "dandelion": "#f0e130",
    "darkdeagreen": "#8fbc8f",
    "ferrari red": "#ff2800",
    "gray": "#bebebe"
}

color_name = input("Enter color name (hit enter to quit):  ").lower()
while color_name != "":
    if color_name in COLOR_NAME_TO_COLOR_CODE:  # find key
        print(f"{color_name} is {COLOR_NAME_TO_COLOR_CODE[color_name]}")
    else:
        print("Invalid color name")
    color_name = input("Enter color name (hit enter to quit):  ").lower()
print("Bye.")
