def format_datetime(value, fmt="%Y년 %m월 %d일 %H:%M"):
    # value는 datetime 객체, value를 fmt 형식으로 변환
    return value.strftime(fmt)