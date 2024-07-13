"""
Word Occurrences
Estimate: 30 minutes
Actual:    minutes
"""
import csv
def read_wimbledon_data(filename):
    champions = []
    with open(filename, "r",  encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            champions.append(row)
    return champions

def process_data(champions):
    champion_count = {}
    countries = set()
    for champion in champions:
        name = champion[2]
        country = champion[1]
        if name in champion_count:
            champion_count[name] += 1
        else:
            champion_count[name] = 1
        countries.add(country)
    sorted_countries = sorted(countries)
    return champion_count, sorted_countries

def display_results(champion_count, sorted_countries):
    print("Wimbledon Champions:")
    for champion, count in champion_count.items():
        print(f"{champion} {count}")
    print("\nThese", len(sorted_countries), "countries have won Wimbledon:")
    print(", ".join(sorted_countries))

def main():
    filename = "wimbledon.csv"
    champions = read_wimbledon_data(filename)
    champion_count, sorted_countries = process_data(champions)
    display_results(champion_count, sorted_countries)

main()