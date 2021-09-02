# -*- coding: utf8 -*-
import requests 
from bs4 import BeautifulSoup

cookie = '__gads=ID=dda52e07a7202b63-227d3afe2fc600c2:T=1614588261:RT=1614588261:S=ALNI_MZXx40MBr7kQGg91eXAuwNDgCKXcg; htVD_2132_connect_is_bind=1; htVD_2132_nofavfid=1; htVD_2132_smile=1D1; KF4=SHK5uu; htVD_2132_atarget=1; htVD_2132_ignore_rate=1; htVD_2132_sid=0; htVD_2132_lastviewtime=1559381|1630485926; Hm_lvt_46d556462595ed05e05f009cdafff31a=1629443320,1630042810,1630485914,1630565917; htVD_2132_ttask=1559381|20210902; htVD_2132_saltkey=YOqY2mnH; htVD_2132_lastvisit=1630571915; htVD_2132_seccodecSGpt=49602.7f0fb7d09e297ed007; htVD_2132_ulastactivity=1630575520|0; htVD_2132_auth=e0f9CoED1f/udUdmf3pWqn/Wgc6mgxBskJ7IvUWIzMoZNjoSGa38AvLRR/eS/cIZJ5BYcExGxMcbk5JnM/CRTSckjt+P; htVD_2132_lip=119.164.213.114,1630575520; htVD_2132_seccodecS=49640.2f5e218dbdb8bb06eb; htVD_2132_visitedfid=8D10D66D16; htVD_2132_st_p=1559381|1630575597|414f956f0691a1e0091db5e87cf0151a; htVD_2132_viewid=tid_1504934; htVD_2132_home_diymode=1; htVD_2132_st_t=1559381|1630575944|c25f1c3d2892735d3bc0d2f9f7aa5c35; htVD_2132_forum_lastvisit=D_10_1630566958D_8_1630575944; htVD_2132_checkpm=1; htVD_2132_lastcheckfeed=1559381|1630576012; htVD_2132_checkfollow=1; htVD_2132_lastact=1630576023	home.php	spacecp; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1630576024'  # 配置你的cookie
sckey = 'SCT70915T3aQ61IMuFowhLPIMI517Dgpj' # 配置你的server酱SCKEY

def pushinfo(info,specific):
    headers={   
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'ContentType': 'text/html'
    }
    requests.session().get("https://sc.ftqq.com/"+sckey+".send?text=" + info + "&desp=" + specific,headers=headers)

def main(*args):
    headers={
        'Cookie': cookie,
        'ContentType':'text/html;charset=gbk'
    }
    requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=apply&id=2',headers=headers)
    a=requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=draw&id=2',headers=headers)
    b=BeautifulSoup(a.text,'html.parser')          
    c=b.find('div',id='messagetext').find('p').text

    if "您需要先登录才能继续本操作"  in c: 
        pushinfo("Cookie失效", c)
    elif "恭喜"  in c:
        pushinfo("吾爱破解签到成功",c)
    else:
        pushinfo("吾爱破解签到失败",c)
    print(c)


if __name__ == '__main__':
    main()
