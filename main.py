
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/bitch_hitler", methods=['GET'])
def get_instagram_info():
    # احصل على اسم المستخدم من الطلب
    username = request.args.get('username')
    
    if not username:
        return jsonify({"error": "يجب توفير اسم المستخدم في الطلب"})
    
    url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
    
    # قم بإرسال طلب إلى Instagram API باستخدام الرؤوس المحددة في الطلب السابق
    headers = {
        "Accept": "*/*",
        "Accept-Language": "ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "ig_did=2BF40B41-E798-41BD-80FC-BDFAC86D17DF; ig_nrcb=1; datr=3-TcZJtzPpzOObTVJNV-BNA0; mid=ZNzk4QABAAE_qtUgAsACc_0p8Mah; ds_user_id=61324243464; csrftoken=6msft5Wjywgklg1Wz8S3vaiCYupjFNki",
        "Dpr": "3",
        "Referer": "https://www.instagram.com/ibrahimm.aliraqi/",
        "Sec-Ch-Prefers-Color-Scheme": "light",
        "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
        "Sec-Ch-Ua-Full-Version-List": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.61\"",
        "Sec-Ch-Ua-Mobile": "?1",
        "Sec-Ch-Ua-Model": "\"JKM-LX1\"",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Sec-Ch-Ua-Platform-Version": "\"9.0.0\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        "Viewport-Width": "360",
        "X-Asbd-Id": "129477",
        "X-Csrftoken": "6msft5Wjywgklg1Wz8S3vaiCYupjFNki",
        "X-Ig-App-Id": "1217981644879628",
        "X-Ig-Www-Claim": "0",
        "X-Requested-With": "XMLHttpRequest"
    }
    try:
        req = requests.get(url, headers=headers).json()
        bio = req["data"]["user"]["biography"]
        followers = req["data"]["user"]["edge_followed_by"]["count"]
        following = req["data"]["user"]["edge_follow"]["count"]
        fullname = req["data"]["user"]["full_name"]
        idd = req["data"]["user"]["id"]
        username = req["data"]["user"]["username"]
        
        info = {
            "USERNAME": username,
            "FULL NAME": fullname,
            "FOLLOWERS": followers,
            "FOLLOWING": following,
            "BIO": bioo,
            "ID": idd,
            "PROGRAMMER": "IBRAHIM",
            "TELEGRAM":"@B_XXBX"
        }
        return jsonify(info)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
