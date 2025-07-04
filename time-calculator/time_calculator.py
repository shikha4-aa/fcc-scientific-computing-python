def add_time(start, duration, starting_day=None):
    # Days of the week for reference
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Parse start time
    start_time, meridian = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Normalize to 24-hour format
    if meridian.upper() == 'PM' and start_hour != 12:
        start_hour += 12
    if meridian.upper() == 'AM' and start_hour == 12:
        start_hour = 0

    # Parse duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Add times
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour + (end_minute // 60)
    end_minute = end_minute % 60
    days_later = end_hour // 24
    end_hour = end_hour % 24

    # Convert back to 12-hour format
    if end_hour == 0:
        final_hour = 12
        meridian = 'AM'
    elif end_hour < 12:
        final_hour = end_hour
        meridian = 'AM'
    elif end_hour == 12:
        final_hour = 12
        meridian = 'PM'
    else:
        final_hour = end_hour - 12
        meridian = 'PM'

    # Format minute
    final_minute = str(end_minute).zfill(2)
    new_time = f"{final_hour}:{final_minute} {meridian}"

    # Add day of the week if provided
    if starting_day:
        starting_day_index = days_of_week.index(starting_day.capitalize())
        new_day_index = (starting_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    # Add (next day) or (n days later)
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
