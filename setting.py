import logging
import argparse
from datetime import datetime


def arg_setting():
    parser = argparse.ArgumentParser()
    args = parser.parse_args("")

    args.start_date = '2021-10-05'
    args.end_date = datetime.now().strftime("%Y-%m-%d %H")
    args.output_path = './aws_output'

    return args


def logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # log를 파일에 출력
    file_handler = logging.FileHandler('aws_crawling_parallel.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def datadict():
    dict_ = {
        'dt': list(),
        'rain': list(),
        'rain15': list(),
        'rain60': list(),
        'rain3h': list(),
        'rain6h': list(),
        'rain12h': list(),
        'rainday': list(),
        'temp': list(),
        'wd1': list(),
        'wd1s': list(),
        'ws1': list(),
        'wd10': list(),
        'wd10s': list(),
        'ws10': list(),
        'hum': list(),
        'pha': list(),
    }

    return dict_
