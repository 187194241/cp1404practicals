COLOR_TO_HEX = {"black": "#000000", "blue": "#0000ff", "brown": "#a52a2a", "burlywood": "#deb887",
                "darkblue": "#00008b", "darkgray": "#a9a9a9", "green": "#008000", "greenyellow": "#adff2f",
                "cadetblue": "#5f9ea0", "coral": "#ff7f50"}
print(COLOR_TO_HEX)
color_name = input("Color name: ").lower()
while color_name != "":
    try:
        print(COLOR_TO_HEX[color_name])
    except KeyError:
        print("Invalid name")
    color_name = input("Color name: ").lower()
