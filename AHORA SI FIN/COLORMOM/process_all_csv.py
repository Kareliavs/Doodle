import os
import numpy as np
import sys
from PIL import Image
from math import floor
import PIL.ImageOps
import json
import csv
#0-248
codes=['AF','AX','AL','DZ','AS','AD','AO','AI','AQ','AG','AR','AM','AW','AU','AT','AZ','BH','BS','BD','BB','BY','BE','BZ','BJ','BM','BT','BO','BQ','BA','BW','BV','BR','IO','BN','BG','BF','BI','KH','CM','CA','CV','KY','CF','TD','CL','CN','CX','CC','CO','KM','CG','CD','CK','CR','CI','HR','CU','CW','CY','CZ','DK','DJ','DM','DO','EC','EG','SV','GQ','ER','EE','ET','FK','FO','FJ','FI','FR','GF','PF','TF','GA','GM','GE','DE','GH','GI','GR','GL','GD','GP','GU','GT','GG','GN','GW','GY','HT','HM','VA','HN','HK','HU','IS','IN','ID','IR','IQ','IE','IM','IL','IT','JM','JP','JE','JO','KZ','KE','KI','KP','KR','KW','KG','LA','LV','LB','LS','LR','LY','LI','LT','LU','MO','MK','MG','MW','MY','MV','ML','MT','MH','MQ','MR','MU','YT','MX','FM','MD','MC','MN','ME','MS','MA','MZ','MM','NA','NR','NP','NL','NC','NZ','NI','NE','NG','NU','NF','MP','NO','OM','PK','PW','PS','PA','PG','PY','PE','PH','PN','PL','PT','PR','QA','RE','RO','RU','RW','BL','SH','KN','LC','MF','PM','VC','WS','SM','ST','SA','SN','RS','SC','SL','SG','SX','SK','SI','SB','SO','ZA','GS','SS','ES','LK','SD','SR','SJ','SZ','SE','CH','SY','TW','TJ','TZ','TH','TL','TG','TK','TO','TT','TN','TR','TM','TC','TV','UG','UA','AE','GB','US','UM','UY','UZ','VU','VE','VN','VG','VI','WF','EH','YE','ZM','ZW','ZZ']

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

number_images = 1000; # Number of images in each category
npy_dir = './raw/'
out_dir = './out/'
npy_files = [f for f in os.listdir(npy_dir) if os.path.isfile(os.path.join(npy_dir, f))]
print(npy_files)

categories = []

for x in npy_files:
	category_split = x.split('.')
	category = category_split[0].title()
	categories.append(category)
	
print(categories)

for y in categories:
	if not os.path.exists(os.path.join(out_dir, y)):
		os.makedirs(os.path.join(out_dir, y))

index_cat = 0		
for z in npy_files:
	print('Processing file', z)
	images = np.load(os.path.join(npy_dir, z))
	otro=z.split(".")
	otro="./raw/nd/"+otro[0]+".ndjson"
	f = open(otro)
	xa = json.load(f)
	f = csv.writer(open("Airplane.csv", "w"))
	f.writerow(["word", "countrycode","year","month","day","hour","minute","second","recognized","c1","c2","c3","c4","c5","c6","c7","c8","c9"])
	print('Saving in', categories[index_cat])
	number_imgs = range(0, number_images, 1)
	for a in number_imgs:
		print('Processing Image', a+1)
		file_name = '%s.png' % (a+1)
		file_path = os.path.join(out_dir, categories[index_cat], file_name)
		img = images[a].reshape(28,28)
		f_img = Image.fromarray(img)
		inverted_image = PIL.ImageOps.invert(f_img)
		img2 = inverted_image.convert("RGBA")
		datas = img2.getdata()
		newData = []
		i=0
		c1=c2=c3=c4=c5=c6=c7=c8=c9=0	
		for item in datas:
			#print(i%28+1,floor(i/28+1))
			x=i%28+1
			y=floor(i/28+1)
			if item[0] == 255 and item[1] == 255 and item[2] == 255:
				newData.append((255, 255, 255, 0)) #transparentes
			else:
				#newData.append((0,0,0,255))
				if x<=9 and y<=9: 
					c1=c1+1
				elif x>9 and x<=18 and y<=9: 
					c2=c2+1
				elif x>18 and y<=9: 
					c3=c3+1         ######Cuadrantes superiores
				elif x<=9 and y>9 and y<=18: 
					c4=c4+1
				elif x>9 and x<=18 and y>9 and y<=18: 
					c5=c5+1
				elif x>18 and y>9 and y<=18: 
					c6=c6+1
				elif x<=9 and y>18: 
					c7=c7+1
				elif x>9 and x<=18 and y>18: 
					c8=c8+1
				else: 
					c9=c9+1
				newData.append(item)				
			i=i+1	

		print(c1, c2, c3, c4, c5, c6, c7, c8, c9)
		palabra=categoria.index(xa[a]["word"])
		pais=codes.index(xa[a]["countrycode"])
		partes =xa[a]["timestamp"].split(" ") 
		fecha=partes[0].split("-") 
		horacomp=partes[1].split(":")
		anho=fecha[0]
		mes=fecha[1]
		dia=fecha[2]
		hora=horacomp[0]
		minuto=horacomp[1]
		segundo=floor(float(horacomp[2]))
		reconocido=booleano.index(str(xa[a]["recognized"]))
		f.writerow([palabra,pais,anho,mes,dia,hora,minuto,segundo,reconocido,c1, c2, c3, c4, c5, c6, c7, c8, c9])

		#img2.putdata(newData)
		#img2.save(file_path, 'PNG')
	index_cat = index_cat + 1
