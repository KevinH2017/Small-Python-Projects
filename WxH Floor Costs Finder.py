# Find Estimated Cost of Tile to Cover Width x Height Floor
# User inputs Width, Height, and costs

def tile_calc():
    user_w = float(input("Width: "))
    user_h = float(input("Height: "))

    user_cost = float(input("Cost: "))

    Width_Height = user_w * user_h

    total_cost = Width_Height * user_cost
    total_cost_string = '{:,.2f}'.format(total_cost)                          # Creates commas for thousands with 2 decimals for cents
    print("Estimated total cost would be about $" + total_cost_string)        # Adds $ symbol

tile_calc()