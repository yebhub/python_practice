def get_formatted_city(city, country, population = ''):
    if population:
        formatted_city_name = city.title() + ", " + country.title() + "\npopulation: " + str(population) + " million."
    else:
        formatted_city_name = city.title() + ", " + country.title()

    return(formatted_city_name)
