agent_name = "bond"
mission_cod = 2134
distance_to_target = 2.5 
mission_active_status = (True)
print(agent_name)
print(mission_cod,distance_to_target,mission_active_status)
print(type(agent_name))
print(type(mission_cod))
print(type(distance_to_target))
print(type(mission_active_status))
travel_distance_feature = (distance_to_target*2)
print(travel_distance_feature)
fual_usage = 1
full_estimation = fual_usage*2
print(full_estimation)
total_fual = 10
fual_after_mission = total_fual-full_estimation
print(fual_after_mission)
countdown_feature = input("how long until your mission will be done in seconds")
countdown_feature = int(countdown_feature)
print(countdown_feature)
countdown_minutes = countdown_feature / 60
coundown_hours = countdown_minutes / 60
print("seconds", countdown_feature)
print("minutes", countdown_minutes)
print("hours", coundown_hours)
