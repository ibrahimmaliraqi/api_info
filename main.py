from flask import Flask,jsonify,request

from fake_useragent import UserAgent
import secrets
import requests
import re
import random
Session = requests.Session()
UserAgent = UserAgent()
MOZ = UserAgent.random
Cookie = secrets.token_hex(16)*2
ibrahim = Flask(__name__)
@ibrahim.route("/ibrahimm")
def gmail():
    email = request.args.get("email")
    if not email:
        return jsonify({"code":"you must put an email."})
    
    Session.Link_1 = ('https://accounts.google.com/_/signup/validatepersonaldetails?hl=ar&_reqid=47268&rt=j')
    Session.Headers_1 = ({
    'Host': 'accounts.google.com',
    'content-length': '1385', 
    'pragma': 'no-cache', 
    'cache-control': 'no-cache',
    'x-same-domain': '1',
    'google-accounts-xsrf': '1',
    'user-agent':MOZ,
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'accept': '*/*', 
    'origin': 'https://accounts.google.com', 
    'x-requested-with': 'com.saschaha.browses', 
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors', 
    'sec-fetch-dest': 'empty', 
    'referer': 'https://accounts.google.com/signup/v2/createaccount?cc=IQ&continue=https%3A%2F%2Fwww.google.com%2F%3Fgws_rd%3Dssl&dsh=S1879162115%3A1695507206795332&flowEntry=SignUp&flowName=GlifWebSignIn&hl=ar&ifkv=AYZoVheKR-Bt7b1NLOaIJh0Ah3QDHWymXlDkMiV8YajWsy6_cU2BVSCMZqa9R3n6gTTIzAOoUzHoCA&theme=glif',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': Cookie,
    })
    #Session.headers = ({'User-Agent':MOZ})
    #response = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=Session.headers)
    #Session.ae = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', response.text).group(2)
    AE = ['AEThLly0I1DBnCp9LUsrxnoP6Y4mJMMn0-YjxHMK6VbGfHcRJrARZpSuLifeVakOXL8FFeY0-wKYJnuGZAf9P1J9IjnFg_2Wjl-Yy_MN8zMn31FX7w9hmZtwd0V7iLkyQAECk6LY8C4Rz2QJPICKqFaOHUAtM9fk4Z7VQHHmNIXYujz9DfKlOvyCeYAbY4VwTATBncNdvjwW','AEThLlyo3Vgk0D4Zat7DaHNmQQ9lHWQVD_tDtmXoU6UJaXRjr_pidJBt0CkqgdfHm_2cSvvGtFYNHstpXcbDpuGx0-eWATRRmpa0FstcNrYtrGXLaIOiy8kJDptzYHAIoWiIdrJVG5MfUSPgmwvZGZqJLZnFZ2mc0Rqlpc-DaViiLEuLUSMCr5S2xC5cO_s0qfXJMHWLefn6','AEThLlxjb6VZLBcamppy-ooIXUThHZ_tbh4ugPT8zhAN-izrmeregIPHlM3TB_nHCMudQgK9EsZigpKyJoFsfcvR7xEqCNxPV8-l35_oSvkBrq1MKEQdUXrP9FjAeewMHSQu7VxnrJC5M43OkM3rLqKf_ByDzbrzsx6rZJK1brmPm7pkbC9IBFwmw7pMf-Ph0GlPjgbjtji6','AEThLlwh-E1wuMV1pB8J1l0OnJZmRsUotC7qqHY76ek89SvwvHNHfgxvquXZddTe9HamKXUrk7qp2HnKkQxTu4FGtrV8nWLbz8yn2JYUbt1IS_ORGY49A1i0-pmN61X3EEiZDJh6hrniNvRFckp-HuUClnU2OJL8eNQTqowV-cphrDZTy3KmqJZdiDrnUqk2RN1RTSonKDhg','AEThLlxAwTiEzh36yhDH9Qd3xZ9OrAA6Hjaiue1Ys419aLUg3omXfWnLKlAtZ5oYk0LIn1uIOiqjYX8QZWntarWZ4Pam4NqHXNwjStNkJ7-DscTvMPDi8KC-iKlR0qPRf271J8F3INui-UEq4zK3d3JMz7ZY6iZykUaHePtPLt8YiYlIlyGUZnYFon1OIi2Xcvu6q8DP8pA0','AEThLlxi0DYZgq6uBCOmqb0LsoiEuJv85B7_Nkfa7_qcLIKwHXooWuGQnOVH5Cl6HG2N73nh5wjQ_ThXydKRkKD2JazSQrHjGMB4RVrWPXHQk8Ud7Ffwr_wRYlMfUi0DImt6Jugt2o42OR7gfJuRZG5nqVeAJscAfklSEOYC5QQLRfTIBOWcx9s_nmI5ZmbYd37p13Qfpsqo','AEThLlyzmtFNmxPoYeE7FzO3R8P7Bpe8hPij5W8KLtBnZZQddPeE5mNCmTWkFA2oBh4De3c8-sdByeT8OuIfUpcWP7SxAW793zKmDwkSO9EKtKFRd6sDlgO1vR4kt-T0WkRU5r8tbLwZ1dcDfqx2nV6apqEZp6uwjCrqdc4SNpmTNfQ43slpqdjB6G-qUUzSGqojhEeXKAbO','AEThLlxLlkt95I7aO-mIG6Mrq3joVIQyH5i1q0WbfHOj0f15wz_nNoiDEXljK05HvgEhrBVZQVWXEGMPZLq_fflDgC2C0COTThvCIhe0J-cRWPp4YEptwyGisGkbuWt8b9BDbS8CjsCNh4UR0bmCNajnyEygJ4JKN-uq_0rPhh4g6prlCNWycYcyWnPiDogL0mU5iqsdi8aE','AEThLlwQUVhqYoe9t6zx8CbVu35U6Sq3Knzgh4r1rHN97ML_-1TH6Lxzmkb8oe2R-C_meG2d4FjzftTSxmyB-PtSHJJt1658IkZ4OAiS7-fZTWvUiKGlw0nxM_-d7iTuYGvoYz9Rla1IemXkw4kJsgYh49ifVuNCVJ47ErSxuJYdnkZoT1uatGyU7ueehtF4qm8diL7GDyz0','AEThLlxT5sPsM8NTquQiNO7d79bVL7OsHzJ77romKv-dQjhbgHTvI0m6UMMShylAG0xCxAPK5NJ0arbZS4D2dt64oqrDq-C6cdJd7063lttUOFo8SVnqGcWKGl9MBr65dcp3snJwH559saKJndkbJLIouMqWxocqVRgXFUtQZ-rq6hF6ftajo5uktskG3Gi4SvOakdQOk9JY','AEThLlynUsN4LSra3fsjPuIFGeWo1KbjlG3kxK9ZuncwNKfwhEOAkBfyQaSKRNumZZ07iKyYHNKLvo3BRyxdVRb6tb84y1QTHpfqN2EMdX2zPA3yeN3Hzcc--aQvsXcjhM69BlpcBGBK31KugN_5xdWk9EpCyIPUi-p8qB6h4Zta_JFol7M4f6ohDu6i98SZPuoWpSFCYccx','AEThLlw8yIbTWjAs7V-iQSZIFH2OB6JMDD9235xcKArZRTC46yf7wR3d6eQWsIFSPNajIWc7jtoRZ5598DAYsPlpEKzSvz3YA2KuD6nSUTJmPQaY2o1g7KsHMFgNQUkeEM0TYU5dEb_xALXA4nQ8SkcBuLuvUKq7f7G1ZFBiQbkvGsfaClOvCBpr9EcScDNSctrAEQOaTZVR','AEThLlzbhtzo5KJE36Pit8Vf1akp31bKPNWzvA5Ulyj_cx_c7I5jzNy9zxy9nOcDNLG42sj5SFvqDo5F97CqqECcmHyRNw-4njoNBpd_IEsVeNVAxF6ELB5IvVscO7lTbIWB7OxFRm9i0FX6g94RrXhFy8-DVIHuz_GQa6EQqmWO0l5N76h3zblJo4YsU4dTSgm_1IobGBz_','AEThLlwDbTL-kNfH6qThSsrtJ0xsThwozD2wduN2xiXWmjviryrxyVI5cA79KvYI81tNJvWZSxwK-R-EWNkIbuQ7UgPjD_u8GKPec_POR-QsS5tcDAGIa3udN-yPua2y-SAP-7xF6goiCqGsP4pA6HTzD73OVQYpiQm30NTUjY_aoc5y196tNr8nHxkUVPtQ4Y9BHEQIfPSr','AEThLlwEWw8MAIUG3Jxkfd214sqrKD3DeIho62O-otf0UNiWP7qRGDh-Fl2SDUuj50zeBj18o8wV145uGplU8bJrd_Yk5dePifFemoslhtI9ETQL5hFwf8fw1whz5NrB1fBWDJ1ZAnzftOJSEFDaH7fAjtqiOySSltfwI-fWoeBit6edtd6VpuHgKJtRvfgAXiNrbhqLfwQ5','AEThLlzfVvaKJOGrHHGJMWLy_eb7AsAQIpgEODpUc_cPdDk7AjNKiLTMSGAywJ0D1b8S9CdNeN9bhgyWZt2TDJwXdzmfSd_4AHm2g9u0WKKl0HX1syZcGsAH4378qwHvP9YHqL--GAwd3rAIxXcGyVb2okrxlND--WIxTEYJrIjxyn8PAQWU1uJFgzCmjAutxcRxSUUXB9tH','AEThLlx2jfTzP_3LPVdHYoSCXM5abyRIyKEJqJaDPCRSOPmyGewD88YjHjZFinbm8kcosdrRbQDZpD4FjKYcCWrbZcRLPawlKuxByCEoQ7R9x9-L0jPxei9gErjk4vLKD3kYFNJATfOaF8u47uzrE_4TYoe5IxjoVbGHRw-j8BlrVr8THJ1od0egSebUejO2e9DTFYCXAQpa','AEThLlxmUGVNWSsaQwpGYNSxrtHbh82YBAkkKrTLyANu9HgsnBA1zRhy8LGE3urHZ1fKfG8m2PLbIe5-d2ZUDp0PrKGvs_d2xUSoq3y2CfXLfsc2HXjktMOXPVS11kVAPjaURee1GcRjZ_jeVs3zl1KlUvXTrPCG-zE9HswSshOJcpf161dOvqNpFrbKqlttsLQ92HArNggd','AEThLlwDefuiIkP7Io1Sy_laaB_0U0LB-sxFhUqx-bNXaGaNkbhpT4jDxywESDPqxDmIMXBaX8VBZu7ttooHVb-Rv4wX_aY6lil2bSOGth13c7iaS9DPnt_OyyJ7FuqxnVLANC_v_qwiMj29nNFwisQdy40tdaGTKWwfAtvscB2SMZXyGulOnMGJCa2aQN8lV39hE2pIAcMN','AEThLly-Fxm99IEZUbawxhXqXz9xf7LdHpJleBy8WsUt9iHNnbsP9WW-vxfguksO7NqdY2uOczi4BwJ11w5VKzv4RirSfuxTw4iy2mEUC9rZI9ak4wlmAKVjIF9xaRMJOEfBXdXqtcPvm40xTk5cVk1WD4wrHMaPXTxTcWeJWpHGfTI6-MW57P86ZNNHDChBGOzypCn9AnoT','AEThLly7DQ0QMLol8Go7RMmffBTqMwJyOoS5qXIBK96nCmX5y8pcZ5FfplcUywe6qgyWK056wyNw0YCReswR6PdvgZVJlld6dXDMfvVCahgHSDyjgwNYMXYCPalJoY07QZSX624-RRvqBQbptULkjqL60hHMErAjG4OdHXXwxQFRnWJ6lqVOCScgaOFiSmw83EG6lp-9krXW','AEThLlyj7LgrAT27zc6BnP5cEO7O3ybTuJ_dNW46cjgKN6ufS21_CpwUZpttlBAW0WJl5nTWkS6oGyTwm8g-64p4k27yKWvhjsToyc6_ow75CBPnTWxSJgQdbXNPLDnV6VUY6fErj_hHtp0ZfCwPN1AYSQg4GZqkzvYnzqSDt2LAgetOnrMNKT-l195XavQ7Y8MQzx0m_Ux3']
    AE_1 = random.choice(AE)
    Session.Data_1 = ({
    'continue':'https://www.google.com/?gws_rd=ssl',
    'dsh':'S1879162115:1695507206795332',
    'flowEntry':'ServiceLogin',
    'hl':'ar',
    'ifkv':'AYZoVheKR-Bt7b1NLOaIJh0Ah3QDHWymXlDkMiV8YajWsy6_cU2BVSCMZqa9R3n6gTTIzAOoUzHoCA',
    'theme':'glif',
    'f.req':f'["{AE_1}",null,null,null,null,0,0,"Jwjww","Jwjww","web-glif-signup",0,null,1,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,null,[]],1]',
    'azt':'AFoagUWmxrkhiDP8ysVpv_gcrkp9LhuU_g:1695722846394',
    'cookiesDisabled':'false',
    'deviceinfo':'[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,0,null,0,2,"",null,null,0,0]',
    'gmscoreversion':'undefined',
    'flowName':'GlifWebSignIn',
    })
    
    Session.Response_1 = requests.post(Session.Link_1,headers=Session.Headers_1,data=Session.Data_1).text
    
    TL_1 = Session.Response_1.split('["gf.ttu",null,"')[1].split('"')[0]
    
    Session.Link_3 = (f'https://accounts.google.com/_/signup/usernameavailability?&_reqid=402236&rt=j')
    
    Session.Headers_3 = ({
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'ar,en-US;q=0.9,en;q=0.8,pt;q=0.7',
    'Content-Length':'1308',
    'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
    'Cookie':Cookie,
    'Google-Accounts-Xsrf':'1',
    'Origin':'https://accounts.google.com',
    'Referer':'https://accounts.google.com/signup/v2/emailsignup?cc=IQ&continue=https%3A%2F%2Fmyaccount.google.com%2F&dsh=S2047335643%3A1695764186961798&flowEntry=SignUp&flowName=GlifWebSignIn&hl=ar&service=accountsettings&theme=glif&authuser=0&TL=AJeL0C4oEc2sC6AHE7AI8m4pSaKfhzUws8_secODqTuLt86dQ57RhZSPU6vT9XJw',
    'Sec-Ch-Ua':'"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Sec-Ch-Ua-Arch':'"x86"',
    'Sec-Ch-Ua-Bitness':'"64"',
    'Sec-Ch-Ua-Full-Version':'"117.0.5938.92"',
    'Sec-Ch-Ua-Full-Version-List':'"Google Chrome";v="117.0.5938.92", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.92"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Model':'""',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Ch-Ua-Platform-Version':'"10.0.0"',
    'Sec-Ch-Ua-Wow64':'?0',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':MOZ,
    'X-Chrome-Id-Consistency-Request':'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=b20ba583-8cad-46a7-80ea-88e6755866ad,sync_account_id=105342098533404169783,signin_mode=all_accounts,signout_mode=show_confirmation',
    'X-Client-Data':'CIe2yQEIpbbJAQipncoBCMzfygEIkqHLAQiFoM0BCI2yzQEI3L3NAQjfxM0BCOnFzQEIucrNAQi90c0BCIrTzQEItdbNAQj5wNQVGPXJzQE=',
    'X-Same-Domain':'1'
    })
    
    Session.Data_3 = ({
    'continue': 'https://myaccount.google.com/',
    'dsh': 'S2047335643:1695764186961798',
    'flowEntry': 'AddSession',
    'hl': 'ar',
    'service': 'accountsettings',
    'theme': 'glif',
    'f.req': f'["TL:{TL_1}","{email}",0,0,0,null,0,19744]',
    'at': 'AFoagUWOnIrBJBckkFUnTamL6_WLmffsvw:1695764210486',
    'azt': 'AFoagUV9HJdcEVT2k7IPQ0i8HiVi6O-Sdg:1695764210486',
    'cookiesDisabled': 'false',
    'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"b20ba583-8cad-46a7-80ea-88e6755866ad",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,2]',
    'gmscoreversion': 'undefined',
    'flowName': 'GlifWebSignIn',
    })
    Session.Response_3 = requests.post(Session.Link_3,headers=Session.Headers_3,data=Session.Data_3).text
    
    if ('"gf.uar",1') in Session.Response_3:
        return jsonify({"code":"true"})
    else:
        return jsonify({"code":"false"})
ibrahim.run(debug=True)       
        
