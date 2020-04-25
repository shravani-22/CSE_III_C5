from gtts import gTTS
import playsound
import mysql.connector
import time
import speech_recognition as sr

mydb = mysql.connector.connect(host="localhost",user="root",passwd="{NewPassword}",
                               auth_plugin="mysql_native_password",database="griet_college")

if(mydb):
    #print("successfully  connected to DataBase")
    print('wake up the assistant and then ask your question')
    print("wakeup words: 'hello tech','hello champion','hello assistant'")

else:
    print("DataBase Connection Unsuccessful")
cus = mydb.cursor()

def recordAudio():
    r = sr.Recognizer()
    print("Speak..")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,timeout=8)
    sentence=''
    try:
        sentence = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("unknown value error")
    except sr.RequestError:
        print("request error")
    return sentence

def response(mytext):
    language = 'en'
    output = gTTS(text=mytext, lang=language, slow=False)
    output.save("output.mp3")
    playsound.playsound("output.mp3")

def wakecall(text):
    text = text.lower()
    wake_words = ['hello tech','hello champion','hello assistant']
    text = text.lower()
    for phrase in wake_words:
        if phrase in text:
            return True
    return False

flag=1
time.sleep(3)
text=recordAudio()
text = text.lower()
print("You said: ", text)

if wakecall(text):


    if 'history' in text and ('college' in text or 'griet' in text):
        cus.execute("select info from college where about='History'")

    elif 'vision' in text and ('college' in text or 'griet' in text):
        cus.execute("select info from college where about='Vision'")

    elif 'mission' in text and ('college' in text or 'griet' in text):
        cus.execute("select info from college where about='Mission'")

    elif ('quality policies' in text or 'quality policy' in text)  and ('college' in text or 'griet' in text):
        cus.execute("select info from college where about='QualityPolicy'")

    elif ('strategies' in text or 'strategy' in text) and ('college' in text or 'griet' in text):
        cus.execute("select info from college where about='Strategies'")

    elif 'core values' in text and ('college' in text or 'griet' in text):
        cus.execute("select info from college where about='CoreValues'")

    elif 'student events' in text and ('college' in text or 'griet' in text):
        cus.execute("select info from college where about='StudentEvents'")

    elif 'special days' in text and ('college' in text or 'griet' in text):
        cus.execute("select info from college where about='SpecialDays'")

    elif 'chairman' in text or 'chairperson' in text and ('about' not in text and 'qualifications' not in text):
        cus.execute("select person_name from people where position='Chairman'")

    elif 'director' in text and ('about' not in text and 'qualifications' not in text):
        cus.execute("select person_name from people where position='Director'")

    elif 'principal' in text and ('about' not in text and 'qualifications' not in text):
        cus.execute("select person_name from people where position='Principal'")

    elif 'vp' in text or 'vice president' in text and ('about' not in text and 'qualifications' not in text):
        cus.execute("select person_name from people where position='VicePresident'")

    elif 'about' in text and ('chairman' in text or 'ganga' in text):
        cus.execute("select about from people where position='Chairman'")

    elif 'about' in text and ('director' in text or 'jandhyala' in text or 'jandiala' in text or 'murthy' in text):
        cus.execute("select about from people where position='Director'")

    elif 'about' in text and ('principal' in text or 'praveen' in text):
        cus.execute("select about from people where position='Principal'")

    elif 'about' in text and ('vice president' in text or 'ranga' in text or 'vp' in text):
        cus.execute("select about from people where position='VicePresident'")

    elif (('physics' in text) and ('name' in text or 'who is' in text)):
        print("physics")
        cus.execute("select chairperson_name from bos where programme='physics' ")

    elif (('computer' in text or 'cse' in text) and ('name' in text or 'who is' in text)):
        print("computer")
        cus.execute("select chairperson_name from bos where programme='cse' ")

    elif ('basic sciences' in text) and ('name' in text or 'who is' in text):
        cus.execute("select chairperson_name from bos where programme='bsh' ")

    elif ('chemistry' in text) and ('name' in text or 'who is' in text):
        cus.execute("select chairperson_name from bos where programme='chemistry' ")

    elif ('civil' in text) and ('name' in text or 'who is' in text):
        cus.execute("select chairperson_name from bos where programme='civil' ")

    elif ('ece' in text or 'communication' in text or 'electronics' in text) and 'electrical' not in text and ('name' in text or 'who is' in text):
        cus.execute("select chairperson_name from bos where programme='ece' ")

    elif ('eee' in text or 'triple' in text or 'electrical' in text) and ('name' in text or 'who is' in text):
        cus.execute("select chairperson_name from bos where programme='eee' ")

    elif ('english' in text) and ('name' in text or 'who is' in text):
        cus.execute("select chairperson_name from bos where programme='english'")

    elif ('humanities' in text) and ('name' in text or 'who is' in text):
        cus.execute("select chairperson_name from bos where programme='humanities' ")

    elif ('information technology' in text or 'it' in text) and ('name' in text or 'who is' in text):
        cus.execute("select chairperson_name from bos where programme='it'")

    elif ('mathematics' in text or 'maths' in text) and ('name' in text or 'who is' in text):
        cus.execute("select chairperson_name from bos where programme='mathematics' ")

    elif ('mechanical' in text) and ('name' in text or 'who is' in text):
        cus.execute("select chairperson_name from bos where programme='me' ")

    elif ('basic sciences' in text or 'srinivasa' in text) and 'qualifications' in text:
        cus.execute("select qualifications from bos where programme='bsh'")

    elif ('chemistry' in text or 'venkateshwara' in text or 'venkateshvara' in text) and 'qualifications' in text:
        cus.execute("select qualifications from bos where programme='chemistry'")

    elif ('civil' in text or 'mallikarjuna' in text) and 'qualifications' in text:
        cus.execute("select qualifications from bos where programme='civil'")

    elif ('computer science' in text or 'madhavi' in text) and 'qualifications' in text:
        cus.execute("select qualifications from bos where programme='cse'")

    elif ('communication' in text or 'swetha' in text or 'electronics' in text) and 'qualifications' in text and 'electrical' not in text:
        cus.execute("select qualifications from bos where programme='ece'")

    elif ('electrical' in text or 'sridevi' in text) and 'qualifications' in text:
        cus.execute("select qualifications from bos where programme='eee'")

    elif ('english' in text or 'lakshmi prasanna' in text) and 'qualifications' in text:
        cus.execute("select qualifications from bos where programme='english'")

    elif ('humanities' in text or 'indira' in text) and 'qualifications' in text and 'basic' not in text:
        cus.execute("select qualifications from bos where programme='humanities'")

    elif ('information' in text or 'prasanna lakshmi' in text) and 'qualifications' in text:
        cus.execute("select qualifications from bos where programme='it'")

    elif ('mathematics' in text or 'rama murthy' in text or 'maths' in text) and 'qualifications' in text:
        cus.execute("select qualifications from bos where programme='mathematics'")

    elif ('mechanical' in text or 'sateesh' in text) and 'qualifications' in text:
        cus.execute("select qualifications from bos where programme='mechanical'")

    elif ('physics' in text or 'vagdevi' in text or 'cs' in text) and 'qualifications' in text:
        cus.execute("select qualifications from bos where programme='physics'")

    elif 'n b a' in text or 'nba' in text:
        cus.execute("select ranking from accreditations where accredited_by='nba'")
    elif 'naac' in text:
        cus.execute("select ranking from accreditations where accredited_by='naac'")
    elif 'n i r f' in text or 'nirf' in text:
        cus.execute("select ranking from accreditations where accredited_by='nirf'")
    elif 'u g c' in text or 'ugc' in text:
        print("ugc")
        cus.execute("select ranking from accreditations where accredited_by='ugc'")
    elif 'accreditations' in text or 'accreditation' in text or 'accredited' in text:
        cus.execute("select ranking from accreditations where accredited_by='all' ")

    elif 'block' in text and ('cse' in text or 'computer science' in text) and ('head' not in text or 'hod' not in text):
        cus.execute("select block_no from blocks where block_name='cse' ")
    elif 'block' in text and 'civil' in text and ('head' not in text or 'hod' not in text) :
        cus.execute("select block_no from blocks where block_name='civil' ")
    elif 'block' in text and ('ece' in text or 'electronics' in text and ('electrical' not in text)) and ('head' not in text or 'hod' not in text):
        cus.execute("select block_no from blocks where block_name='ece' ")
    elif 'block' in text and ('eee' in text or 'electrical' in text or 'triple' in text) and ('head' not in text or 'hod' not in text):
        cus.execute("select block_no from blocks where block_name='eee' ")
    elif 'block' in text and ( 'mechanical' in text) and ('head' not in text or 'hod' not in text):
        cus.execute("select block_no from blocks where block_name='mech' ")
    elif 'block' in text and ( 'information technology' in text) and ('head' not in text or 'hod' not in text):
        cus.execute("select block_no from blocks where block_name='it' ")
    elif 'block' in text and ( 'humanities' in text) and ('head' not in text or 'hod' not in text):
        cus.execute("select block_no from blocks where block_name='hs' ")
    elif 'block' in text and ('cse' in text or 'computer science' in text) and ('head' in text or 'hod' in text):
        cus.execute("select hod_room_no from blocks where block_name='cse' ")
    elif 'block' in text and 'civil' in text and ('head' in text or 'hod' in text) :
        cus.execute("select hod_room_no from blocks where block_name='civil' ")
    elif 'block' in text and ('ece' in text or 'electronics' in text and ('electrical' not in text)) and ('head' in text or 'hod' in text):
        cus.execute("select hod_room_no from blocks where block_name='ece' ")
    elif 'block' in text and ('eee' in text or 'electrical' in text or 'triple' in text) and ('head' in text or 'hod' in text):
        cus.execute("select hod_room_no from blocks where block_name='eee' ")
    elif 'block' in text and ( 'mechanical' in text) and ('head' in text or 'hod' in text):
        cus.execute("select hod_room_no from blocks where block_name='mech' ")
    elif 'block' in text and ( 'information technology' in text) and ('head' in text or 'hod' in text):
        cus.execute("select hod_room_no from blocks where block_name='it' ")
    elif 'block' in text and ( 'humanities' in text) and ('head' in text or 'hod' in text):
        cus.execute("select hod_room_no from blocks where block_name='hs' ")
    else:
        flag=0

else:
    print("invalid wakeup call..so repeat it again")
    exit()

mytext=""
for db in cus:
    mytext=''.join(db)
if flag==1:
    print("here is your response..")
    print(mytext)
    response(mytext)
else:
    print("Sorry..I didn't get you")
