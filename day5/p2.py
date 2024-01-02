
global lines
global minVal
global seed_soil
global soil_fert
global fert_water
global water_light
global light_temp
global temp_humid
global humid_loc

def update(val):
    global minVal
    
    for k in seed_soil.keys():
        if val-k >= 0 and val-k < seed_soil[k][0]:
            val = seed_soil[k][1] + (val-k)
            break
    
    for k in soil_fert.keys():
        if val-k >= 0 and val-k < soil_fert[k][0]:
            val = soil_fert[k][1] + (val-k)
            break
            
    for k in fert_water.keys():
        if val-k >= 0 and val-k < fert_water[k][0]:
            val = fert_water[k][1] + (val-k)
            break
            
    for k in water_light.keys():
        if val-k >= 0 and val-k < water_light[k][0]:
            val = water_light[k][1] + (val-k)
            break
    
    for k in light_temp.keys():
        if val-k >= 0 and val-k < light_temp[k][0]:
            val = light_temp[k][1] + (val-k)
            break
            
    for k in temp_humid.keys():
        if val-k >= 0 and val-k < temp_humid[k][0]:
            val = temp_humid[k][1] + (val-k)
            break
        
    for k in humid_loc.keys():
        if val-k >= 0 and val-k < humid_loc[k][0]:
            val = humid_loc[k][1] + (val-k)
            break
    
    if minVal == -1 or val < minVal:
        minVal = val
    

if __name__ == "__main__":
    # open file, read lines
    f = open("input.txt")
    lines = f.readlines()
    minVal = -1
    
    # read seeds
    seedline = lines[0]
    lines = lines[3:]   # to cut out first two lines (not needed)
    
    # read soil to seed map
    seed_soil = {}
    for i in range(len(lines)):
        if len(lines[i].split()) == 0:
            break
        else:
            # we have a soil to seed line, so fill in map
            vals = [int(x) for x in lines[i].split()]
            seed_soil[vals[1]] = [vals[2] ,vals[0]]
            
    lines = lines[i+2:]
    
    # read soil to fertilizer
    soil_fert = {}
    for i in range(len(lines)):
        if len(lines[i].split()) == 0:
            break
        else:
            # we have a soil to seed line, so fill in map
            vals = [int(x) for x in lines[i].split()]
            soil_fert[vals[1]] = [vals[2] ,vals[0]]
            
    lines = lines[i+2:]
    
    # read fertilizer to water
    fert_water = {}
    for i in range(len(lines)):
        if len(lines[i].split()) == 0:
            break
        else:
            # we have a soil to seed line, so fill in map
            vals = [int(x) for x in lines[i].split()]
            fert_water[vals[1]] = [vals[2] ,vals[0]]
            
    lines = lines[i+2:]
    
    # read water to light
    water_light = {}
    for i in range(len(lines)):
        if len(lines[i].split()) == 0:
            break
        else:
            # we have a soil to seed line, so fill in map
            vals = [int(x) for x in lines[i].split()]
            water_light[vals[1]] = [vals[2] ,vals[0]]
            
    lines = lines[i+2:]
    
    # read light to temperature
    light_temp = {}
    for i in range(len(lines)):
        if len(lines[i].split()) == 0:
            break
        else:
            # we have a soil to seed line, so fill in map
            vals = [int(x) for x in lines[i].split()]
            light_temp[vals[1]] = [vals[2] ,vals[0]]
            
    lines = lines[i+2:]
    
    # read temperature to humidity
    temp_humid = {}
    for i in range(len(lines)):
        if len(lines[i].split()) == 0:
            break
        else:
            # we have a soil to seed line, so fill in map
            vals = [int(x) for x in lines[i].split()]
            temp_humid[vals[1]] = [vals[2] ,vals[0]]
            
    lines = lines[i+2:]
    
    # read humidity to location
    humid_loc = {}
    for i in range(len(lines)):
        if len(lines[i].split()) == 0:
            break
        else:
            # we have a soil to seed line, so fill in map
            vals = [int(x) for x in lines[i].split()]
            humid_loc[vals[1]] = [vals[2] ,vals[0]]
            
    lines = lines[i+2:]
    
    
    
    vals = seedline.split(':')[1].split()
    
    i = 0
    while i < len(vals):
        [update(x) for x in range(int(vals[i]), int(vals[i])+int(vals[i+1]))]
        print("done: ", i)
        i += 2
              

    print(minVal)