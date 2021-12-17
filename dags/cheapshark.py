
import json
from csv import DictWriter,writer
from datetime import date
import requests
import json
import csv

def getStoreData():
    response_stores = requests.get('https://www.cheapshark.com/api/1.0/stores')
    dicts = json.loads(response_stores.text)
    #the_file = open("/usr/local/airflow/store_files_airflow/store.csv", "w")
    the_file = open("store.csv", "w")
    #print (dicts)
    writer = DictWriter(the_file, dicts[0].keys())
    writer.writeheader()
    writer.writerows(dicts)
    the_file.close()

def getDealGameData():
    response_deals = requests.get('https://www.cheapshark.com/api/1.0/deals')
    json_deals = json.loads(response_deals.text)
    """ the_file = open("deals.csv", "w")
    writer = DictWriter(the_file, json_deals[0].keys())
    writer.writeheader()
    writer.writerows(json_deals)
    the_file.close() """
    isfirsttime  = 1
    game_file = open("gamesinfo.csv", "a")
    cheapprice_file = open("cheapestPriceEver.csv", "a")
    deal_file = open("deal.csv", "a")

    for deals in json_deals:
        gameID = deals["gameID"]
        response_games = requests.get('https://www.cheapshark.com/api/1.0/games?id='+gameID)
        json_games = json.loads(response_games.text)
        json_games['info']['gameid'] = gameID
        writer = DictWriter(game_file, json_games['info'].keys())
        if isfirsttime == 1:
            writer.writeheader()
        #for row in json_games['info'].items():
         #   print(row)
        
        csv.writer(game_file).writerow(row[1] for row in json_games['info'].items())

        json_games['cheapestPriceEver']['gameId'] = gameID
        writer = DictWriter(cheapprice_file, json_games['cheapestPriceEver'].keys())
        if isfirsttime == 1:
            writer.writeheader()
            isfirsttime = 0
        csv.writer(cheapprice_file).writerow(row[1] for row in json_games['cheapestPriceEver'].items())

        csv_writer = csv.writer(deal_file)
        count = 0
        for i in json_games["deals"]:
            i['gameId'] = gameID
            for deal in i.items():
                print (deal.keys())
                #if count == 0:
                 #   header = deal.keys()
                  #  csv_writer.writerow(header)

                # Writing data of CSV file
                #csv_writer.writerow(deal.values())
            
            #writer = DictWriter(deal_file, i.keys())
            #writer.writeheader()
            #writer.writerows(i)
        #writer = DictWriter(deal_file, json_games['deals'].keys())
        #csv.writer(deal_file).writerow(row[1] for row in json_games['deals'].items())
        """ for i in json_games["deals"]:
            print (i)
            break """
        break

    cheapprice_file.close()
    game_file.close()
    deal_file.close()
if __name__ == "__main__":
    getStoreData()
    getDealGameData()
   
