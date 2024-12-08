from datetime import datetime, timezone, timedelta


def get_date_str():
  # JST（UTC+9）タイムゾーンを設定
  jst = timezone(timedelta(hours=9))

  # 現在のJSTの日時を取得
  current_time_jst = datetime.now(jst)

  # 日付と時間を文字列で取得
  date_str = current_time_jst.strftime("%Y%m%d%H%M%S")

  return date_str

if __name__ == "__main__":
  print(get_data_str())