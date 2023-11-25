basket = {
    "LW": {"quantity": 1, "unit_price": 1100, "gst":18},
    "Cig": {"quantity": 4, "unit_price": 900, "gst":12},
    "Umb": {"quantity": 12, "unit_price": 200, "gst":8},
    "Haney": {"quantity": 28, "unit_price": 100, "gst":0},
}

maxgstprd = None
maxgstamt = 0

for prd, details in basket.items():
    quantity = details["quantity"]
    uprice = details["unit_price"]
    gstamt = details["gst"] * (quantity * uprice) 

    if gstamt > maxgstamt:
        maxgstamt = gstamt
        maxgstprd = prd

tamount = sum(details["quantity"] * details["unit_price"] for details in basket.values())


print("Product with maximum GST:", maxgstprd)
print("Maximum GST amount:", maxgstamt)
print("Total amount to be paid:",tamount)