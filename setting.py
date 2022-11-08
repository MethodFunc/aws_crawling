import logging
import argparse


def arg_setting():
    parser = argparse.ArgumentParser()
    args = parser.parse_args("")

    args.year = 2022
    args.month = 10
    args.day = 5
    args.hour = 1
    args.range_date = 395
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
