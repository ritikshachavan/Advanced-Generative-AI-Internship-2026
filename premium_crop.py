def premium_crop_filter(prices):
    premium_crops = []

    for price in prices:
        if price > 2000:
            premium_crops.append(price)

    print("Premium Crops:", premium_crops)


# Example Input
crop_prices = [1500, 2500, 3200, 1800]
premium_crop_filter(crop_prices)