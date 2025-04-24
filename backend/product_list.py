from datetime import datetime

def cr_products(title, price, total_rev, img_url):
    create_p = {
        "title" : title,
        "price" : price,
        "total_reviews" : total_rev,
        "image_url" : img_url,
        "scraped_time" : datetime.now().isoformat()
    }
    return create_p