from model.Product import Product


def to_model(title, price, url_img):
    data = Product

    data.name = title
    data.price = float(price)
    data.image = url_img
    data.origin = "LOCATEL"
    return data


