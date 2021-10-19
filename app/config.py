class CompetitionConfig:
    NAME = 'Lab #'
    
    # UTC TIME (YYYY/MM/DD HH:MM:SS)
    OPEN_TIME = '2019/12/02 11:25:00'
    CLOSE_TIME = '2022/12/02 11:27:00'
    TERMINATE_TIME = '2023/12/02 11:27:00'

    # USERS with special behaviours
    ADMIN_USER_ID = "prof"
    BASELINE_USER_ID = "baseline"

    UPLOAD_FOLDER = './uploads'  # Where to store submissions
    DUMP_FOLDER = './dumps'  # Where to store DB dumps with scores

    TEST_FILE_PATH = './static/test_solution/test_solution.csv'  # './static/test_solution/eval_solution.csv'
    MAX_FILE_SIZE = 32 * 1024 * 1024  # limit upload file size to 32MB
    API_FILE = 'mappings.dummy.json'  # API mappings
    DB_FILE = 'sqlite:///test.db'
    TIME_BETWEEN_SUBMISSIONS = 5 * 60  # 5 minutes between submissions
    MAX_NUMBER_SUBMISSIONS = 100
