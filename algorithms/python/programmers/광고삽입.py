def convert_to_seconds(time):
    hours, minutes, seconds = time.split(':')
    return int(hours) * 60 * 60 + int(minutes) * 60 + int(seconds)


def solution(play_time, adv_time, logs):
    play_time = convert_to_seconds(play_time)
    adv_time = convert_to_seconds(adv_time)

    times = [0 for _ in range(play_time + 1)]
    for log in logs:
        start_at, end_at = log.split('-')

        start_at = convert_to_seconds(start_at)
        end_at = convert_to_seconds(end_at)

        times[start_at] += 1
        times[end_at] -= 1

    for index in range(1, play_time):
        times[index] += times[index-1]

    current_sum = sum(times[:adv_time])
    max_index = 0
    max_summed = current_sum
    for index in range(adv_time, play_time):
        current_sum = current_sum - times[index-adv_time] + times[index]
        if max_summed < current_sum:
            max_summed = current_sum
            max_index = index - adv_time + 1

    return '%02d:%02d:%02d' % (
        max_index / 3600,
        max_index / 60 % 60,
        max_index % 60,
    )
