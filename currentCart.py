currCart = []
allNDC = [805253403611,805253311312,8052531545316,805253354111,754471585718,754471298816,805253313019,715244064595,805253389717,8052531318514,805253389519,805253310919,805253403710,805253300187,805253354517,8145270297513,687985263516,8052531321118,8052531514718,705108553600,814527302512,8145271611110,754471577911,8052531290117,8052531503910,805253337411,687985250110,8052531322412,8145270206812,814527316717,754471577119,8052531507314,754471584612,805253300293,8052531530817,687985265114,805253354418,805253300354,805253402812,805253131064,805253390812,805253375291,705108551408,687985220717,705108555505,814527200245,754471333517,705108804900,805253354715,8052530140116,805253357013,754471294313,805253026520,8052530147214,8052532451319,754471332015,754471331711,754471331216,805253331716,805253331518,754471292111,754471204312,754471284116,754471292715,8052531324614,805253401211,805253400610,805253400917,8052531317715,805253401013,754471277910,8052531342212,705108602513,754471295914,754471294016,754471293910,754471294214,514677092027,8052531135012,805253301658,754471202318,805253392014,8052530170328,754471197911,754471197928,815161001090,20916,21715,715244101009,715244111008,715244111107,754471121329,8052530055328,815165001652399,815165001652,754471181910,754471181927,754471181613,754471181620,754471182610,805253332317,7801,7818,7603,815165001362,805253311114,754471140115,754471140016,8052530185414,805253300026,705108321605,805253332515,754471198611,754471170112,754471170129,805253369214,805253369221,15820,15820,43908,43922,43304,43328,754471176626,754471171829,754471171010,754471171027,75447118751,715244013913,16421,16605,754471599012,754471329015,754471582212,8052530192511,8052531504818,805253406612,8052531508618,8052531513711,140000103711,8052531311515]
allPrice = [49.99, 59.99, 79.99, 239.99, 69.99, 79.99, 89.99, 69.99, 89.99, 79.99, 79.99, 89.99, 79.99, 59.99, 239.99, 69.99, 69.99, 79.99, 79.99, 219.99, 189.99, 99.99, 249.99, 199.99, 89.99, 79.99, 199.99, 79.99, 69.99, 59.99, 79.99, 79.99, 89.99, 89.99, 79.99, 89.99, 239.99, 79.99, 59.99, 99.99, 119.99, 239.99, 199.99, 89.99, 109.99, 149.99, 159.99, 249.99, 149.99, 129.99, 149.99, 159.99, 179.99, 129.99, 179.99, 79.99, 59.99, 35.99, 99.99, 49.99, 49.99, 39.99, 29.99, 29.99, 21.99, 29.99, 19.99, 19.99, 24.99, 19.99, 19.99, 14.99, 12.99, 39.99, 12.99, 12.99, 4.99, 17.99, 16.99, 15.99, 14.99, 15.99, 4.99, 1.49, 7.99, 1.49, 7.99, 7.99, 1.99, 34.99, 19.99, 2.99, 10.99, 1.99, 9.99, 0.99, 8.99, 0.99, 8.99, 2.49, 4.99, 1.99, 4.99, 1.99, 4.99, 19.99, 19.99, 19.99, 19.99, 14.99, 15.99, 5.99, 5.99, 1.99, 25.99, 1.99, 39.99, 2.49, 7.99, 0.50, 9.99, 0.79, 8.99, 0.99, 7.99, 1.99, 9.99, 1.99, 7.99, 9.99, 1.99, 34.99, 12.99, 89.99, 3.99, 189.99, 21.99, 49.99, 79.99, 399.99, 19.99]
allName =["Jurassic Raptor", "Polar Attack","American Riders","Party On America","Triple Feature","Shock and Awe ","Amazing","Gunfighters From Hell","Death Rider","One Bad Mother","Scorpion","Dr. Jekyll","Showboatin'","Evil Clown","Baby Boomer","Dark Night","Schizo","Grave Digger","Gorilla Warfare","Disco Ball","Red Giant","U.S.A","Maximum Insanity","One Bad Mother 3","Crazy Exciting On Steroids","Folds Of Honor","Whacky Tobacky","Widow Maker","Super Freak","Jim Dandy","Barely Legal","Sexy Rider","Rock N' Roll","Chasing Booty","Greeen"," Yin Yang","Placa Vintage King","Tank Girl","Rock Em' Sock Em'","Loyal To None","Skull Engine","Zippity Doo-Dah","Golden Peacock","Wicked Cool","Party Bus","Keeping It Real","Instant Party","Tank Busters","Growler","Excaliber","Excaliber Platinum","Shocker Shells 6","Goliath","Zues","The King Assortment","Sky Box","Wild Thing","Super Assortment","Power Wagon","Family Truckster","Dirty Dancing in The Sky","Sky Angel","Bullet Clusters","Pure Party","Motor Mouth","Trash Panda","Second Ammendment","Road Rage","Crazy Exciting ","Lets Go Brandon","Texas Rattlesnake","Hot Dog","Jurrasic Jungle","Big Bad Bangers","Artillery Shells","Festival Balls","Red Rascals","Frog Fountain","Frosty Mug Of Beer","Lemonade","Lava Lamp","Flight In The Sky","Single Night Parachute","Nutty Monkey","Nutty Monkey","Cuckoo","Cuckoo","Killer Bees","Black Cat's 100 Brick","Black Cat's 100 Brick","Black Cat's 1000","Bunker Buster","Jumbo M-5000 Red","Morning Glories","Morning Glories","10 Color Showtime Sparklers","10 Color Showtime Sparklers","10 Color Showtime Sparklers","10 Color Showtime Sparklers","Neon Sparklers","Patriot Sticks","10 Ball Exploding","10 Ball Exploding","8 Ball Blue Thunder","8 Ball Blue Thunder","Flame Thrower","Zoom Bomb","Cyber Cannon","Balls Of Fire","Bubble Blaster","Super Slugger","Night Saber","Princess of Pyro","Snap Draggons","Snap Draggons","Adult Snappers ","Adult Snappers ","Party Poppers","Party Poppers","Hen Laying Eggs","Hen Laying Eggs","Tanks","Tanks","Strobe Lights","Showtime Smoke Tube","Smoke Balls","Smoke Balls","Diamond Cones","Ground Mine","Jumping Jacks","Whistling Chaser","Whacky Packs","Just For Kids","Pickled Parrot", "Gold Sparklers20inch","The Big Dog", "Dog Bless America", "Oriental Dragon", "Fighting Rooster", "Ground Rattler", "Saturn Missle"]


def addToCart(value):
    value = int(value)
    index = allNDC.index(value)
    item = [allNDC[index], allPrice[index], allName[index]]

    # Check if the item is already in the cart
    for cart_item in currCart:
        if cart_item[0] == item[0]:
            # Increase the quantity if the item is already in the cart
            cart_item[3] += 1
            break
    else: 
        # If the item is not already in the cart, add it with quantity 1
        item.append(1)
        currCart.append(item)
    print(currCart)

def deleteCart():
    global currCart
    currCart = []

def addToCartManual(quantity, price):
    currCart.append(["", price, "MANUAL", quantity])


