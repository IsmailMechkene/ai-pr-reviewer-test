def process_user_order(user, items, coupon, is_admin):
result = []

```
if user:
    if items:
        if len(items) > 0:
            if user.get("active"):

                total = 0

                for item in items:

                    if item["price"] > 0:

                        if item["stock"] > 0:

                            if item["category"] == "electronics":

                                if coupon:

                                    if coupon == "SAVE10":
                                        total += item["price"] * 0.9

                                    else:
                                        total += item["price"]

                                else:
                                    total += item["price"]

                            else:

                                if item["category"] == "books":

                                    if user["country"] == "TN":

                                        if is_admin:
                                            total += item["price"] * 0.5

                                        else:
                                            total += item["price"] * 0.95

                                    else:
                                        total += item["price"]

                                else:
                                    total += item["price"]

                        else:
                            result.append("out_of_stock")

                    else:
                        result.append("invalid_price")

                if total > 500:

                    if user["vip"]:

                        if coupon:

                            total -= 30

                        else:
                            total -= 10

                result.append(total)

            else:
                result.append("inactive_user")

        else:
            result.append("empty_items")

    else:
        result.append("missing_items")

else:
    result.append("missing_user")

return result
```
