import pymysql,logging,cv2
from configparser import ConfigParser

logging.basicConfig(level=logging.INFO, filename='log/log.txt', format='%(asctime)s - %(levelname)s - %(message)s')

# mysql config from ./database.cfg
config = ConfigParser()
config.read('database.cfg', encoding='UTF-8')
mysql_host = config.get('DEFAULT', 'mysql_host')
mysql_user = config.get('DEFAULT', 'mysql_user')
mysql_passwd = config.get('DEFAULT', 'mysql_passwd')
mysql_database = config.get('DEFAULT', 'mysql_database')
mysql_table = config.get('DEFAULT', 'mysql_table')
mysql_port = config.get('DEFAULT', 'mysql_port')


from fastapi import FastAPI, File, UploadFile, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
app.mount("/output", StaticFiles(directory="./output"), name="static")
base_url = 'http://192.168.0.1:6699'
origins = [
    "http://localhost:8080",
    "http://localhost",
    "http://192.168.0.1",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message:": "Please Try"}


@app.post("/poseaction")
async def index(background_task: BackgroundTasks, videofile: UploadFile = File(...)):
    try:
        video_name = videofile.filename
        if video_name[-3:] in ['mp4', 'avi']:
            tmp_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, str(time.time()))) + str(video_name[-4:])
            tmp_save = './input/' + tmp_id
            F = await videofile.read()
            with open(tmp_save, 'wb') as f:
                f.write(F)
            try:
                background_task.add_task(infer,video_name)
                return {
                    "result_code": 200,  # 识别成功
                    "result_data":
                        {
                            'doc': 'Use http://xxx.xxx.xxx.xxx:port/poseaction/video_id Get this action result.',
                            'video_id': tmp_id[:-4] + '-h264.mp4',
                        }}
            except Exception as e:
                logging.info(str(e))
                return {
                    "result_code": 201,  # 识别失败，视频无相应行为
                    "result_data": {}
                }
        else:
            return {"result_code": 202, "result_data": {}}  # 识别失败，视频格式错误

    except Exception as e:
        print(str(e))
        logging.info(str(e))
        return {
            "result_code": 203,  # 识别失败，其他错误
            "result_data": {}
        }


def infer(video_name):
    try:
        db = pymysql.connect(host=mysql_host,
                             user=mysql_user,
                             passwd=mysql_passwd,
                             database=mysql_database
                             )
        cursor = db.cursor()
        sql_insert_pre = f"INSERT INTO {mysql_table} VALUES ('{video_name}')"
        cursor.execute(sql_insert_pre)
        db.commit()  # 事务提交
        cursor.close()
        db.close()
    except Exception as e:
        print('事务处理失败', e)
        logging.debug(str(e) + 'this erro in DB.')


@app.get("/poseaction/{video_name}")
def inference(video_name):
    try:
        db = pymysql.connect(host=mysql_host,
                             user=mysql_user,
                             passwd=mysql_passwd,
                             database=mysql_database
                             )
        cursor = db.cursor()
        sql = f"CREATE DATABASE IF NOT EXISTS {mysql_database}"
        cursor.execute(sql)
        sql_text = f"SELECT * FROM {mysql_table} WHERE video_name='{video_name}';"
        cursor.execute(sql_text)
        results = cursor.fetchone()
        cursor.close()
        db.close()
        return {
            "result_code": 200,
            "result_data":
                {
                    "video_name": results[0],
                }}
    except:
        return {
            'message': 'Wait a moment please'
        }


if __name__ == '__main__':
    # 注意这里每次修改文件名需要修改
    uvicorn.run(app="app-fastapi:app", host="0.0.0.0", port=6000, reload=True, debug=True)
