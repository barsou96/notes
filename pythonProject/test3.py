import logging
logging.basicConfig(filename="test4.log", level=logging.INFO , format= '%(asctime)s %(name)s %(levelname)s %(message)s')

def devide(a,b) :
    logging.info("the number entered by user is %s and %s" , a,b)
    try:
        logging.info("we are into function")
        div = a/b
        logging.info("we have completed a division operation")
        logging.info("result of code is %s " , div)
        return div
    except Exception as e :
        logging.exception(e)




print((devide(3,7)))