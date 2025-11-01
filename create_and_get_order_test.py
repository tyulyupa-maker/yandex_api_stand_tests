import sender_stand_request
import data


def test_create_and_get_order_success():
    # Создание заказа
    create_response = sender_stand_request.post_create_order(data.order_body)
    assert create_response.status_code == 201, "Ошибка при создании заказа"

    # Получение трека
    track = create_response.json()["track"]
    print("Создан заказ, track =", track)

    # Получение заказа по треку
    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200, "Ошибка при получении заказа"
