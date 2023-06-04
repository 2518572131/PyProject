import base64
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models





if __name__ == "__main__":
    file_path = "./channel3.wav"
    cred = credential.Credential("AKIDDI9lbP1ReeR1OabQ2FH5f193j094nJci", "vb5NSKyOXaSAg1A9wWu42mKfppdKrHWY")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "asr.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = asr_client.AsrClient(cred, "", clientProfile)
    req = models.CreateRecTaskRequest()
    params = {
    "EngineModelType": "16k_en",
    "ChannelNum": 1,
    "ResTextFormat": 0,
    "SourceType": 0,
    "Url": "https://test-1312185535.cos.ap-chengdu.myqcloud.com/channel3.wav"
    }
    req.from_json_string(json.dumps(params))
    resp = client.CreateRecTask(req)
    print(resp.to_json_string())
    
