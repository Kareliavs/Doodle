import json
import csv
#0-248
codes=['AF','AX','AL','DZ','AS','AD','AO','AI','AQ','AG','AR','AM','AW','AU','AT','AZ','BH','BS','BD','BB','BY','BE','BZ','BJ','BM','BT','BO','BQ','BA','BW','BV','BR','IO','BN','BG','BF','BI','KH','CM','CA','CV','KY','CF','TD','CL','CN','CX','CC','CO','KM','CG','CD','CK','CR','CI','HR','CU','CW','CY','CZ','DK','DJ','DM','DO','EC','EG','SV','GQ','ER','EE','ET','FK','FO','FJ','FI','FR','GF','PF','TF','GA','GM','GE','DE','GH','GI','GR','GL','GD','GP','GU','GT','GG','GN','GW','GY','HT','HM','VA','HN','HK','HU','IS','IN','ID','IR','IQ','IE','IM','IL','IT','JM','JP','JE','JO','KZ','KE','KI','KP','KR','KW','KG','LA','LV','LB','LS','LR','LY','LI','LT','LU','MO','MK','MG','MW','MY','MV','ML','MT','MH','MQ','MR','MU','YT','MX','FM','MD','MC','MN','ME','MS','MA','MZ','MM','NA','NR','NP','NL','NC','NZ','NI','NE','NG','NU','NF','MP','NO','OM','PK','PW','PS','PA','PG','PY','PE','PH','PN','PL','PT','PR','QA','RE','RO','RU','RW','BL','SH','KN','LC','MF','PM','VC','WS','SM','ST','SA','SN','RS','SC','SL','SG','SX','SK','SI','SB','SO','ZA','GS','SS','ES','LK','SD','SR','SJ','SZ','SE','CH','SY','TW','TJ','TZ','TH','TL','TG','TK','TO','TT','TN','TR','TM','TC','TV','UG','UA','AE','GB','US','UM','UY','UZ','VU','VE','VN','VG','VI','WF','EH','YE','ZM','ZW']

categoria=['aircraft carrier','airplane','alarm clock','ambulance','angel','animal migration','ant','anvil','apple','arm','asparagus','axe','backpack','banana',
'bandage','barn','baseball','baseball bat','basket','basketball','bat','bathtub','beach','bear','beard','bed','bee','belt','bench','bicycle','binoculars','bird',
'birthday cake','blackberry','blueberry','book','boomerang','bottlecap','bowtie','bracelet','brain','bread','bridge','broccoli','broom','bucket','bulldozer','bus',
'bush','butterfly','cactus','cake','calculator','calendar','camel','camera','camouflage','campfire','candle','cannon','canoe','car','carrot','castle','cat','ceiling fan',
'cello','cell phone','chair','chandelier','church','circle','clarinet','clock','cloud','coffee cup','compass','computer','cookie','cooler','couch','cow','crab','crayon','crocodile',
'crown','cruise ship','cup','diamond','dishwasher','diving board','dog','dolphin','donut','door','dragon','dresser','drill','drums','duck','dumbbell','ear','elbow','elephant','envelope',
'eraser','eye','eyeglasses','face','fan','feather','fence','finger','fire hydrant','fireplace','firetruck','fish','flamingo','flashlight','flip flops','floor lamp','flower','flying saucer',
'foot','fork','frog','frying pan','garden','garden hose','giraffe','goatee','golf club','grapes','grass','guitar','hamburger','hammer','hand','harp','hat','headphones','hedgehog','helicopter',
'helmet','hexagon','hockey puck','hockey stick','horse','hospital','hot air balloon','hot dog','hot tub','hourglass','house','house plant','hurricane','ice cream','jacket','jail','kangaroo',
'key','keyboard','knee','knife','ladder','lantern','laptop','leaf','leg','light bulb','lighter','lighthouse','lightning','line','lion','lipstick','lobster','lollipop','mailbox','map','marker',
'matches','megaphone','mermaid','microphone','microwave','monkey','moon','mosquito','motorbike','mountain','mouse','moustache','mouth','mug','mushroom','nail','necklace','nose','ocean',
'octagon','octopus','onion','oven','owl','paintbrush','paint can','palm tree','panda','pants','paper clip','parachute','parrot','passport','peanut','pear','peas','pencil','penguin',
'piano','pickup truck','picture frame','pig','pillow','pineapple','pizza','pliers','police car','pond','pool','popsicle','postcard','potato','power outlet','purse','rabbit','raccoon',
'radio','rain','rainbow','rake','remote control','rhinoceros','rifle','river','roller coaster','rollerskates','sailboat','sandwich','saw','saxophone','school bus','scissors','scorpion',
'screwdriver','sea turtle','see saw','shark','sheep','shoe','shorts','shovel','sink','skateboard','skull','skyscraper','sleeping bag','smiley face','snail','snake','snorkel','snowflake',
'snowman','soccer ball','sock','speedboat','spider','spoon','spreadsheet','square','squiggle','squirrel','stairs','star','steak','stereo','stethoscope','stitches','stop sign','stove',
'strawberry','streetlight','string bean','submarine','suitcase','sun','swan','sweater','swing set','sword','syringe','table','teapot','teddy-bear','telephone','television','tennis racquet',
'tent','The Eiffel Tower','The Great Wall of China','The Mona Lisa','tiger','toaster','toe','toilet','tooth','toothbrush','toothpaste','tornado','tractor','traffic light','train','tree',
'triangle','trombone','truck','trumpet','t-shirt','umbrella','underwear','van','vase','violin','washing machine','watermelon','waterslide','whale','wheel','windmill','wine bottle','wine glass',
'wristwatch','yoga','zebra','zigzag']
booleano = ['False','True']
#print(codes.index('ZW'))

f = open('airplane2.ndjson')
#print(f)
x = json.load(f)
#print(x)
f = csv.writer(open("airplane2.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["word", "countrycode","year","month","day","hour","minute","second","recognized"])

for x in x:
    #print(x["word"])
    palabra=categoria.index(x["word"])
    pais=codes.index(x["countrycode"])

    partes =x["timestamp"].split(" ") 
    fecha=partes[0].split("-") 
    horacomp=partes[1].split(":") 
    ####################
    anho=fecha[0]
    mes=fecha[1]
    dia=fecha[2]
    hora=horacomp[0]
    minuto=horacomp[1]
    segundo=horacomp[2]

    reconocido=booleano.index(str(x["recognized"]))
    #print(fecha, hora)
    f.writerow([palabra,pais,anho,mes,dia,hora,minuto,segundo,reconocido])
