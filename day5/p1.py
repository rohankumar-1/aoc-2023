

if __name__ == "__main__":
    # open file, read lines
    f = open("input.txt")
    lines = f.readlines()
    
    # read seeds
    seeds = [int(x) for x in lines[0].split(':')[1].split()]
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
    
    # convert seeds to soil
    for i in range(len(seeds)):
        
        for k in seed_soil.keys():
            if seeds[i]-k >= 0 and seeds[i]-k < seed_soil[k][0]:
                seeds[i] = seed_soil[k][1] + (seeds[i]-k)
                break
        
        for k in soil_fert.keys():
            if seeds[i]-k >= 0 and seeds[i]-k < soil_fert[k][0]:
                seeds[i] = soil_fert[k][1] + (seeds[i]-k)
                break
                
        for k in fert_water.keys():
            if seeds[i]-k >= 0 and seeds[i]-k < fert_water[k][0]:
                seeds[i] = fert_water[k][1] + (seeds[i]-k)
                break
                
        for k in water_light.keys():
            if seeds[i]-k >= 0 and seeds[i]-k < water_light[k][0]:
                seeds[i] = water_light[k][1] + (seeds[i]-k)
                break
        
        for k in light_temp.keys():
            if seeds[i]-k >= 0 and seeds[i]-k < light_temp[k][0]:
                seeds[i] = light_temp[k][1] + (seeds[i]-k)
                break
                
        for k in temp_humid.keys():
            if seeds[i]-k >= 0 and seeds[i]-k < temp_humid[k][0]:
                seeds[i] = temp_humid[k][1] + (seeds[i]-k)
                break
            
        for k in humid_loc.keys():
            if seeds[i]-k >= 0 and seeds[i]-k < humid_loc[k][0]:
                seeds[i] = humid_loc[k][1] + (seeds[i]-k)
                break
                
                
            
    
    print(min(seeds))