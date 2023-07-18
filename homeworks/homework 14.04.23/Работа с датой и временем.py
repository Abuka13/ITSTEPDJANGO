from datetime import datetime, timezone, timedelta


def get_time_gmt_and_local():
    # Получаем текущее время по Гринвичу
    gmt_time = datetime.now(timezone.utc)

    # Получаем смещение местного времени относительно Гринвича
    local_timezone = datetime.now().astimezone().tzinfo
    local_offset = local_timezone.utcoffset(gmt_time)

    # Вычисляем местное время на основе Гринвического времени и смещения
    local_time = gmt_time + local_offset

    return gmt_time, local_time


if __name__ == "__main__":
    gmt_time, local_time = get_time_gmt_and_local()

    print("Текущее время по Гринвичу: ", gmt_time.strftime('%Y-%m-%d %H:%M:%S'))
    print("Местное время: ", local_time.strftime('%Y-%m-%d %H:%M:%S'))