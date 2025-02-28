import httpx

def get_exchange_rate():
    url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
    response = httpx.get(url)
    
    if response.status_code != 200:
        print("Chyba při načítání kurzu.")
        return None
    
    lines = response.text.split("\n")
    for line in lines:
        if "|EUR|" in line:
            row = line.split("|")
            return float(row[-1].replace(",", "."))
    
    print("Kurz nebyl nalezen.")
    return None

def convert_currency():
    rate = get_exchange_rate()
    if rate is None:
        return
    
    while True:
        print("Vyber typ převodu:")
        print("1: EUR -> CZK")
        print("2: CZK -> EUR")
        choice = input("Zadej číslo (1 nebo 2): ")
        
        if choice not in ["1", "2"]:
            print("Neplatná volba, zkuste to znovu.")
            continue
        
        while True:
            amount = input("Zadej částku: ")
            try:
                amount = float(amount)
                break
            except ValueError:
                print("Neplatná částka, zadejte číslo.")
        
        if choice == "1":
            result = amount * rate
            print(f"{amount} EUR = {result:.2f} CZK")
        else:
            result = amount / rate
            print(f"{amount} CZK = {result:.2f} EUR")
        
        again = input("Chcete provést další převod? (ano/ne): ").strip().lower()
        if again != "ano":
            break

if __name__ == "__main__":
    convert_currency()
