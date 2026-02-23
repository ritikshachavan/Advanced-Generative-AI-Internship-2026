def medicine_stock_alert(stock):
    if stock < 10:
        status = "Low Stock Alert"
    else:
        status = "Stock Sufficient"

    print("Medicine Stock:", stock)
    print("Status:", status)


# Input
medicine_stock_alert(6)