import requests
import configuration


def post_create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body,
                         verify=False)


def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + "?t=" + str(track),
                        verify=False)
