import json
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import SparkSession

def extract_reviews(json_response):
    reviews = json_response.get('reviews', [])
    extracted_reviews = {}
    for review in reviews:
        i = review['asin']['original']
        if not extracted_reviews.get(i):
            extracted_reviews[i] = [
            {'rating': review['rating'], 
            'title': review['title'], 
            'review': review['review']
            }]
        else:
            extracted_reviews[i] += [ 
            {'rating': review['rating'], 
            'title': review['title'], 
            'review': review['review']
            }]
    return extracted_reviews

def trigger_api(product_asin, page_no):
    '''
    This function accepts the product’s ASIN and the page number as arguments. 
    The country is set to “US” so the program will only work with the products 
    listed on Amazon’s US website. It invokes the API via the requests library 
    and returns an API response in JSON format. 
    '''
    querystring = {"page": str(page_no) ,  "country":"US" , "asin": product_asin}
    headers = {
    'x-rapidapi-host': "amazon-product-reviews-keywords.p.rapidapi.com",
    'x-rapidapi-key': "e155b49501msh0172d07b4bed653p11ccd6jsn2a9f2b62d0ee"
    }
    url = "https://amazon-product-reviews-keywords.p.rapidapi.com/product/reviews"
    response = requests.request("GET", url, headers=headers, params=querystring)
    if(200 == response.status_code):
        # print(response.text)
        return extract_reviews(json.loads(response.text))
    else:
        return None



# if __name__ == "__main__":
def step1():
    # li = ['B098F9B796', 'B09HC3TWXY', 'B09H3ZWV3S', 'B08DTZY81Z', 'B07VWLDBMR', 'B09V5LNQSC', 'B08CL2DBF1', 'B07KWDH8HD', 'B0BTZWVNML', 'B096XML621', 'B08XBC5PSR', 'B07YF81T39', 'B09MFMFD6T', 'B08XJFWK3D', 'B086P935X6', 'B00L3ESYXC', 'B09QQSZC7P', 'B08M4JN955', 'B09S5234YL', 'B098NDGDFH', 'B09WJ3NTLM', 'B07QY4HSL1', 'B0913H16F1', 'B01KJMDK1E',    'B071JNKK11',     'B07N2F3JXP',    'B08FXD5SNC',    'B00WH1RTTU',    'B0834X56QF',    'B07PY3D9M7',    'B077K6BNXL',    'B082YY63R5',    'B0B5GVNJPR',    'B079K8L72H',    'B09LD7WRVS',    'B07HF3X6Y4',    'B009S750LA',    'B086X7QKHD',    'B08C4KWM9T']
    li = ['B098F9B796']
    m = {}
    for i in li:
        for j in range(1,5):
            temp = trigger_api(i,j)
            if i in m.keys():
                m[i] += temp[i]
            else:
                m[i] = temp[i]
    # m
    # with open('my_dict.json', 'w') as f:
    #     json.dump(m, f)
    
    
    # return {"status": 404}
    return m