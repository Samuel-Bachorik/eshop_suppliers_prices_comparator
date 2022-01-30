# Just demo, work in progess 

Piece ofprogram that helps my e-shop to get the cheapest suppliers of all products. This program evaluates whether the goods are still in stock, whether the selected margin is achievable with current supplier prices and if supplier deleted product or changed the price of product. This program also finds out if there is a cheaper supplier than the one I have.

### What it does
- For each product, it can handle a different supplier
- Checks if i have cheapest supplier of particular product
- Checks if i have desired margin
- Checks if product is still available
- Checks if suplier changed the price
### How it works

- I created my own database of products in Google Sheets (Manually added products)
- This database consist of 3 columns - My shop, supplier, Heureka
- Web scraper takes prices and availablity out of theese websites
- All of this runs on multiprocessing
- The number of processed products is divided between the processes

![Table](https://github.com/Samuel-Bachorik/eshop_suppliers_prices_comparator/blob/main/table.jpg)
### If the program finds a mismatch it throws warning and number row in table
