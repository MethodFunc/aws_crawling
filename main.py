import warnings
import json
import pandas as pd
from pathlib import Path
from setting import logger
from datetime import datetime, timedelta
from joblib import Parallel, delayed
from module.crawling import get_result, arg_setting


warnings.filterwarnings('ignore')


def main(args):
    # 해당 관측지점 및 지역명은 직접 찾아야함. 해당 데이터는 제주도 위주의 데이터가 들어있음
    data = ...
    data = json.loads(data)
    aws_info = pd.DataFrame(data)

    date_list = [
        (datetime(args.year, args.month, args.day, args.hour) + timedelta(hours=i)).strftime("%Y%m%d%H%M")
        for i in range(args.range_date * 24)
    ]

    total_start = datetime.now()
    for _, value in aws_info.iterrows():
        start = datetime.now()
        urls = [f'https://www.weather.go.kr/cgi-bin/aws/nph-aws_txt_min_cal_test?{dt}&0&MINDB_01M&{value["지역번호"]}&m&M'
                for
                dt in date_list]

        logger.info(f'{value["지역명"]} 크롤링 시작')

        with Parallel(n_jobs=-1) as parallel:
            result = parallel(delayed(get_result)(url, dt) for url, dt in zip(urls, date_list))

        dataframe = pd.concat(result, ignore_index=True)
        dataframe['dt'] = pd.to_datetime(dataframe['dt'])
        dataframe.set_index('dt', inplace=True)
        dataframe.sort_index(inplace=True)
        dataframe = dataframe.loc[~dataframe.index.duplicated()]
        if not Path(args.output_path).exists():
            Path(args.output_path).mkdir(parents=True, exist_ok=True)

        dataframe.to_csv(f'./{args.output_path}/aws_{value["지역명"]}_{value["관측지점(m)"]}_{value["지역번호"]}.csv')
        end = datetime.now()

        log.info(f'걸린 시간: {end - start}')
        log.info(f'{value["지역명"]} 크롤링 종료')

    total_end = datetime.now()
    log.info(f'총 걸린 시간: {total_end - total_start}')


if __name__ == '__main__':
    log = logger()
    args = arg_setting()

    main(args)
